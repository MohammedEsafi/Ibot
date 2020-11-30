from time import sleep
from random import randint


def login(driver, usr, pwd):
	# open the Instagram login page
	driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

	# some shut-eye :)
	sleep(randint(3, 5))

	# find username & password fields and set their input
	username = driver.find_element_by_name('username')
	username.send_keys(usr)
	password = driver.find_element_by_name('password')
	password.send_keys(pwd)

	# get the login button & click
	submit = driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button')
	submit.click()

	# some shut-eye :)
	sleep(randint(3, 5))

	try:
		# in case you get a popup to save your login info
		element = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
		if (element.text == 'Not Now'):
			element.click()

		# notifications popup, press not now
		element = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
		if (element.text == 'Not Now'):
			element.click()
	except:
		pass
