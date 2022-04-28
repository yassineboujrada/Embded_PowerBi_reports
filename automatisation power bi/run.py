# from django.shortcuts import redirect
from flask import Flask, render_template,request, session,redirect
import os
from fct_of_PowerBI import *
from flask.helpers import url_for,flash
import shutil

app=Flask(__name__)

UPLOAD_FOLDER = 'static/'

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["POST","GET"])
def login_in():
    if request.method=="POST":
        session["email_connect"]=request.form.get("email_conect")
        session["password"]=request.form.get("password")
        if session["email_connect"]=="balabala@gmail.com" and \
            session["password"]=="S9fHNn9H3jsH@eh":
            return redirect(url_for("home"))
        print(session["email_connect"],session["password"])
    return render_template("login.html")

@app.route("/send_mail",methods=["POST","GET"])
def home():
    if request.method=="POST":
        session["recieve"]=request.form.get("recieve_adr")
        session["subject"]=request.form.get("subject")
        session["msg"]=request.form.get("msg")

        print("11111",session["recieve"],session["subject"],\
        session["msg"])
        return redirect(url_for("file_select"))
    return render_template("mail.html")

@app.route("/file_select",methods=["POST","GET"])
def file_select():
    all_files=serch_file_path(".pbix")
    if request.method=="POST":
        session["file_name"]=request.form.get("name_file")
        print("bbb 1: ",session["file_name"])
        shutil.copy(session["file_name"], UPLOAD_FOLDER)
        print(session["file_name"])
        new_path='\\static\\'+str(session["file_name"].split("\\")[-1])
        b=new_path.split("\\")[-1]
        c=b.split(".pbix")
        c=str(c[0])+".pdf"
        take_screens_from_pbix(b)

        if session["file_name"] != None:
            return redirect(url_for('time_selection_time'))
        else:
            pass

    return render_template("file_show.html",files=all_files)

@app.route("/define_time",methods=["POST","GET"])
def time_selection_time():
    if request.method=="POST":
        session["send_timing"]=request.form.get("time_to_send")
        session["which_day"]=request.form.get("value_for_day")
        session["every_"]=request.form.get("period_day")
        print(session["file_name"])
        # send_pdf_file(new_path,session["msg"],session["recieve"],session["subject"])
        if send_pdf_file(session["msg"],session["recieve"],session["subject"]):

            return redirect(url_for('home'))
        else:
            pass

    return render_template("time.html")


if "__main__"==__name__:
    app.run(debug=True)