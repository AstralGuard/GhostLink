👻 GHOSTLINK
Drive‑By Download Demonstration & Red‑Team Lab Server
By AstralGuard Cyber Academy

────────────────────────────────────────

🚀 OVERVIEW

GhostLink is an elite red‑team educational tool that simulates real‑world drive‑by download attacks in a safe, controlled lab environment. It is designed for cybersecurity students, red‑team trainees, and defensive security professionals to understand how silent delivery attacks work in the real world.

With GhostLink, you can safely demonstrate:

• Silent payload delivery
• Redirect‑based attack chains
• Real‑time victim logging
• Stealth techniques used by real attackers

⚠️ This tool is strictly for defensive cybersecurity education and awareness only.

────────────────────────────────────────

🏛 CREATED BY

AstralGuard Cyber Academy
Training the next generation of cyber defenders.

────────────────────────────────────────

✨ FEATURES

• Direct drive‑by download simulation
• Template‑based HTML + redirect attack simulation
• Live logging of victim activity
• Logs include:
– Victim IP Address
– Timestamp
– Downloaded File
– User‑Agent
• Interactive terminal menu
• Professional ASCII banner
• Safe local lab execution
• Cloudflare Tunnel support for remote demos
• Zero external Python dependencies
• Built for ethical education and demonstrations

────────────────────────────────────────

🧰 REQUIREMENTS

• Python 3.8 or higher
• Linux, macOS, or Windows
• No external Python libraries required

────────────────────────────────────────

📦 INSTALLATION

Clone the repository

git clone https://github.com/AstralGuard/GhostLink.git

Navigate into the project directory

cd ghostlink

Initialize the environment

./setup.sh

This script verifies Python installation and prepares the environment automatically.

Prepare payloads

Place all demonstration files inside the payloads directory.

────────────────────────────────────────

▶️ RUNNING GHOSTLINK

Start the tool using:

python3 ghostlink.py

You will see the interactive menu:

[1] Start Server
[2] Stop Server
[3] About
[4] Exit

Select an option by entering the corresponding number.

────────────────────────────────────────

⚙️ HOW GHOSTLINK WORKS (TECHNICAL OVERVIEW)

GhostLink implements two real‑world drive‑by attack techniques commonly used by real attackers.

🧨 1. DIRECT DRIVE‑BY MODE

The victim accesses a direct file URL such as:

http://127.0.0.1:8080/example.apk

The server forces an immediate download using the HTTP header:

Content‑Disposition: attachment

This simulates:

• Malvertising delivery
• Phishing payload drops
• Compromised server delivery

All activity is silently logged to:

server_logs.txt

────────────────────────────────────────

🕵️ 2. TEMPLATE (REDIRECT) MODE

This mode simulates exploit‑kit style attack behavior:

• Victim opens an innocent‑looking HTML page
• The page silently triggers a background download
• The page immediately redirects to a legitimate website
• The victim believes it was only a redirect — but the payload is already delivered

This demonstrates:

• Exploit‑kit delivery chains
• Silent infection techniques
• User deception methods
• Stealth payload delivery

────────────────────────────────────────

🌍 REMOTE ACCESS (OPTIONAL)

GhostLink can be safely exposed to the internet using Cloudflare Tunnel:

• No port opening required
• No IP address exposure
• Full HTTPS encryption
• Instant shutdown after the demo

This is ideal for remote student demonstrations in a controlled lab environment.

────────────────────────────────────────

📝 LOGGING

All download activity is recorded in:

server_logs.txt

Each log entry contains:

• Timestamp
• Victim IP Address
• Downloaded File
• User‑Agent

────────────────────────────────────────

⚠️ LEGAL & EDUCATIONAL DISCLAIMER

GhostLink is strictly intended for:

• Cybersecurity education
• Defensive security research
• Red‑team & blue‑team training
• Malware awareness programs

❌ Any illegal, unauthorized, or malicious use is strictly prohibited.

AstralGuard Cyber Academy and its contributors assume NO liability for misuse of this tool.

────────────────────────────────────────

🌟 OPEN‑SOURCE & COMMUNITY

GhostLink is open‑source for educational purposes.

You are encouraged to:

⭐ Star the repository
🍴 Fork the project
📥 Clone the code
🛠 Modify and extend functionality
🧪 Build your own lab extensions
🔁 Contribute improvements

Knowledge grows when shared responsibly.

────────────────────────────────────────

📜 LICENSE

This project is released under the MIT License — free to use, modify, and distribute for educational purposes with proper attribution.

────────────────────────────────────────

© COPYRIGHT

© AstralGuard Cyber Academy
All Rights Reserved.

Developed as part of AstralGuard’s professional cybersecurity training programs.

────────────────────────────────────────

👑 MOTTO

AstralGuard | Guardian of the Digital Realm.

────────────────────────────────────────
