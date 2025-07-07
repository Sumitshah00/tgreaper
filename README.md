# TGReaper
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

<p align="center">
  <img src="https://github.com/user-attachments/assets/6754a5cc-e43e-4830-aeb8-621f606aef97" alt="TGReaper Logo" width="250"/>
</p>


## Overview

**TGReaper** is a powerful open-source CLI tool designed for cybersecurity professionals and researchers to hunt down, analyze, and monitor potentially malicious Telegram bots. It automates the process of infiltrating Telegram bots, capturing and forwarding their messages, and exporting findings for further analysis. TGReaper is intended for educational and research purposes only.

---

## Features

- **Bot Token Validation:** Quickly validate and analyze Telegram bot tokens.
- **Infiltration:** Automate the process of sending commands and capturing messages from Telegram bots.
- **Message Forwarding:** Forward all messages from a target chat to your own account for safe analysis.
- **Export Data:** Export captured messages and logs to files for further investigation.
- **Interactive CLI:** User-friendly interactive mode with animated banners, colored output, and menu-driven workflow.
- **Session Management:** Resume, stop, and clear operations as needed.
- **Environment Variable Support:** Securely manage your Telegram API credentials using a `.env` file.

---

## Legal & Ethical Disclaimer

> **TGReaper is intended for educational and security research purposes only.**
> - Use responsibly and only on systems you own or have explicit permission to test.
> - The authors are not responsible for any misuse or legal consequences.
> - Using this tool may violate Telegram's Terms of Service and could result in account bans.

---

## Installation

### Prerequisites
- Python 3.7+
- Telegram account and API credentials ([get them here](https://my.telegram.org/apps))

---



### Clone the Repository
```bash
git clone https://github.com/sumitshah00/tgreaper.git
cd tgreaper
```

### Install Dependencies
```bash
pip install -r requirements.txt --break-system-packages

```

## 🔐 Telegram API Setup (Quick Guide)

1. Go to [https://my.telegram.org](https://my.telegram.org) and log in.
2. Click **API Development Tools**.
3. Fill in:
   - **App title:** e.g. TGReaper
   - **Short name:** e.g. ghostdinit
4. Click **Create application** to get your **API ID** and **API Hash**.

Create a `.env` file in your project root:
```dotenv
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=+1234567890
```
- `TELEGRAM_API_ID`: Your Telegram API ID
- `TELEGRAM_API_HASH`: Your Telegram API Hash
- `TELEGRAM_PHONE`: Your phone number (with country code) 
## Usage

### Command-Line Interface (CLI)

#### Show Help
```bash
python main.py --help
```

#### Show Version
```bash
python main.py --version
```

#### Run in Interactive Mode (Recommended)
```bash
python main.py --interactive
```
Or simply:
```bash
python main.py
```

### Interactive Mode Walkthrough

1. **Start the tool:**
   ```bash
   python main.py
   ```
2. **Enter the malicious bot token and chat ID** when prompted.
3. **Use the menu** to:
   - Start attack (validate and infiltrate bot)
   - Forward all messages
   - Stop/resume operations
   - Export captured data
   - Clear session logs
   - View help
   - Exit

#### Example Session
```
$python main.py                


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠻⣥⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⡿⠻⣆⠙⠦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠁⠀⠘⣆⡔⢶⣆⠉⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⡿⢿⡀⠉⠀⠞⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⡄⠀⡇⠘⣧⣀⣀⣀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠁⢀⣠⠞⣹⢿⠻⡟⢿⣿⣯⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃⠶⠒⠉⠁⣴⠇⢸⡇⡟⡷⢬⡙⠎⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠇⢀⣠⣄⡀⠚⠁⠀⠈⠀⠀⣷⠀⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣽⣿⣶⠋⢉⡿⠇⠀⠀⠀⠀⠀⣰⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣿⣿⠇⠀⣠⣥⣤⡀⠀⠀⠀⢀⡟⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣿⢀⣾⡟⠉⢹⡇⠀⠀⠀⢸⠁⡿⠙⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢸⣇⣾⡟⠀⠸⡏⣄⡀⠀⠀⢹⢀⡇⢀⢘⢿⣮⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣇⠀⡀⣧⠰⣿⣶⣄⠀⠀⠀⠘⣎⠳⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡿⣿⣆⠹⣿⡐⣾⣷⣹⣆⠀⠀⠀⠘⢷⣄⣻⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣦⠽⣇⣹⣟⢿⠙⠁⠀⠀⠀⣤⠉⠻⣿⣿⣿⣿⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠙⡟⠂⣿⢹⡿⣼⠇⠀⠀⣀⠀⣷⡀⠀⠈⠻⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⠀⠉⢸⡇⠈⣀⣠⣾⠇⠀⠻⣿⣦⣤⣴⣿⠿⣿⡿⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢸⡀⠀⢸⠁⣰⠛⣽⡧⠖⠻⢿⡆⠈⠉⠉⠀⠀⢻⣷⠹⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠘⡇⠀⢸⢰⡏⢰⡟⠀⣀⣀⡼⠃⠀⢀⡆⠀⠀⠘⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣿⣶⣷⣶⣾⣿⣧⣾⣤⣄⣀⣀⣤⣤⣶⡿⠀⠀⠀⢠⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣟⡛⠛⠛⠉⠉⠉⠉⢉⣭⣽⡿⠿⠿⠿⠛⠛⠛⠓⠲⠦⠄⣼⢻⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢉⣼⣿⣿⠿⠛⠛⠁⠀⠀⣠⠖⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⣸⡇⠀
⠀⠀⠀⠀⠀⢀⣴⠿⠛⠁⢀⣀⣀⣀⣀⣀⣄⡀⠀⠀⠀⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠇⣰⣿⠁⠀
⠀⠀⠀⢀⣴⣟⣥⣶⣾⣿⣿⣿⣿⣿⣿⣭⣤⣤⣤⣀⣀⡀⠈⠛⠶⢶⣶⣶⣶⣾⣿⣿⣿⠟⠁⠀⠀
⠀⢀⣴⡿⠟⠋⡽⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀
⠐⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                       👻 Stealth, Intelligence, and Tracking 👻

                                 💀 TGReaper 💀
     
                              👾 Version: 1.0.0 👾

                     💻 Author: Sumit Shah (aka Ghostdinit) 💻

🚀 Welcome to TGReaper Interactive Mode!

🎯 Enter malicious bot token: 


🎯 Hunt Down Malicious Telegram Bots 🎯

═══════════════════════════════════════════════════════════════
🔧 TGReaper Menu
═══════════════════════════════════════════════════════════════
1. 🎯 Start Attack
2. 📨 Forward All Messages
3. ⏹️  Stop Operation
4. ▶️  Resume Operation
5. 📁 Export Captured Data
6. 🔄 Clear Session Logs
7. ❓ Help
8. 🚪 Exit
═══════════════════════════════════════════════════════════════
🎲 Select an option (1-8): 1
  Starting attack process...
✅ Bot validated: @(botname)
Please enter the code you received: 12345   (please enter the code u recived through Telegram)

```

---





## Troubleshooting

- **Missing Credentials:**
  - Ensure your `.env` file is present and correctly filled.
  - Double-check your API ID, hash, and phone number.
- **Account Banned:**
  - Using this tool may violate Telegram's ToS. Use a disposable or research account.
- **Dependencies Not Installed:**
  - Run `pip install -r requirements.txt` again.
- **Errors with Telethon:**
  - Make sure your credentials are valid and you have internet access.
- **Other Issues:**
  - Check for error messages in the terminal and consult the [issues page](https://github.com/yourusername/tgreaper/issues).

---

## Contribution Guide

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit and push (`git commit -am 'Add new feature' && git push origin feature/your-feature`)
5. Open a pull request

All contributions, bug reports, and suggestions are welcome!

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Credits

- **Author:** sumit
- **Original Concept:** 0x6rss (Matkap)
- **Libraries:** [Telethon](https://github.com/LonamiWebs/Telethon), [python-dotenv](https://github.com/theskumar/python-dotenv), [requests](https://docs.python-requests.org/)

---

## Screenshots

![image](https://github.com/user-attachments/assets/ad630778-cc01-4eec-bec7-e16d9b275a48)


---

## Contact

For questions, suggestions, or support, open an issue or contact the maintainer at [Ghostdinit](https://www.instagram.com/ghostdinit/). 
