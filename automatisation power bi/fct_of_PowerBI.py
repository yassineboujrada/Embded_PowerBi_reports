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
