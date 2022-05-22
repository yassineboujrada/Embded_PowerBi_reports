# from time import time
# from selenium import webdriver
# from PIL import Image
# import time
# from selenium.webdriver.firefox.options import Options as FirefoxOptions

# options = FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)
# url="http://127.0.0.1:3000/dashbord/d72eff1f-51d2-4e98-b093-fddce847145d/c4cabace-7684-47e3-b2f3-9e183ae3322e"
# driver.get(url)
# driver.execute_script("document.body.style.zoom='50%'")
# driver.set_window_size(1920,1080,driver.window_handles[0])
# time.sleep(5)
# driver.save_screenshot('test.png')
# im1=Image.open('test.png')

import os
from urllib import response
import requests
from bs4 import BeautifulSoup

# url = "http://127.0.0.1:3000/dashbord/d72eff1f-51d2-4e98-b093-fddce847145d/c4cabace-7684-47e3-b2f3-9e183ae3322e"
url="https://pythonbasics.org/selenium-firefox/"
reponse = requests.get(url)
print(reponse.status_code)
if reponse.ok:
	soup = BeautifulSoup(reponse.text, "lxml")
	title = str(soup.find("title"))

	title = title.replace("<title>", "")
	title = title.replace("</title>", "")
	print("The title is : " + str(soup))