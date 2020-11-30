# Ibot

Python script hat can automatically follow users based on hashtag list

## Installation

Install the required Python dependencies using ```pip3```:

```
$ pip3 install -r requirements.txt
```

You have to download chromedriver and put it in a folder that is on your system’s path. *[use Selenium Documentation](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#chromiumchrome)*.

## Configuring

it's easy to set up, ```first``` open ```config.json``` file from cloning content and fill it

```json
{
	"duration": 4,
	"range": 200,
	"hashtags": [
		"fashion",
		"community",
		"selfie"
	]
}
```

| properties |                        usage                            |
|------------|---------------------------------------------------------|
| duration   | sleep time by seconds to prevent issues with the server |
| range      | of follow-up for every hashtag                          |
| hashtags   | list of targeted hashtags                               |

## Running

After the configuration file you now can run the script

```
$ python3 Ibot.py
```