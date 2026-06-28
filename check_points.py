#!/usr/bin/env python3

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils import create_driver, log_print
from config import mperks_url

def check_points(driver, name):
	# Get total mPerks points
	mperks_points = None
	mperks_points_alt = None	
	try:
		driver.get(mperks_url)
		time.sleep(5)
		driver.refresh()
		time.sleep(15)
		mperks_points = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="mperks-rewards-banner-desktop-update__points"]'))).text
		mperks_points_alt = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="account-flyout-v2__mperks-text"]'))).text
	except Exception as e:  # Issue getting points balance
		log_print(f"[{name}] Error getting points balance: {e}")
	if mperks_points is None or mperks_points_alt is None:
		log_print(f"[{name}] Error reading points, trying again")
		mperks_points = None
		mperks_points_alt = None
		try:
			time.sleep(1)
			driver.refresh()
			time.sleep(15)  
			mperks_points = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="mperks-rewards-banner-desktop-update__points"]'))).text
			mperks_points_alt = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="account-flyout-v2__mperks-text"]'))).text
		except Exception as e:  # Issue getting points balance
			log_print(f"[{name}] Error getting points balance: {e}")
		if mperks_points is None or mperks_points_alt is None:
			log_print(f"[{name}] Error reading points again, giving up")
		else:
			log_print(f"[{name}] *** mPerks Points: {mperks_points}")
	else:
		log_print(f"[{name}] mPerks Points: {mperks_points}")

	# Check for any expiring points
	expiring_points = None
	try:
		if driver.current_url != mperks_url:
			driver.get(mperks_url)
			time.sleep(5)
			driver.refresh()
			time.sleep(15)
		expiring_points = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='ads-notification']"))).text
	except TimeoutException:
		log_print(f"[{name}] No expiring points found")
	except Exception as e:
		log_print(f"[{name}] Error getting expiring points: {e}")
	else:
		log_print(f"[{name}] !!! {expiring_points}")
	time.sleep(1)
	log_print("")
