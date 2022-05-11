import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
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



 # --------------------------------------------------
# Set local variables
# --------------------------------------------------
CLIENT_ID='5ddb532c-2735-4570-adc2-32eacfd30068'
username="yassineboujrada@datastory453.onmicrosoft.com"
password="yassine@2002"

AUTHORITY_URL = 'https://login.microsoftonline.com/a23b80fb-03cf-48e7-b7ea-4a9094cff16c'
SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
URL_TO_GET_GROUPS = 'https://api.powerbi.com/v1.0/myorg/groups'

# CLIENT_POWER_BI = PowerBiClient(
#     client_id='5ddb532c-2735-4570-adc2-32eacfd30068',
#     client_secret='L6h8Q~Rsq6lSqdrnmHE-oqKxh7khYO~lkvT6tcAX',
#     scope=['https://analysis.windows.net/powerbi/api/.default'],
#     redirect_uri="https://localhost/redirect",
#     credentials='__pycache__/power_bi_state.jsonc'
# )

def get_report_informations():
    client_data = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY_URL)
    result = client_data.acquire_token_by_username_password(username=username,password=password,scopes=SCOPE)
    if 'access_token' in result:
        access_token = result['access_token']
        header = {'Content-Type':'application/json','Authorization': f'Bearer {access_token}'}
        api_out = requests.get(url=URL_TO_GET_GROUPS, headers=header)
        return api_out.json()
    else:
        # return 
        print(result.get("error"))
        print(result.get("error_description"))


# def reports_information():
#     reports_service = CLIENT_POWER_BI.reports()
#     pprint(
#         reports_service.get_group_reports(
#             group_id='3e2cfcff-1fc4-4412-af6d-838fe7707cf6'
#         )
#     )
#     # # Grab all the reports in our workspace.

#     return reports_service.get_reports()
























############################################################  envoyer pbi report ou pdf a une email 
def send_pdf_file(mesg,recieve,subject):
    for i in recieve:
        body = f'{mesg},\npiece jointe:'
        sender,password = 'centre.declaration@gmail.com','bouchaib2021'
        
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = i#receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        
        pdfname=f'{os.path.abspath(os.getcwd())}\\static\\file.pdf'
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


def refresh_report():
    time.sleep(1.5)
    x_median_position,y_median_position=(731+774)/2 , (95+169)/2
    pyautogui.moveTo(x_median_position,y_median_position)
    pyautogui.click()

def take_screens_from_pbix(file_name):
    print("hhhhh", file_name)
    b="".join(file_name.split("/static/files/"))
    file_name_derictory=f'{os.path.abspath(os.getcwd())}\\static\\files\\{b}'
    os.startfile(f'{file_name_derictory}')
    time.sleep(40)
    refresh_report()
    time.sleep(35)
    screenshot(f'{"".join(b.split(".pbix"))} - Power BI Desktop')
    screen_to_pdf()

def screenshot(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)

        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            x, y, x1, y1 = win32gui.GetClientRect(hwnd)
            x, y = win32gui.ClientToScreen(hwnd, (x, y))
            x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
            im = pyautogui.screenshot(region=(60,200,1510 ,750))
            im.save(r'static/test1.png')
            os.system("taskkill /f /im PBIDesktop.exe")
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        os.system("taskkill /f /im PBIDesktop.exe")
        return im

def screen_to_pdf():
    image_directory=f'{os.path.abspath(os.getcwd())}\\static\\files\\'
    extensions = ('test1.jpg','test1.png')
    pdf = FPDF()
    imagelist=[]
    for ext in extensions:
        imagelist.extend(glob.glob(os.path.join(image_directory,ext)))

    for imageFile in imagelist:
        cover = Image.open(imageFile)
        width, height = cover.size

        # convert pixel in mm with 1px=0.264583 mm
        width, height = float(width * 0.264583), float(height * 0.264583)

        # given we are working with A4 format size 
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

        # get page orientation from image size 
        orientation = 'P' if width < height else 'L'

        #  make sure image size is not greater than the pdf format size
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

        pdf.add_page(orientation=orientation)

        pdf.image(imageFile, 0, 0, width, height)
    pdf.output(image_directory + "file.pdf", "F")

def serch_file_path(file_ext):
    l,b=[],[]
    for root, dirs, files in os.walk(r'C:\\Users\\yassine\\Documents\\power bi tutorial'):
        for name in files:
            if name.endswith(file_ext) :
                l.append(os.path.abspath(os.path.join(root, name)))

    for i in l:
        b.append([i,i.split("\\")[-1]])

    return b


# import schedule

# def job():
#     print("I'm working...")

# schedule.every(1).minutes.do(function)

##########  RUN IN SPECIFIC TIME AN DAY  #############
# schedule.every().day.at("13:48").do(function)

# ##########  RUN IN SPECIFIC TIME AN MONTH  #############
# schedule.every(30).day.at("13:48").do(function)

# ##########  RUN IN SPECIFIC TIME AN YEAR  #############
# schedule.every(365).day.at("13:48").do(function)

# while True:
#     schedule.run_pending()
#     time.sleep(1) 

# import re
# import win32api

# def find_file(root_folder, rex=".pdf"):
#     for root,dirs,files in os.walk(root_folder):
#         for f in files:
#             result = rex.search(f)
#             if result:
#                 print("test\t",os.path.join(root, f))
#                 break # if you want to find only one

# def find_file_in_all_drives(file_name):
#     #create a regular expression for the file
#     rex = re.compile(file_name)
#     for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
#         find_file( drive, rex )