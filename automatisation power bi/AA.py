# from docx2pdf import convert

# convert("test2.pbix")
# convert("test2.pbix", "output.pdf")
# convert("my_docx_folder/")

####################################

# import sys
# import subprocess
# import re


# def convert_to(folder, source, timeout=None):
#     args = [libreoffice_exec(), '--headless', '--convert-to', 'pdf', '--outdir', folder, source]

#     process = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
#     filename = re.search('-> (.*?) using filter', process.stdout.decode())

#     return filename.group(1)


# def libreoffice_exec():
#     # TODO: Provide support for more platforms
#     if sys.platform == 'darwin':
#         return '/Applications/LibreOffice.app/Contents/MacOS/soffice'
#     return 'libreoffice'

# result = convert_to('final-stage-project',  'test2.pbix', timeout=15)

# import os
# import win32com.client

# wdFormatPDF = 17
# a='Outlook.Application'

# for root, dirs, files in os.walk(r'C:\\Users\\yassine\\Documents\\final-stage-project'):
#     for f in files:

#         if  f.endswith(".doc")  or f.endswith(".pbit") or f.endswith(".pbix"):
#             try:
#                 print(f)
#                 in_file=os.path.join(root,f)
#                 word = win32com.client.Dispatch(a)
#                 word.Visible = False
#                 doc = word.Documents.Open(in_file)
#                 doc.SaveAs(os.path.join(root,f[:-4]), FileFormat=wdFormatPDF)
#                 doc.Close()
#                 word.Quit()
#                 word.Visible = True
#                 print ('done')
#                 os.remove(os.path.join(root,f))
#                 pass

#             except:
#                 print('could not open')
#                 # os.remove(os.path.join(root,f))

#         elif f.endswith(".docx") or f.endswith(".dotm") or f.endswith(".docm") or f.endswith(".pbix"):
#             try:
#                 print(f)
#                 in_file=os.path.join(root,f)
#                 word = win32com.client.Dispatch(a)
#                 word.Visible = False
#                 doc = word.Documents.Open(in_file)
#                 doc.SaveAs(os.path.join(root,f[:-5]), FileFormat=wdFormatPDF)
#                 doc.Close()
#                 word.Quit()
#                 word.Visible = True
#                 print ('done')
#                 os.remove(os.path.join(root,f))
#                 pass
#             except:
#                 print('could not open')
#                 # os.remove(os.path.join(root,f))
#         else:
#             pass

# from datetime import datetime
# import os
# import pyautogui
# import win32gui
# import time

# def take_screens_from_pbix(file_name):
#     os.startfile(f'{file_name}')
#     a=f'{str(file_name)} - Power BI Desktop'
#     print(datetime.now())
#     print(2)
#     time.sleep(40)
#     print(datetime.now())
#     screenshot("test2 - Power BI Desktop")
#         # print(1)
#         # print(datetime.now())
#         # os.system("taskkill /f /im PBIDesktop.exe")
#         # return

# def screenshot(window_title=None):
#     if window_title:
#         hwnd = win32gui.FindWindow(None, window_title)

#         if hwnd:
#             win32gui.SetForegroundWindow(hwnd)
#             x, y, x1, y1 = win32gui.GetClientRect(hwnd)
#             x, y = win32gui.ClientToScreen(hwnd, (x, y))
#             x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
#             im = pyautogui.screenshot(region=(x, y, x1, y1))
#             im.save(r'test1.png')
#             os.system("taskkill /f /im PBIDesktop.exe")
#         else:
#             print('Window not found!')
#     else:
#         im = pyautogui.screenshot()
#         print(5)
#         os.system("taskkill /f /im PBIDesktop.exe")
#         return im

# take_screens_from_pbix("test2.pbix")


# while True:
#     screenshot("test2 - Power BI Desktop")
#     time.sleep(4)

    # if im:
    #     im.show()
# os.startfile("test2.pbix")
# os.close()

# from win32com.client import GetObject 
# WMI = GetObject('winmgmts:')

# # print(WMI.ExecQuery('select Name from Win32_Process'))
# for process in WMI.ExecQuery('select * from Win32_Process where Name="Microsoft Power BI Desktop"'): 
# #the date format is something like this 20200613144903.166769+480 create_dt, *_ = process.CreationDate'.split('.') 
# # diff = datetime.now() - datetime.strptime(create_dt,'%Y%m%d%H%M%S')
#     print("Terminating PID:", process.ProcessId) 
#     os.system("taskkill /pid "+str(process.ProcessId))


