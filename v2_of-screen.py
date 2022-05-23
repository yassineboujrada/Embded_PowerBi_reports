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

def get_contenet_of_html():
    url = "http://127.0.0.1:3000/my_table_of_period"
    # url="https://pythonbasics.org/selenium-firefox/"
    reponse = requests.get(url)
    print(reponse.status_code)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, "lxml")
        title = str(soup.find("title"))

        title = title.replace("<title>", "")
        title = title.replace("</title>", "")
        print("The title is : " + str(soup))

# from flask import Flask, render_template
# from bs4 import BeautifulSoup
# import requests

# source = requests.get('http://127.0.0.1:3000/my_table_of_period').text
# soup = BeautifulSoup(source, 'lxml')

# print(soup)

# import pdfkit 
# pdfkit.from_url(['google.com', 'geeksforgeeks.org', 'facebook.com'], 'shaurya.pdf')
# pdfkit.from_file(['file1.html', 'file2.html'], 'out.pdf')

from scrapingbee import ScrapingBeeClient

url="https://ep76.fr/formations/"
api="9IG2PK0A6O7NV7PNGQYOIURT4IMKW0U0TG5WCHJ6BJ48XM18GK95HMA6TBYXF9KGL75TKY1ZOL0GPDVW"
client = ScrapingBeeClient(api_key=api)
response = client.get(
	url,
	# 'http://192.168.0.192:3000/dashbord/d72eff1f-51d2-4e98-b093-fddce847145d/c4cabace-7684-47e3-b2f3-9e183ae3322e', # Demo link
	params={
		'screenshot': True, # Take a full screenshot of the page
	}
)
if response.ok:
	with open("./screenshot.png", "wb") as f:
		f.write(response.content)
else:
	print(response.content)