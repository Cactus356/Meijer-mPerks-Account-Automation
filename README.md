

# Meijer mPerks Account Automation
Uses existing Firefox profiles with a logged in mPerks account to check and log points, rewards, and coupons for each account. 

## Features:  
For each logged in account, it will navigate to the mPerks website and check any or all of the following:
- Total mPerks points, including any expiring
- Unused rewards + expiration date (ie save $5 on your total purchase. Valid thru x/x/xx)
- Unused earn tasks (ie earn 5,000 points for every $50 spent on select gift cards. Through x/x/xx)
- Coupon clipper - Clip coupons based off user defined terms, and shows all existing clipped coupons on the account
- Prints output directly to the console and also saves into an output.txt file

- (PLANNED) - Points redeemer - Redeems the largest available reward for cash off next purchase until you have no points left (ie 75k points into $50, $20, and $5 off your next purchase)
- (PLANNED) - Multi-threading to allow faster checking

<details>
  <summary>  Click to show an example output.txt</summary>
  
  ![img](https://i.imgur.com/oIxsrtQ.png)
</details>

## How does it work?
Obviously you need Python, I use python3.

Geckodriver - `sudo pacman -S geckodriver`
Firefox
Selenium - `pip install selenium`

In Firefox, create a new profile and name it whatever you want, we'll say it's called Account1. Log into mPerks on this profile, we'll refer to this mPerks account as 'Account1' as well. Navigate to `about:support` and note the profile directory.

![img](https://i.imgur.com/6S96DDZ.png)

The part that says 'Profile 1' is what we need for the accounts.txt file. Fill this out in the form of 'CommonName:Profile Number', and do a line for all accounts/profiles you want to check. The common name is anything you want, this is just what will be logged to the console and output.txt, so we'll use our Account1. If you don't want an account to be checked, you can comment it out (Adding a # at the start of the line), or of course delete it from accounts.txt altogether.

For example:
```
Account1:Profile 1
Account2:Profile 2
#Account3:Profile 3
```
They might not always match, ie Account5 might use Profile 8, I'd just verify with `about:support`

Once you have the accounts set up in your Firefox profiles, run main.py and select what actions you want to check.


## What's the point of this?
Some users have multiple mPerks accounts to take advantage of promo offers more than once, often to farm credit card points. Keeping track of what accounts have used gift card offers, how many points they have, and if the points have been redeemed for coupons can get confusing. Instead of manually checking everything on all accounts, this will just do it for you and print a report of everything at the end.

## Disclaimers
- This is not for malicious use and/or account cracking. It only uses existing mPerks account sessions, it does not perform any login actions.
- This is probably against the mPerks TOS in some way, so this is for hypothetical and testing purposes only. 
- I am not a python developer. I can use Google, ChatGPT, and some free time on the weekends. Between all of that, I can toss some stuff together. Yes, I'm sure this code could be better. Yes, I'm sure there's issues. Report them or fix them yourself.
