from scrapingbee import ScrapingBeeClient

def screen():
    api="9IG2PK0A6O7NV7PNGQYOIURT4IMKW0U0TG5WCHJ6BJ48XM18GK95HMA6TBYXF9KGL75TKY1ZOL0GPDVW"
    client = ScrapingBeeClient(api_key=api)
    response = client.get(
        "https://app.powerbi.com/groups/d72eff1f-51d2-4e98-b093-fddce847145d/reports/e9fde765-f95d-424a-b879-f2f0a89c171f/ReportSection",
        params={
            # 'stealth_proxy': 'True',
            # 'premium_proxy': 'True',
            # 'screenshot_selector': 'section', # Take a full screenshot of the page
            'screenshot': True
        }
    )
    import time
    print("am runing")
    if response.ok:
        time.sleep(6)
        with open("./screenshot.png", "wb") as f:
            f.write(response.content)
            
    else:
        print(response.content)

def login():

    MAIN_URL = "https://app.powerbi.com/reportEmbed?reportId=e9fde765-f95d-424a-b879-f2f0a89c171f&groupId=d72eff1f-51d2-4e98-b093-fddce847145d&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUNFTlRSQUwtQi1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJtb2Rlcm5FbWJlZCI6dHJ1ZSwiYW5ndWxhck9ubHlSZXBvcnRFbWJlZCI6dHJ1ZSwiY2VydGlmaWVkVGVsZW1ldHJ5RW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlLCJza2lwWm9uZVBhdGNoIjp0cnVlfX0=&autoAuth=true&ctid=a23b80fb-03cf-48e7-b7ea-4a9094cff16c"

    client = ScrapingBeeClient(api_key='9IG2PK0A6O7NV7PNGQYOIURT4IMKW0U0TG5WCHJ6BJ48XM18GK95HMA6TBYXF9KGL75TKY1ZOL0GPDVW')
    response = client.post( # Using a POST request instead of GET
        MAIN_URL,
        data= { # Data to send with our POST request
            "email": "yassineboujrada@datastory453.onmicrosoft.com", # Login email
            "passwd": "yassine@2002" # Login password
        }
    )

    if response.ok:
        print('hi')
        with open("./account.html", "wb") as f:
            f.write(response.content)
    else:
        print(response.content)

def login_screen():
    MAIN_URL = "https://app.powerbi.com/groups/d72eff1f-51d2-4e98-b093-fddce847145d/reports/e9fde765-f95d-424a-b879-f2f0a89c171f/ReportSection"

    client = ScrapingBeeClient(api_key='9IG2PK0A6O7NV7PNGQYOIURT4IMKW0U0TG5WCHJ6BJ48XM18GK95HMA6TBYXF9KGL75TKY1ZOL0GPDVW')
    response = client.get(
        MAIN_URL,
        params= {
            "js_scenario": {"instructions":[
                {"fill": [".pbi-text-input", "yassineboujrada@datastory453.onmicrosoft.com"]},
                {"click": "#submitBtn"}, # Click on login
                {"wait": 7000} ,
                {"fill": ["#i0118", "yassine@2002"]}, 
                {"click": "#idSIButton9"}, # Click on login
                {"wait": 5000} ,
                {"click": "#idSIButton9"},
                {"wait": 10000}
                 # Enter registration email
                # {"fill": ["#passwd", "yassine@2002"]}, # Enter password
                # Wait for a second
            ]},
            "screenshot_full_page": True # Take a screenshot
        }
    )
    if response.ok:
        with open("./screenshot.png", "wb") as f:
            f.write(response.content)
    else:
        print(response.content)

def cookies():

    MAIN_URL = "https://app.powerbi.com/reportEmbed?reportId=e9fde765-f95d-424a-b879-f2f0a89c171f&groupId=d72eff1f-51d2-4e98-b093-fddce847145d&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUNFTlRSQUwtQi1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJtb2Rlcm5FbWJlZCI6dHJ1ZSwiYW5ndWxhck9ubHlSZXBvcnRFbWJlZCI6dHJ1ZSwiY2VydGlmaWVkVGVsZW1ldHJ5RW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlLCJza2lwWm9uZVBhdGNoIjp0cnVlfX0=&autoAuth=true&ctid=a23b80fb-03cf-48e7-b7ea-4a9094cff16c"

    client = ScrapingBeeClient(api_key='9IG2PK0A6O7NV7PNGQYOIURT4IMKW0U0TG5WCHJ6BJ48XM18GK95HMA6TBYXF9KGL75TKY1ZOL0GPDVW')
    response = client.get(
    MAIN_URL,
    cookies = {"hldcro4znvvji3cn3smwncyp": "Cookie-Text-Here"},
    params= {
        "screenshot_full_page": True,
    }
    )
    if response.ok:
        with open("./screenshot2.png", "wb") as f:
            f.write(response.content)
    else:
        print(response.content)

import os
from urllib import response
import requests
from bs4 import BeautifulSoup
import time

def get_contenet_of_html():
    reponse = requests.get("https://app.powerbi.com/reportEmbed?reportId=e9fde765-f95d-424a-b879-f2f0a89c171f&groupId=d72eff1f-51d2-4e98-b093-fddce847145d&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUNFTlRSQUwtQi1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJtb2Rlcm5FbWJlZCI6dHJ1ZSwiYW5ndWxhck9ubHlSZXBvcnRFbWJlZCI6dHJ1ZSwiY2VydGlmaWVkVGVsZW1ldHJ5RW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlLCJza2lwWm9uZVBhdGNoIjp0cnVlfX0%3d&autoAuth=true&ctid=a23b80fb-03cf-48e7-b7ea-4a9094cff16c")
    print(reponse.status_code)
    if reponse.ok:
        print("am here")
        soup = BeautifulSoup(reponse.text, "html.parser")#"lxml")
        time.sleep(16)
        return soup.prettify()
    else:
        print(reponse)
        return f'<h1>hhhhh</h1>'

    # get_contenet_of_html()

# with open('./indice33.html','w+') as f:
#     f.write(get_contenet_of_html())
#     print("am here2")

import urllib.request
from pprint import pprint

def lherba_kharya():
    
    with urllib.request.urlopen('https://app.powerbi.com/reportEmbed?reportId=e9fde765-f95d-424a-b879-f2f0a89c171f&groupId=d72eff1f-51d2-4e98-b093-fddce847145d&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUNFTlRSQUwtQi1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJtb2Rlcm5FbWJlZCI6dHJ1ZSwiYW5ndWxhck9ubHlSZXBvcnRFbWJlZCI6dHJ1ZSwiY2VydGlmaWVkVGVsZW1ldHJ5RW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlLCJza2lwWm9uZVBhdGNoIjp0cnVlfX0%3d&autoAuth=true&ctid=a23b80fb-03cf-48e7-b7ea-4a9094cff16c') as response:
        html = response.read()
        pprint(html)

# lherba_kharya()

def khereya2():
    text = urllib.request.urlopen('https://app.powerbi.com/reportEmbed?reportId=e9fde765-f95d-424a-b879-f2f0a89c171f&groupId=d72eff1f-51d2-4e98-b093-fddce847145d&w=2&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLVVTLUNFTlRSQUwtQi1QUklNQVJZLXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0IiwiZW1iZWRGZWF0dXJlcyI6eyJtb2Rlcm5FbWJlZCI6dHJ1ZSwiYW5ndWxhck9ubHlSZXBvcnRFbWJlZCI6dHJ1ZSwiY2VydGlmaWVkVGVsZW1ldHJ5RW1iZWQiOnRydWUsInVzYWdlTWV0cmljc1ZOZXh0Ijp0cnVlLCJza2lwWm9uZVBhdGNoIjp0cnVlfX0%3d&autoAuth=true&ctid=a23b80fb-03cf-48e7-b7ea-4a9094cff16c').read().decode('utf8')
    with open('./test.html','w+') as f:
        f.write(text)

# khereya2()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
def screen_number1():
    chrome_options = Options() #
    chrome_options.add_argument('--headless')

    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/yassine/Downloads/chromedriver_win32/chromedriver.exe")
    # service object
    driver.get("https://app.powerbi.com/groups/d72eff1f-51d2-4e98-b093-fddce847145d/reports/e9fde765-f95d-424a-b879-f2f0a89c171f/ReportSection")
    # driver.get("http://127.0.0.1:3000/dashbord/d72eff1f-51d2-4e98-b093-fddce847145d/e9fde765-f95d-424a-b879-f2f0a89c171f")
    # driver.find_element_by_tag_name("iframe").click()
    time.sleep(6)
    driver.find_element_by_id('email').send_keys("yassineboujrada@datastory453.onmicrosoft.com")
    driver.find_element_by_id('submitBtn').click()

    l=WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    if l:
        time.sleep(6)
        driver.find_element_by_name('passwd').send_keys("yassine@2002")
        driver.find_element_by_id('idSIButton9').click()
        g=WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        if g:
            time.sleep(6)
            driver.find_element_by_id('idSIButton9').click()
            h=WebDriverWait(driver=driver, timeout=10).until(
                lambda x: x.execute_script("return document.readyState === 'complete'")
            )
            if h:
                print('mmmm')
    time.sleep(6)
    driver.get_screenshot_as_file("capture.png")
    driver.close()

chrome_options = Options() #
chrome_options.add_argument('--headless')

chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/yassine/Downloads/chromedriver_win32/chromedriver.exe")
# service object
driver.get("https://app.powerbi.com/groups/d72eff1f-51d2-4e98-b093-fddce847145d/reports/e9fde765-f95d-424a-b879-f2f0a89c171f/ReportSection")
# driver.get("http://127.0.0.1:3000/dashbord/d72eff1f-51d2-4e98-b093-fddce847145d/e9fde765-f95d-424a-b879-f2f0a89c171f")
# driver.find_element_by_tag_name("iframe").click()
time.sleep(6)
driver.find_element_by_id('email').send_keys("yassineboujrada@datastory453.onmicrosoft.com")
driver.find_element_by_id('submitBtn').click()

l=WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
if l:
    time.sleep(6)
    driver.find_element_by_name('passwd').send_keys("yassine@2002")
    driver.find_element_by_id('idSIButton9').click()
    g=WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    if g:
        time.sleep(6)
        driver.find_element_by_id('idSIButton9').click()
        h=WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        if h:
            print('mmmm')
            time.sleep(6)
            driver.get_screenshot_as_file("capture2.png")

driver.close()

