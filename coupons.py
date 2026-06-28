#!/usr/bin/env python3

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils import create_driver, log_print
from config import mperks_url, clipped_url, coupons_url, coupon_search_terms

def coupons(driver, name):
#coupon-banner-v2__button-badge
#Could check that for 0 from the last coupon search page
	# Check for clipped coupons
	clipped_coupons_count = None
	clipped_coupons = None
	try:
		driver.get(clipped_url)
		time.sleep(5)
		driver.refresh()
		time.sleep(15)
		clipped_coupons_count = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ads-type-heading-03 ads-color-text-01"]'))).text
		time.sleep(1)
	except Exception as e:
		log_print(f"[{name}] Error checking for clipped coupons: {e}")
	if clipped_coupons_count == "Clipped Coupons (0)":
		log_print(f"[{name}] No coupons currently clipped")
	else:
		clipped_coupons = driver.find_elements(By.CLASS_NAME, "coupon-tile-v2__component")
		for coupon in clipped_coupons:
			try:
				coupon_title = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__title").text.strip()
				coupon_description = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__description").text.strip()
				coupon_expiration = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__expire-date").text.strip()
				log_print(f"[{name}] {coupon_title} {coupon_description}. {coupon_expiration}")
			except Exception as e:
				log_print(f"[{name}] Error getting clipped coupons description: {e}")
			time.sleep(1)

	# Search for defined coupons
	coupon_result_count = None
	coupon_results = None
	for search_term in coupon_search_terms:
		try:
			driver.get(coupons_url + search_term)
			time.sleep(5)
			driver.refresh()
			time.sleep(15)
			coupon_result_count = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="coupon-grid__header"]'))).text
		except Exception as e:  # Issue getting points balance
			log_print(f"[{name}] Error searching coupon '{search_term}': {e}")
		if coupon_result_count == "All Coupons (0)":
			log_print(f"[{name}] No coupons found for '{search_term}'")
		else:
			coupon_results = driver.find_elements(By.CLASS_NAME, "coupon-tile-v2__component")
			for coupon in coupon_results:
				try:
					coupon_title = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__title").text.strip()
					coupon_description = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__description").text.strip()
					coupon_expiration = coupon.find_element(By.CLASS_NAME, "coupon-tile-v2__expire-date").text.strip()
					coupon_button = coupon.find_element(By.TAG_NAME, "button")
					coupon_button_text = coupon_button.text.strip()
					time.sleep(1)
					if coupon_button_text == "Clip":
						coupon_button.click()
						log_print(f"[{name}] Clipped coupon - {coupon_title} {coupon_description}. {coupon_expiration}")
					elif coupon_button_text == "Shop":
						log_print(f"[{name}] Coupon already clipped for '{search_term}'")
				except Exception as e:
					log_print(f"[{name}] Error getting clipped coupons description: {e}")
				time.sleep(1)
		time.sleep(1)
	log_print("")




