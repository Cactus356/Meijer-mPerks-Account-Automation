#!/usr/bin/env python3

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils import create_driver, log_print
from config import mperks_url

def check_rewards(driver, name):
	# Check for unredeemed rewards (X off total purchase usually)
	redeemed_mperks_rewards = None	
	try:
		if driver.current_url != mperks_url:
			driver.get(mperks_url)
			time.sleep(5)
			driver.refresh()
			time.sleep(15)
		redeemed_mperks_rewards = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="mperks-rewards-banner-desktop-update__reward-heading"]'))).text
		time.sleep(1)
	except Exception as e:  # Issue getting points ba
		log_print(f"[{name}] Error getting redeemed rewards: {e}")
	if redeemed_mperks_rewards == 'Your Rewards (0)':
		log_print(f"[{name}] You do not have any rewards waiting to be used")
	else:
		reward_cards = driver.find_elements(By.CLASS_NAME, "mperks-rewards-tile-short-v2__text")
		for card in reward_cards:
			reward_value = card.find_element(By.CLASS_NAME, "mperks-rewards-tile-short-v2__title").text.strip()
			expiration = card.find_element(By.CLASS_NAME, "mperks-rewards-tile-v2__valid-text").text.strip()
			log_print(f"[{name}] $$$ {reward_value}. {expiration}")

	# Check for gift card related earn offers
	earn_tiles = None
	try:
		if driver.current_url != mperks_url:
			driver.get(mperks_url)
			time.sleep(5)
			driver.refresh()
			time.sleep(15)
		WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "earn-tab-tab"))).click()
		time.sleep(2)
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mperks-earn-tile")))
		earn_tiles = driver.find_elements(By.CSS_SELECTOR, ".mperks-earn-tile")
		time.sleep(1)
		for tile in earn_tiles:
			try:
				title = tile.find_element(By.CLASS_NAME, "card-body__title").text.strip()
				description = tile.find_element(By.CLASS_NAME, "mperks-earn-tile__description").text.strip()
				if "gift card" not in description.lower():
					continue
				expiration = tile.find_element(By.CLASS_NAME, "mperks-earn-tile__through-text").text.strip()
				log_print(f"[{name}] {title} {description}. {expiration}")
			except Exception as e:
				log_print(f"[{name}] Error checking earn offers: {e}")
	except Exception as e:  # Issue loading earn offers
		log_print(f"[{name}] Error loading any earn offers: {e}")
	time.sleep(1)
	log_print("")
