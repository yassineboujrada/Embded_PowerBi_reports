# from flask import Flask
from flask import Flask, render_template,request, session,redirect
import os
from Power_bi_functions import *
from flask.helpers import url_for,flash
import shutil
from powerbi.client import PowerBiClient

app=Flask(__name__)

UPLOAD_FOLDER = 'static/files/'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CLIENT_POWER_BI = PowerBiClient(
    client_id='5ddb532c-2735-4570-adc2-32eacfd30068',
    client_secret='L6h8Q~Rsq6lSqdrnmHE-oqKxh7khYO~lkvT6tcAX',
    scope=['https://analysis.windows.net/powerbi/api/.default'],
    redirect_uri="https://localhost/redirect",
    credentials='__pycache__/power_bi_state.jsonc'
)

reports_service = CLIENT_POWER_BI.reports()

@app.route("/",methods=["POST","GET"])
def login_in():
    if request.method=="POST":
        session["email_connect"]=request.form.get("email_conect")
        session["password"]=request.form.get("password")
        if session["email_connect"]=="" and \
            session["password"]=="22":
            return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/dashbord",methods=["POST","GET"])
def home():
    # report by id workspace
    report_out=reports_service.get_group_reports(
            group_id='3e2cfcff-1fc4-4412-af6d-838fe7707cf6'
        )
    ## data from ther workspace
    data_workspace=get_workspace_informations()
    ## data from my workspace
    report_in_workspace=reports_service.get_reports()#reports_information()
    return render_template("Show_Dashbord.html",data_workspace=data_workspace['value'],report_in_workspace=report_in_workspace['value'],report_out=report_out['value'])

if "__main__"==__name__:
    app.run(debug=True,port=4000)






# @app.route("/",methods=["POST","GET"])
# find_file_in_all_drives( 'C\\.doc' )
    # if request.method=="POST":
    #     session["recieve"]=request.form.get("recieve_adr")
    #     session["subject"]=request.form.get("subject")
    #     session["msg"]=request.form.get("msg")
    #     return redirect(url_for("file_select"))
    # return render_template("mail.html")

# @app.route("/send_mail",methods=["POST","GET"])
# def home():
#     find_file_in_all_drives( 'C\\.doc' )
#     if request.method=="POST":
#         session["recieve"]=request.form.get("recieve_adr")
#         session["subject"]=request.form.get("subject")
#         session["msg"]=request.form.get("msg")
#         return redirect(url_for("file_select"))
#     return render_template("mail.html")

# @app.route("/file_select",methods=["POST","GET"])
# def file_select():
#     all_files=serch_file_path(".pbix")
#     if request.method=="POST":
#         session["file_name"]=request.form.get("name_file")
#         shutil.copy(session["file_name"], UPLOAD_FOLDER)
#         new_path='\\static\\'+str(session["file_name"].split("\\")[-1])
#         b=new_path.split("\\")[-1]
#         c=b.split(".pbix")
#         c=str(c[0])+".pdf"
#         take_screens_from_pbix(b)
#         if session["file_name"] != None:
#             return redirect(url_for('time_selection_time'))
#         else:
#             pass

#     return render_template("file_show.html",files=all_files)

# @app.route("/define_time",methods=["POST","GET"])
# def time_selection_time():
#     if request.method=="POST":
#         session["send_timing"]=request.form.get("time_to_send")
#         session["which_day"]=request.form.get("value_for_day")
#         session["every_"]=request.form.get("period_day")
#         print(session["file_name"])
#         if send_pdf_file(session["msg"],session["recieve"].split(","),session["subject"]):
#             return redirect(url_for('home'))
#         else:
#             pass

#     return render_template("time.html")

