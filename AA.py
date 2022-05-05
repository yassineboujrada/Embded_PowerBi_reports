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

# from flask import Flask
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast
# app = Flask(__name__)
# api = Api(app)

# class Users(Resource):
#     # methods go here
#     pass
    
# class Locations(Resource):
#     # methods go here
#     pass

# class Users(Resource):
#     def get(self):
#         data = pd.read_csv('C:\\Users\\yassine\\Downloads\\coin_Bitcoin.csv')  # read CSV
#         data = data.to_dict()  # convert dataframe to dictionary
#         return {'data': data}, 200  # return data and 200 OK code
    
# api.add_resource(Users, '/users')  # '/users' is our entry point for Users
# api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

# if __name__ == '__main__':
#     app.run()  # run our Flask app

# from flask import Flask, jsonify, request

# from cashman.model.expense import Expense, ExpenseSchema
# from cashman.model.income import Income, IncomeSchema
# from cashman.model.transaction_type import TransactionType

# app = Flask(__name__)

# transactions = [
#   Income('Salary', 5000),
#   Income('Dividends', 200),
#   Expense('pizza', 50),
#   Expense('Rock Concert', 100)
# ]


# @app.route('/incomes')
# def get_incomes():
#   schema = IncomeSchema(many=True)
#   incomes = schema.dump(
#     filter(lambda t: t.type == TransactionType.INCOME, transactions)
#   )
#   return jsonify(incomes.data)


# @app.route('/incomes', methods=['POST'])
# def add_income():
#   income = IncomeSchema().load(request.get_json())
#   transactions.append(income.data)
#   return "", 204


# @app.route('/expenses')
# def get_expenses():
#   schema = ExpenseSchema(many=True)
#   expenses = schema.dump(
#       filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
#   )
#   return jsonify(expenses.data)


# @app.route('/expenses', methods=['POST'])
# def add_expense():
#   expense = ExpenseSchema().load(request.get_json())
#   transactions.append(expense.data)
#   return "", 204


# if __name__ == "__main__":
#     app.run()

# Build the POST parameters
import webbrowser
import os
import msal

def generate_access_token(app_id, scopes):
    # Save Session Token as a token file
    access_token_cache = msal.SerializableTokenCache()

    # read the token file
    if os.path.exists('api_token.json'):
        access_token_cache.deserialize(open("api_token.json", "r").read())

    # assign a SerializableTokenCache object to the client instance
    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

    accounts = client.get_accounts()
    if accounts:
        # load the session
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else:
        # authetnicate your accoutn as usual
        flow = client.initiate_device_flow(scopes=scopes)
        print('user_code: ' + flow['user_code'])
        webbrowser.open('https://microsoft.com/devicelogin')
        token_response = client.acquire_token_by_device_flow(flow)

    with open('api_token.json', 'w') as _f:
        _f.write(access_token_cache.serialize())

    return token_response

if __name__ == '__main__':
    ...

