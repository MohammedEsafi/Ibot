from random import randint
from time import sleep


def follow(driver, config):
	for hashtag in config['hashtags']:
		driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')

		thumbnail = driver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div')
		thumbnail.click()

		for _ in range(config['range']):
			# some shut-eye :)
			sleep(config['duration'])

			# if we already follow, do not unfollow
			button = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button')
			
			if button.text == 'Follow':
				button.click()

			# some shut-eye :)
			sleep(config['duration'])
			
			# next picture
			driver.find_element_by_link_text('Next').click()
