# from flask import Flask
from flask import Flask, render_template,request, session,redirect,jsonify,make_response
import os
from Power_bi_functions import *
from flask.helpers import url_for,flash
import shutil

app=Flask(__name__)

UPLOAD_FOLDER = 'static/files/'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["POST","GET"])
def login_in():
    X=Authentification_for_PowerBI().show_workspace()
    if request.method=="POST":
        session["email_connect"]=request.form.get("email_conect")
        session["password"]=request.form.get("password")
        if session["email_connect"]=="" and \
            session["password"]=="22":
            return render_template("Show_Dashbord.html",d=X)

    return render_template("login.html")

@app.route("/dashbord",methods=["POST","GET"])
def home():
    X=Authentification_for_PowerBI().show_workspace()
    # data_workspace=Authentification_for_PowerBI().show_workspace()
    # h=Authentification_for_PowerBI().hh()
    # if request.method == "GET":
    #     return render_template("Show_Dashbord.html",d=data_workspace,h=h)

    # val = request.json.get("c_check")
    # print(val)
    # return jsonify({"data": {"val": val}})
    
    return render_template("Show_Dashbord.html",d=X)#,data_workspace=data_workspace,report_in_workspace=report_in_workspace)

@app.route('/dashbord/<string:page_id>')
def page(page_id):
    X=Authentification_for_PowerBI().show_workspace()
    h=Authentification_for_PowerBI().get_report_from_workspace(page_id)['value']
    pprint(h)
    return render_template("Show_Dashbord.html",d=X,h=h)

# from flask_restful import Api, Resource
# api =   Api(app)
  
# class returnjson(Resource):
#     def get(self):
#         data={
#             "Modules": 15, 
#             "Subject": "Data Structures and Algorithms"
#         }
#         return data
  
# api.add_resource(returnjson,'/returnjson')

if "__main__"==__name__:
    app.run(debug=True,port=3000)






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

