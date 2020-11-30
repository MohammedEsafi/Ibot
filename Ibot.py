from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from helpers import login, follow
from time import sleep
from random import randint
import os.path
import json


def reader():
	# read config.json file
	pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')

	with open(pathname) as file:
		return (json.load(file))


def main():
	# get the instagram user & password from standard input
	usr = input("Enter your username: ")
	pwd = getpass(prompt="Enter your password: ")

	options = Options()

	# get rid of the chrome info bar
	options.add_experimental_option("excludeSwitches", ["enable-automation"])

	# disable chrome "save password" popup
	options.add_experimental_option('prefs', {
		'credentials_enable_service': False,
		'profile': {
			'password_manager_enabled': False
		}
	})

	# open a new Chrome browser | get an event-firing-web-driver instance
	global driver
	driver = Chrome(options=options)

	# sleep to prevent issues with the server
	sleep(randint(3, 5))

	# login to instagram account
	login(driver, usr, pwd)

	# follow up
	follow(driver, reader())

	# closes all browser windows and ends driver's session.
	driver.quit()


if __name__ == "__main__":
	main()
