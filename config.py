#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime

date = datetime.now().strftime('%m-%d-%Y %H:%M:%S')

firefox_dir = Path("/home/user/.config/mozilla/firefox")
accounts_file = "accounts.txt"
log_file = "output.txt"

mperks_url = "https://www.meijer.com/shopping/mPerks.html"
coupons_url = "https://www.meijer.com/shopping/coupons.html?search="
clipped_url = "https://www.meijer.com/shopping/coupons/clippedcoupon.html"

coupon_search_terms = ["visa","mastercard"]
