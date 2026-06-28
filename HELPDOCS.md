
## How does it work?
- Obviously you need Python, I use python3.
- Geckodriver - `sudo pacman -S geckodriver`
- Firefox
- Selenium - `pip install selenium`

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

## Troubleshooting:
If there's an error somewhere in the webpage, the console should print what the error was. For example:
```
[Doug] No coupons found for 'search1'
[Doug] No coupons found for 'search2'
[Doug] Error getting clipped coupons description: Message: Unable to locate element: .//button[contains(., 'Clip')]; For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#nosuchelementexception Stacktrace:
```
If you run into something, open an issue and paste that line and I'll see what I can do to fix it.

## Accounts.txt
Fill in the format of `CommonName:Profile Number` on each line. Common name can be anything, it's just for you to differentiate your accounts. The profile number is found in `about:support` in each profile. Ignore the random characters and just pay attention to the Profile X at the end. You can also add a # to the start of the line to comment it out and skip that account in the checking process.

Example:
```
Account1:Profile 1
#Account2:Profile 2
Whatever1:Profile 4
Name1:Profile3
#Whatever2:Profile 5
Account3:Profile8
```
This will skip Account2 and Whatever2


## Config.py
These are all configuration items. The URL's shouldn't change unless mPerks changes them. The others are user defined based on your system and where you want account.txt and output.txt to be. This is also where you define what gift cards you want to search for, in quotes and separated by a comma.
```
firefox_dir = Path("/home/user/.config/mozilla/firefox")  
accounts_file = "accounts.txt"  
log_file = "output.txt"  
  
mperks_url = "https://www.meijer.com/shopping/mPerks.html"  
coupons_url = "https://www.meijer.com/shopping/coupons.html?search="  
clipped_url = "https://www.meijer.com/shopping/coupons/clippedcoupon.html"  
  
coupon_search_terms = ["visa","mastercard","example1","example2"]
```

## mPerks "unexpected internal error"
I ran into this a lot when I first started this project. I believe it's related to a lot of login attempts, even if successful. Although when I purposefully tried to trigger it by spamming logins, I coulnd't, so who knows. With the way this is set up to use existing sessions, we avoid having the script do any login functions, so realistically you shouldn't even run into this. Basically after the email is entered and submitted, instead of the password page, you'll get an error page with a red box and some message. 
- A refresh of the page usually brings you back to the email entry - Manually enter the email and continue. Hopefully you're on password entry now.
- If it still errors, again refresh and go back to the email entry. Select unlock account and enter the email. They'll send you an email, in my case they always said my account wasn't locked and I was good to log in.
- Go back to the email entry and manually enter it again. Hopefully you're now on the password entry.
 
Basically just refresh / go back / unlock / whatever manually until you get to password entry.
