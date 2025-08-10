import time
import os
import json
from colorama import init, Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize Colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    clear_screen()
    logo_lines = [
        (" /$$      /$$ /$$$$$$$        /$$$$$$$  /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$", Fore.CYAN),
        ("| $$$    /$$$| $$__  $$      | $$__  $$| $$__  $$|_  $$_/| $$$ | $$ /$$__  $$| $$_____/ ", Fore.CYAN),
        ("| $$$$  /$$$$| $$  \\ $$      | $$  \\ $$| $$  \\ $$  | $$  | $$$$| $$| $$  \\__/| $$       ", Fore.CYAN),
        ("| $$ $$/$$ $$| $$$$$$$/      | $$$$$$$/| $$$$$$$/  | $$  | $$ $$ $$| $$      | $$$$$    ", Fore.CYAN),
        ("| $$  $$$| $$| $$__  $$      | $$____/ | $$__  $$  | $$  | $$  $$$$| $$      | $$__/    ", Fore.CYAN),
        ("| $$\\  $ | $$| $$  \\ $$      | $$      | $$  \\ $$  | $$  | $$\\  $$$| $$    $$| $$       ", Fore.CYAN),
        ("| $$ \\/  | $$| $$  | $$      | $$      | $$  | $$ /$$$$$$| $$ \\  $$|  $$$$$$/| $$$$$$$$ ", Fore.CYAN),
        ("|__/     |__/|__/  |__/      |__/      |__/  |__/|______/|__/  \\__/ \\______/ |________/ ", Fore.CYAN),
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

def animated_input(prompt_text):
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def load_cookies(driver, cookies_file):
    with open(cookies_file, "r") as f:
        cookies = json.load(f)
    driver.get("https://www.facebook.com")
    for cookie in cookies:
        driver.add_cookie(cookie)

def send_messages(cookies_file, target_uid, messages_file, haters_name, speed):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--headless=new")  # remove if you want to see browser
    driver = webdriver.Chrome(options=chrome_options)

    # Load Messenger with cookies
    driver.get("https://www.messenger.com")
    driver.delete_all_cookies()
    with open(cookies_file, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(f"https://www.messenger.com/t/{target_uid}")
    time.sleep(5)

    with open(messages_file, "r") as file:
        messages = [line.strip() for line in file if line.strip()]

    message_box_xpath = '//div[@role="textbox"]'

    while True:
        for msg in messages:
            full_message = f"{haters_name} {msg}"
            try:
                box = driver.find_element(By.XPATH, message_box_xpath)
                box.send_keys(full_message)
                box.send_keys(Keys.ENTER)
                print(Fore.CYAN + f"[📨] Sent: {full_message}")
                time.sleep(speed)
            except Exception as e:
                print(Fore.RED + f"[x] Error sending message: {e}")
                driver.get(f"https://www.messenger.com/t/{target_uid}")
                time.sleep(3)

def main():
    clear_screen()
    display_animated_logo()

    entered_password = animated_input("ENTER OWNER NAME➜")
    if entered_password != "BROKEN-PRINCE":
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting.")
        exit(1)

    cookies_file = animated_input("((☣️)) ENTER COOKIES FILE (cookies.json)➜")
    target_id = animated_input("((☣️)) ENTER CONVO UID ➜")
    haters_name = animated_input("((☣️)) ENTER HATER NAME➜")
    messages_file = animated_input("((☣️)) ENTER MESSAGE FILE➜")
    speed = float(animated_input("((☣️)) ENTER DELAY/TIME (seconds) ➜"))

    send_messages(cookies_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
