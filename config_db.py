# from pyrebase import pyrebase

# config_db={
#     'apiKey': "AIzaSyCPeLozDHk6Sn2_KGlqZA_YWdrQQBTNNnc",
#     'authDomain': "db-awelk.firebaseapp.com",
#     'databaseURL': "https://db-awelk-default-rtdb.firebaseio.com",
#     'projectId': "db-awelk",
#     'storageBucket': "db-awelk.appspot.com",
#     'messagingSenderId': "37231178359",
#     'appId': "1:37231178359:web:b4e5fae6e61555dce7cc72",
#     'measurementId': "G-VX1NF3YBG7"
# }

# firebase=pyrebase.initialize_app(config_db)

# db=firebase.database()
# db.child('names').push({'name':'khalid'})




# import cx_Oracle
import os
# import platform

# if platform.system() == "Darwin":
#     cx_Oracle.init_oracle_client(lib_dir=os.environ.get("Documents")+"\\last-projects\\Embded_PowerBi_reports\\Wallet_NFS315")
# elif platform.system() == "Windows":
#     cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_14")

# username = os.environ.get("PYTHON_USERNAME")
# password = os.environ.get("PYTHON_PASSWORD")
# connect_string = os.environ.get("PYTHON_CONNECTSTRING")

# connection = cx_Oracle.connect(user=username, password=password, dsn=connect_string)

# with connection.cursor() as cursor:
#     try:

#         sql = """select systimestamp from dual"""
#         for r in cursor.execute(sql):
#             print(r)

#     except cx_Oracle.Error as e:
#         error, = e.args
#         print(error.message)
#         print(sql)
#         if (error.offset):
#             print('^'.rjust(error.offset+1, ' '))

print(os.environ.get("Users"))#+"\\last-projects\\Embded_PowerBi_reports\\Wallet_NFS315")