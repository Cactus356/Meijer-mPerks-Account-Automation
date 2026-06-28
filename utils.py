#!/usr/bin/env python3

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from config import log_file
from config import date, firefox_dir, accounts_file, log_file

def log_print(text):
        print(text)
        with open(log_file, "a") as f:
                f.write(text + "\n")

def create_driver(headless, profile_path):
        options = Options()
        if headless == "Y":
                options.add_argument("-headless")
        options.add_argument("-profile")
        options.add_argument(profile_path)
        return webdriver.Firefox(options=options)

# ---------------- ACCOUNT LOADER ----------------
def load_accounts(): 
        accounts = []
        with open(accounts_file, "r") as f:
                for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                                continue
                        name, profile_name = line.split(":", 1)
                        matches = list(firefox_dir.glob(f"*.{profile_name.strip()}"))
                        if not matches:
                                raise Exception(f"No Firefox profile found for {profile_name}")
                        accounts.append((name.strip(), str(matches[0])))
        return accounts
