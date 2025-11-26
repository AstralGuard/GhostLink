from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import urllib.parse
from datetime import datetime
import threading
import signal
import sys
import time

# ===== CONFIG =====
PAYLOAD_DIR = "payloads"
LOG_FILE = "server_logs.txt"
PORT = 8080
SAFE_REDIRECT_URL = "https://academy.astralguard.online/safe-demo"

server_instance = None
server_thread = None
MODE = None  # direct | template

# ===== COLORS =====
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"


# ===== ASTRALGUARD BANNER =====
def show_banner():
    os.system("clear" if os.name == "posix" else "cls")
    banner = f"""
{GREEN}{BOLD}
   █████╗ ███████╗████████╗██████╗  █████╗ ██╗      ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ 
  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
  ███████║███████╗   ██║   ██████╔╝███████║██║     ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
  ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║     ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
  ██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 

        ◆  A S T R A L G U A R D   C Y B E R   A C A D E M Y  ◆
        ◆   Drive-By Download Demonstration Server (LAB)   ◆
{RESET}
"""
    print(banner)


# ===== HTTP HANDLER =====
class DriveByHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global MODE
        parsed_path = urllib.parse.urlparse(self.path)

        # ===== TEMPLATE MODE ROOT =====
        if MODE == "template" and parsed_path.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            with open("template.html", "r") as f:
                self.wfile.write(f.read().encode())
            return

        # ===== PAYLOAD HANDLING =====
        requested_file = os.path.basename(parsed_path.path)
        file_path = os.path.join(PAYLOAD_DIR, requested_file)

        if os.path.isfile(file_path):
            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Disposition", f'attachment; filename="{requested_file}"')
            self.end_headers()

            with open(file_path, "rb") as f:
                self.wfile.write(f.read())

            self.log_download(requested_file)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found.")

    def log_download(self, filename):
        ip = self.client_address[0]
        user_agent = self.headers.get("User-Agent", "Unknown")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{timestamp}] IP: {ip} | File: {filename} | UA: {user_agent}\n"

        with open(LOG_FILE, "a") as log:
            log.write(log_entry)

    def log_message(self, format, *args):
        return


# ===== SERVER CONTROLS =====
def start_server(selected_mode):
    global server_instance, server_thread, MODE
    MODE = selected_mode

    if server_instance:
        print(f"{YELLOW}[!] Server already running.{RESET}")
        return

    if not os.path.exists(PAYLOAD_DIR):
        os.mkdir(PAYLOAD_DIR)

    server_instance = HTTPServer(("0.0.0.0", PORT), DriveByHandler)

    def run():
        print(f"{GREEN}[+] Server ONLINE at http://127.0.0.1:{PORT}{RESET}")
        print(f"{GREEN}[+] Mode         : {MODE.upper()}{RESET}")
        print(f"{GREEN}[+] Payload Dir  : ./{PAYLOAD_DIR}{RESET}")
        print(f"{GREEN}[+] Log File     : {LOG_FILE}{RESET}")

        if MODE == "direct":
            print(f"{CYAN}Victim URL: http://127.0.0.1:{PORT}/payloads/yourfile.ext{RESET}")
        else:
            print(f"{CYAN}Victim URL: http://127.0.0.1:{PORT}/{RESET}")
            print(f"{CYAN}Redirects to: {SAFE_REDIRECT_URL}{RESET}")

        print()
        server_instance.serve_forever()

    server_thread = threading.Thread(target=run)
    server_thread.daemon = True
    server_thread.start()


def stop_server():
    global server_instance

    if server_instance:
        server_instance.shutdown()
        server_instance.server_close()
        server_instance = None
        print(f"{RED}[!] Server stopped successfully.{RESET}")
    else:
        print(f"{YELLOW}[!] Server is not running.{RESET}")


# ===== ABOUT =====
def about():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{GREEN}{BOLD}

╔══════════════════════════════════════════════════════════════╗
║            ASTRALGUARD CYBER ACADEMY LAB SERVER              ║
╠══════════════════════════════════════════════════════════════╣
║  Purpose  : Drive-By Downloads & Payload Dropper Demo        ║
║  Mode     : Direct & Template Redirect Simulation            ║
║  Logging  : IP, Timestamp, User-Agent, Accessed File         ║
║                                                              ║
║  ⚠ For EDUCATIONAL PURPOSES ONLY                             ║
║  Unauthorized use is strictly prohibited.                    ║
╚══════════════════════════════════════════════════════════════╝

{RESET}""")
    input(f"{CYAN}Press ENTER to return to the menu...{RESET}")


# ===== MENU =====
def menu():
    while True:
        show_banner()
        print(f"{CYAN}")
        print("  [1] Start Direct Drive‑By Server")
        print("  [2] Start Template Redirect Demo")
        print("  [3] Stop Server")
        print("  [4] About")
        print("  [5] Exit")
        print(f"{RESET}")

        choice = input(f"{GREEN}Select an option >>> {RESET}")

        if choice == "1":
            start_server("direct")
            input(f"{CYAN}Press ENTER to continue...{RESET}")

        elif choice == "2":
            start_server("template")
            input(f"{CYAN}Press ENTER to continue...{RESET}")

        elif choice == "3":
            stop_server()
            input(f"{CYAN}Press ENTER to continue...{RESET}")

        elif choice == "4":
            about()

        elif choice == "5":
            graceful_exit()

        else:
            print(f"{RED}[!] Invalid option!{RESET}")
            time.sleep(1)


# ===== GRACEFUL CTRL+C =====
def graceful_exit(signum=None, frame=None):
    print(f"\n{GREEN}{BOLD}[✓] Thanks for learning with AstralGuard!{RESET}")
    print(f"{GREEN}[✓] Exiting server gracefully...{RESET}")
    print(f"{GREEN}[✓] Stay elite. Stay secure. 👑{RESET}")
    stop_server()
    os._exit(0)


signal.signal(signal.SIGINT, graceful_exit)


# ===== MAIN =====
if __name__ == "__main__":
    menu()
