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


def search_about(collection,ref,indice):
    all_data=db.child(collection).child(ref).get()
    for data in all_data.each():
        if data.val()['email'].lower()==indice.lower():
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

        with open(file=f'files/{REPORT_NAME}.pbix', mode='wb+') as power_bi_file:
            power_bi_file.write(my_report_content)

    def export_to_pdf(self,REPORT_ID,REPORT_NAME):
        my_report_content = self.reports_service.export_to_file(
            report_id=REPORT_ID,
            file_format=ExportFileFormats.Pdf
        )
        with open(file=f'files/{REPORT_NAME}.png', mode='wb+') as power_bi_file:
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
                

    def nwita(self):
        url="http://192.168.0.192:3000/dashbord/3e2cfcff-1fc4-4412-af6d-838fe7707cf6/20d3b902-6605-4c1a-bcbf-fd5895e69afe"
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
            
    # def data_report(self):
    #     l,k=[],{}
    #     g=self.show_workspace()
    #     for i in g:
    #         print(i)
    #         report_out=self.reports_service.get_group_reports(
    #                 group_id=str(i[1])
    #             )
    #         print(report_out['value'])
    #         print('######################3\n')

    # def hh(self):
    #     k=[]
    #     for i in self.show_workspace():
    #         report_out=self.reports_service.get_group_reports(
    #                 group_id=str(i[1])
    #             )
    #         k.append([i[0],report_out['value']])
    #     return k

def screen_shot(val,pages_nbr):
    if val:
        l=[]
        for _ in range(pages_nbr):
            path_pic=f'./files/page{_}.png'
            data_recieve=val.split(',')
            myScreenshot = pyautogui.screenshot(region=(int(data_recieve[0]),(int(data_recieve[1])*2),int(data_recieve[2])-220,int(data_recieve[3])-85))
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
    print("\n")
    k=recieve.split(',')
    for i in k:
        print("1",k)
        body = f'{mesg},\npiece jointe:'
        sender,password = 'centre.declaration@gmail.com','bouchaib2021'
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = i#receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        pdfname=path
        # pdfname = path_of_file

        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        
        session = smtplib.SMTP('smtp.gmail.com', 587)

        #enable security
        session.starttls()

        #login with mail_id and password
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