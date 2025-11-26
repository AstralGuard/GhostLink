=====================================================================
                           GHOSTLINK
        Drive-By Download Demonstration & Red-Team Lab Server
                 By AstralGuard Cyber Academy
=====================================================================

GhostLink is an elite red-team educational tool that simulates real-world
drive-by download attacks in a safe controlled lab environment. It allows
students and security professionals to experience silent payload delivery,
redirect-based attack chains, live victim logging, and stealth techniques
used by real attackers — strictly for DEFENSIVE EDUCATION.

This tool was designed and built for cybersecurity awareness, red-team
training, blue-team detection, and attack surface understanding.

---------------------------------------------------------------------
CREATED BY
---------------------------------------------------------------------
AstralGuard Cyber Academy
Training the next generation of cyber defenders.

---------------------------------------------------------------------
FEATURES
---------------------------------------------------------------------
• Direct drive-by download simulation  
• Template-based (HTML + redirect) drive-by attack simulation  
• Live logging of:
  - Victim IP address
  - Timestamp
  - Downloaded file
  - User-Agent
• Clean interactive terminal menu
• Professional ASCII banner interface
• Safe local lab execution
• Cloudflare Tunnel compatible for remote demos
• Zero external Python dependencies
• Designed for ethical education and demonstrations

---------------------------------------------------------------------
REQUIREMENTS
---------------------------------------------------------------------
• Python 3.8+
• Linux / macOS / Windows
• No external Python libraries required

---------------------------------------------------------------------
INSTALLATION
---------------------------------------------------------------------

1. Clone the repository:
   git clone https://github.com/YOUR-USERNAME/ghostlink.git

2. Navigate into the directory:
   cd ghostlink

3. Initialize the environment:
   ./setup.sh

   (This checks Python installation and prepares the environment)

4. Prepare payloads folder:
   Place all demonstration files inside the "payloads" directory.

---------------------------------------------------------------------
RUNNING GHOSTLINK
---------------------------------------------------------------------

Start the tool:
   python3 ghostlink.py

You will see an interactive menu:

  [1] Start Server
  [2] Stop Server
  [3] About
  [4] Exit

Select an option by entering the corresponding number.

---------------------------------------------------------------------
HOW GHOSTLINK WORKS (TECHNICAL OVERVIEW)
---------------------------------------------------------------------

GhostLink simulates two real-world drive-by delivery methods:

========================
1) DIRECT DRIVE-BY MODE
========================
In this mode, a victim accesses a direct file URL such as:

http://127.0.0.1:8080/test.apk

The server immediately forces a download using the HTTP header:
Content-Disposition: attachment

This mimics malicious file delivery from compromised servers,
malvertising links, or phishing campaigns.

Victim activity is silently logged to:
server_logs.txt

========================
2) TEMPLATE (REDIRECT) MODE
========================
This mode simulates what real attackers do:

1. Victim loads an innocent-looking HTML page.
2. The page silently triggers the download in the background.
3. The page immediately redirects the victim to a legitimate-looking
   website or awareness page.
4. Victim believes they were only redirected, unaware the payload
   already downloaded.

This method demonstrates:
• Exploit kit behavior
• Malvertising delivery chains
• Drive-by infection realism
• User deception tactics

---------------------------------------------------------------------
REMOTE ACCESS (OPTIONAL)
---------------------------------------------------------------------

GhostLink can be safely exposed to the internet using Cloudflare Tunnel
for live classroom demonstrations without opening ports or exposing
your IP address.

This allows students to experience real-world delivery remotely in a
completely controlled environment.

---------------------------------------------------------------------
LOG FILE
---------------------------------------------------------------------

All downloads are recorded in:
server_logs.txt

Each entry includes:
• Timestamp
• Victim IP
• Downloaded file
• User-Agent

---------------------------------------------------------------------
EDUCATIONAL USE & LEGAL NOTICE
---------------------------------------------------------------------

This tool is strictly for:
• Cybersecurity education
• Defensive research
• Red-team & blue-team training
• Malware awareness programs

Any use of this tool for illegal activity, unauthorized access, or
malicious exploitation is strictly prohibited.

The authors, AstralGuard Cyber Academy, and contributors assume NO
liability for misuse of this software.

---------------------------------------------------------------------
OPEN SOURCE & COMMUNITY
---------------------------------------------------------------------

GhostLink is open-source for educational purposes.

You are encouraged to:
• Star ⭐ the repository
• Fork 🍴 it
• Clone it
• Modify the source code
• Build your own lab extensions
• Contribute improvements

Knowledge grows when shared responsibly.

---------------------------------------------------------------------
CREDITS & COPYRIGHT
---------------------------------------------------------------------

© AstralGuard Cyber Academy  
All Rights Reserved.

GhostLink is developed as part of AstralGuard’s professional
cybersecurity training and awareness programs.

---------------------------------------------------------------------
STAY ELITE. STAY SECURE.
---------------------------------------------------------------------
