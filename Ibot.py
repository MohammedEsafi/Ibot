from selenium import webdriver
from time import sleep
from getpass import getpass
from helpers import login

if __name__ == "__main__":
	# get the instagram user & password from standard input
	usr = input("Enter your username: ")
	pwd = getpass(prompt="Enter your password: ")

	# open a new Chrome browser
	driver = webdriver.Chrome()

	# sleep for 3 seconds to prevent issues with the server
	sleep(3)

	# login to instagram account
	login(driver, usr, pwd)