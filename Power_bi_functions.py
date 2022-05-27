import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from webbrowser import Chrome
from xml.etree.ElementTree import Element
import pyautogui
import win32gui
import time 
from fpdf import FPDF
from PIL import Image
import glob

import msal
import requests
import json
from pprint import pprint
from powerbi.client import PowerBiClient
from powerbi.enums import ExportFileFormats
from scrapingbee import ScrapingBeeClient
import img2pdf
import schedule
from pyrebase import pyrebase
import bcrypt

CONFIG_DB={
    'apiKey': "AIzaSyCPeLozDHk6Sn2_KGlqZA_YWdrQQBTNNnc",
    'authDomain': "db-awelk.firebaseapp.com",
    'databaseURL': "https://db-awelk-default-rtdb.firebaseio.com",
    'projectId': "db-awelk",
    'storageBucket': "db-awelk.appspot.com",
    'messagingSenderId': "37231178359",
    'appId': "1:37231178359:web:b4e5fae6e61555dce7cc72",
    'measurementId': "G-VX1NF3YBG7"
}
firebase=pyrebase.initialize_app(CONFIG_DB)

db=firebase.database()


def search_about(collection,ref,indice,key):
    all_data=db.child(collection).child(ref).get()
    for data in all_data.each():
        if data.val()['email'].lower()==indice.lower():
            
            data.val()['password']=bcrypt.hashpw(bytes(data.val()['password'], 'utf-8'), key)
            return data.val()
        else:
            return None

def all_data(collection,child_ref):
    keys,values=[],[]
    data=db.child(collection).get()
    for d in data.each():
        for key in d.val():
            keys.append(key)
            values.append(d.val()[key])
    return keys,values

# --------------------------------------------------
# Set local variables
# --------------------------------------------------

class Authentification_for_PowerBI:
    def __init__(self):
        self.CLIENT_ID='5ddb532c-2735-4570-adc2-32eacfd30068'
        self.username="yassineboujrada@datastory453.onmicrosoft.com"
        self.password="yassine@2002"
        self.TENANT_ID='a23b80fb-03cf-48e7-b7ea-4a9094cff16c'
        self.AUTHORITY_URL = 'https://login.microsoftonline.com/'+self.TENANT_ID
        self.SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
        self.URL_TO_GET_GROUPS = 'https://api.powerbi.com/v1.0/myorg/groups'

        self.CLIENT_POWER_BI = PowerBiClient(
            client_id='5ddb532c-2735-4570-adc2-32eacfd30068',
            client_secret='L6h8Q~Rsq6lSqdrnmHE-oqKxh7khYO~lkvT6tcAX',
            scope=['https://analysis.windows.net/powerbi/api/.default'],
            redirect_uri="https://localhost/redirect",
            credentials='__pycache__/power_bi_state.jsonc'
        )

        self.reports_service = self.CLIENT_POWER_BI.reports()
        # self.my_work_space=self.reports_service.get_reports()
        # self.CLIENT_POWER_BI
        # pprint(template_apps_service = self.CLIENT_POWER_BI.template_apps())
    def get_my_workspace(self):
        return self.reports_service.get_reports()

    def get_pages_number(self,WORK_ID,REPORT_ID):
        return self.reports_service.get_group_pages(
                group_id=WORK_ID,
                report_id=REPORT_ID
            )

    def get_tenant(self):
        return str(self.TENANT_ID)

    def download_pbi(self,GROUP_ID,REPORT_ID,REPORT_NAME):
        my_report_content = self.reports_service.export_group_report(
            group_id=GROUP_ID,
            report_id=REPORT_ID
        )

        with open(file=f'{REPORT_NAME}.pbix', mode='wb+') as power_bi_file:
            power_bi_file.write(my_report_content)

    def export_to_pdf(self,REPORT_ID,REPORT_NAME):
        my_report_content = self.reports_service.export_to_file(
            report_id=REPORT_ID,
            file_format=ExportFileFormats.Csv
        )
        with open(file=f'{REPORT_NAME}.csv', mode='wb+') as power_bi_file:
            power_bi_file.write(my_report_content)

    def get_workspace_informations(self):
        client_data = msal.PublicClientApplication(self.CLIENT_ID, authority=self.AUTHORITY_URL)
        result = client_data.acquire_token_by_username_password(username=self.username,password=self.password,scopes=self.SCOPE)
        if 'access_token' in result:
            access_token = result['access_token']
            header = {'Content-Type':'application/json','Authorization': f'Bearer {access_token}'}
            api_out = requests.get(url=self.URL_TO_GET_GROUPS, headers=header)
            return api_out.json()
        else:
            print(result.get("error"))
            print(result.get("error_description"))

    def show_workspace(self):
        work_space=[]
        for i in self.get_workspace_informations()['value']:
            work_space.append([i['name'],i['id']])
        return work_space

    ##  return reports id in each workspace
    def get_report_from_workspace(self,id_work_space):
        report_out=self.reports_service.get_group_reports(
            group_id=str(id_work_space)
        )
        return report_out
                
    def grab_my_report(self,REPORT_ID):
        return self.reports_service.get_report(report_id=str(REPORT_ID))

    def nwita(self):
        url="http://192.168.1.46:3000/"
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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def screen_not_kidding(url_info):
    chrome_options = Options() #
    chrome_options.add_argument('--headless')

    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(options=chrome_options, executable_path="C:/Users/yassine/Downloads/chromedriver_win32/chromedriver.exe")
    # service object
    driver.get(url_info)
    # driver.get("https://app.powerbi.com/groups/d72eff1f-51d2-4e98-b093-fddce847145d/reports/e9fde765-f95d-424a-b879-f2f0a89c171f/ReportSection")
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
                driver.get_screenshot_as_file("page0.png")

    driver.close()
            
# work='d72eff1f-51d2-4e98-b093-fddce847145d'
# repo='c4cabace-7684-47e3-b2f3-9e183ae3322e'

# c=Authentification_for_PowerBI().export_to_pdf(repo,'nwita')
# d=Authentification_for_PowerBI().download_pbi(work,repo,'nwita')

# my_report_content = Authentification_for_PowerBI().reports_service.export_to_file(
#     report_id='c999d266-0291-40ec-aa0f-df0dbe962771',
#     file_format=ExportFileFormats.Pdf
# )

# pprint(my_report_content)

# with open(file='my_group_report_export.pdf', mode='wb+') as power_bi_file:
#     power_bi_file.write(my_report_content)

def screen_shot(val,pages_nbr):
    if val:
        l=[]
        for _ in range(pages_nbr):
            path_pic=f'./files/page{_}.png'
            data_recieve=val.split(',')
            myScreenshot = pyautogui.screenshot(region=(int(data_recieve[0]),(int(data_recieve[1])*2)-30,int(data_recieve[2])-220,int(data_recieve[3])-130))
            myScreenshot.save(path_pic)
            data_recieve=""
            l.append(path_pic)
        return l
    else:
        raise ValueError('hhhhh')

def transform_file_to_pdf(name_folder,pict_list):
    pdf_name_path="./files/"+name_folder+".pdf"
    with open(pdf_name_path,"wb") as f:
        f.write(img2pdf.convert(pict_list))
    return pdf_name_path

############################################################  envoyer pbi report ou pdf a une email 
def send_pdf_file(mesg,recieve,subject,path):
    k=recieve.split(',')
    for i in k:
        print("1",k)
        body = f'{mesg},\npiece jointe:'
        sender,password = 'centre.declaration@gmail.com','bouchaib2021'
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = i
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        pdfname=path

        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        
        session = smtplib.SMTP('smtp.gmail.com', 587)

        session.starttls()

        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, i, text)
        session.quit()
        print('Mail Sent')
    return True

def main(mesg,recieve,subject,path):
    schedule.every(10).seconds.do(send_pdf_file,mesg,recieve,subject,path)

    while True:
        schedule.run_pending()
        time.sleep(1)

# def ancienne_data():
#     _,d=all_data("send_email_informations","-N2hHzKSrK4id3pKLCgF")
#     l=[]
#     for i in d:
#         # print(i)
#         email=i['emails']
#         path_pd=i['file_path']
#         period=i['perids']
#         subj=i['subject']
#         duree=i['time']
#         l.append([email,path_pd,period,subj,duree])
#     return l


# def take_screens_from_pbix(file_name):
#     print("hhhhh", file_name)
#     b="".join(file_name.split("/static/files/"))
#     file_name_derictory=f'{os.path.abspath(os.getcwd())}\\static\\files\\{b}'
#     os.startfile(f'{file_name_derictory}')
#     time.sleep(40)
#     refresh_report()
#     time.sleep(35)
#     screenshot(f'{"".join(b.split(".pbix"))} - Power BI Desktop')
#     screen_to_pdf()

# def screenshot(window_title=None):
#     if window_title:
#         hwnd = win32gui.FindWindow(None, window_title)

#         if hwnd:
#             win32gui.SetForegroundWindow(hwnd)
#             x, y, x1, y1 = win32gui.GetClientRect(hwnd)
#             x, y = win32gui.ClientToScreen(hwnd, (x, y))
#             x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
#             im = pyautogui.screenshot(region=(60,200,1510 ,750))
#             im.save(r'static/test1.png')
#             os.system("taskkill /f /im PBIDesktop.exe")
#         else:
#             print('Window not found!')
#     else:
#         im = pyautogui.screenshot()
#         os.system("taskkill /f /im PBIDesktop.exe")
#         return im


# def serch_file_path(file_ext):
#     l,b=[],[]
#     for root, dirs, files in os.walk(r'C:\\Users\\yassine\\Documents\\power bi tutorial'):
#         for name in files:
#             if name.endswith(file_ext) :
#                 l.append(os.path.abspath(os.path.join(root, name)))

#     for i in l:
#         b.append([i,i.split("\\")[-1]])

#     return b