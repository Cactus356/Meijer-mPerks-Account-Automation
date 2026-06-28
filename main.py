#!/usr/bin/env python3

from datetime import datetime
import time
import traceback
import re

from check_points import check_points
from check_rewards import check_rewards
from coupons import coupons
from utils import create_driver, log_print, load_accounts
from config import date, firefox_dir, accounts_file, log_file

# ---------------- MAIN ----------------
def main():
	headless = input("Run in headless mode? (Y or N): ").strip().upper()
#	headless = "n"
	accounts = load_accounts()
	while True:
		print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   MAIN MENU   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
		print("1. Check points, including any expiring if applicable\n2. Check rewards, both claimed and available to earn")
		print("3. Check coupons, both clipped and search for user defined terms\n4. Check both points and rewards")
		print("5. Check points, rewards, and coupons\n8. Print instructions\n9. Quit")
		menu_choice = input("\nEnter your choice: ")
#		menu_choice = "1"
		if menu_choice == "1":
			log_print(f"\n=== CHECKING POINTS {date} ===\n")
			for name, profile in accounts:
				print(f"[{name}] --- Opening browser ---\n")
				driver = create_driver(headless, profile)
				try:
					check_points(driver, name)
				except Exception as e:  # Issue checking the account
					log_print(f"[{name}] Error running check points module: {e}")
				finally:
					driver.quit()
				print(f"[{name}] --- Closing browser ---\n\n")
			log_print(f"=== DONE CHECKING POINTS {date} ===\n\n")
		
		elif menu_choice == "2":
			log_print(f"\n=== CHECKING REWARDS {date} ===\n")
			for name, profile in accounts:
				print(f"[{name}] --- Opening browser ---\n")
				driver = create_driver(headless, profile)
				try:
					check_rewards(driver, name)
				except Exception as e:  # Issue checking the account
					log_print(f"[{name}] Error running check rewards module: {e}")
				finally:
					driver.quit()
				print(f"[{name}] --- Closing browser ---\n\n")
			log_print(f"=== DONE CHECKING REWARDS {date} ===\n\n")

		elif menu_choice == "3":
			log_print(f"\n=== CHECKING COUPONS {date} ===\n")
			for name, profile in accounts:
				print(f"[{name}] --- Opening browser ---\n")
				driver = create_driver(headless, profile)
				try:
					coupons(driver, name)
				except Exception as e:  # Issue checking the account
					log_print(f"[{name}] Error running check rewards module: {e}")
				finally:
					driver.quit()
				print(f"[{name}] --- Closing browser ---\n\n")
			log_print(f"=== DONE CHECKING COUPONS {date} ===\n\n")

		elif menu_choice == "4":
			log_print(f"\n=== CHECKING POINTS AND REWARDS {date} ===\n")
			for name, profile in accounts:
				print(f"[{name}] --- Opening browser ---\n")
				driver = create_driver(headless, profile)
				try:
					check_points(driver, name)
					check_rewards(driver, name)
				except Exception as e:  # Issue checking the account
					log_print(f"[{name}] Error running check points or check rewards module: {e}")
				finally:
					driver.quit()
				print(f"[{name}] --- Closing browser ---\n\n")
			log_print(f"=== DONE CHECKING POINTS AND REWARDS {date} ===\n\n")

		elif menu_choice == "5":
			log_print(f"\n=== CHECKING POINTS, REWARDS, AND COUPONS {date} ===\n")
			for name, profile in accounts:
				print(f"[{name}] --- Opening browser ---\n")
				driver = create_driver(headless, profile)
				try:
					check_points(driver, name)
					check_rewards(driver, name)
					coupons(driver, name)
				except Exception as e:  # Issue checking the account
					log_print(f"[{name}] Error running check points or check rewards module: {e}")
				finally:
					driver.quit()
				print(f"[{name}] --- Closing browser ---\n\n")
			log_print(f"=== DONE CHECKING POINTS, REWARDS, AND COUPONS {date} ===\n\n")

		elif menu_choice == "8":
			print("\n\n##############################   INSTRUCTIONS   ##############################\n")
			print("Create a new Firefox profile for each mPerks account. Log into mPerks in each profile.")
			print("Confirm the profile name and path by typing 'about:support' into the address bar.")
			print("You should see a line that says something like 'Profile Directory /home/user/.config/mozilla/firefox/msZaVHXp.Profile 1'")
			print("That profile directory needs to be added to the config.py, along with an accounts.txt file")
			print("Place account names (anything you want) and their profile number in accounts.txt in the form of 'Account 1:Profile 1'")
			print("For profile number, ignore the first random part of the profile name (msZaVHXp.Profile 1 is just 'Profile 1').")
			print("\n##############################   INSTRUCTIONS   ##############################\n")		

		elif menu_choice == "9":
			print("Quitting.")
			break
		
		else:
			print("Invalid choice, please enter 1,2,8, or 9")



if __name__ == "__main__":
    main()
