# 👻 GhostLink  
### Drive-By Download Demonstration & Red-Team Lab Server  
**By AstralGuard Cyber Academy**

---

## 🚀 Overview

**GhostLink** is an elite red-team educational tool that simulates real-world **drive-by download attacks** in a **safe, controlled lab environment**.  
It allows students and professionals to experience:

- Silent payload delivery  
- Redirect-based attack chains  
- Real-time victim logging  
- Stealth tactics used by real attackers  

⚠️ **Strictly for defensive cybersecurity education and awareness.**

---

## 🏛 Created By

**AstralGuard Cyber Academy**  
*Training the next generation of cyber defenders.*

---

## ✨ Features

- ✅ Direct drive-by download simulation  
- ✅ Template-based HTML + redirect attack simulation  
- ✅ Live logging of:
  - Victim IP Address  
  - Timestamp  
  - Downloaded File  
  - User-Agent  
- ✅ Interactive terminal menu  
- ✅ Professional ASCII banner  
- ✅ Safe local lab execution  
- ✅ Cloudflare Tunnel support for remote demos  
- ✅ Zero external Python dependencies  
- ✅ Built for ethical education & demonstrations  

---

## 🧰 Requirements

- Python **3.8+**
- Linux / macOS / Windows
- No external Python libraries required

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AstralGuard/GhostLink.git
2️⃣ Navigate Into the Project
bash
Copy code
cd ghostlink
3️⃣ Initialize the Environment
bash
Copy code
./setup.sh
This checks Python installation and prepares the environment automatically.

4️⃣ Prepare Payloads
Place all demonstration files inside the payloads/ directory.

▶️ Running GhostLink
Start the tool with:

bash
Copy code
python3 ghostlink.py
You will see the interactive menu:

csharp
Copy code
[1] Start Server
[2] Stop Server
[3] About
[4] Exit
Select an option by entering the corresponding number.

⚙️ How GhostLink Works (Technical Overview)
GhostLink simulates two real-world drive-by attack techniques used by attackers:

🧨 1. Direct Drive-By Mode
Victim accesses a direct file URL:

text
Copy code
http://127.0.0.1:8080/christ.apk
The server immediately forces a download using:

css
Copy code
Content-Disposition: attachment
This simulates:

Malvertising

Phishing payload drops

Compromised server delivery

✅ All activity is silently logged to:

text
Copy code
server_logs.txt
🕵️ 2. Template (Redirect) Mode
This simulates real-world exploit kit behavior:

Victim opens an innocent-looking HTML page

Page silently triggers a background download

Page immediately redirects to a legit site

Victim believes it was just a redirect — but payload already dropped ✅

Demonstrates:

Exploit-kit chains

Silent infections

User deception

Stealth delivery

🌍 Remote Access (Optional)
GhostLink can be safely exposed to the internet using Cloudflare Tunnel:

✅ No port opening
✅ No IP exposure
✅ Full HTTPS
✅ Instant shutdown after demo

Perfect for remote student demonstrations in a controlled environment.

📝 Logging
All download activity is recorded in:

text
Copy code
server_logs.txt
Each entry includes:

Timestamp

Victim IP

Downloaded File

User-Agent

⚠️ Legal & Educational Disclaimer
GhostLink is strictly for:

Cybersecurity education

Defensive research

Red-team & blue-team training

Malware awareness programs

❌ Illegal or unauthorized use is strictly prohibited.

AstralGuard Cyber Academy and contributors assume NO liability for misuse.

🌟 Open-Source & Community
GhostLink is open-source for educational purposes.

You are encouraged to:

⭐ Star the repository

🍴 Fork it

📥 Clone it

🛠 Modify the code

🧪 Build your own lab extensions

🔁 Contribute improvements

Knowledge grows when shared responsibly.

📜 License
This project is released under the MIT License — free to use, modify, and distribute for educational purposes with attribution.

© Copyright
© AstralGuard Cyber Academy
All Rights Reserved.

Developed as part of AstralGuard’s professional cybersecurity training programs.

👑 Motto
Stay Elite. Stay Secure.
