from time import sleep

def login(driver, usr, pwd):
	# open the Instagram login page
	driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

	# some shut-eye :)
	sleep(5)

	# find username & password fields and set their input
	username = driver.find_element_by_name('username')
	username.send_keys(usr)
	password = driver.find_element_by_name('password')
	password.send_keys(pwd)

	# get the login button & click
	submit = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
	submit.click()

	# some shut-eye :)
	sleep(5)

	# in case you get a popup after logging in, press not now
	not_now = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
	not_now.click()