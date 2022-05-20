# from flask import Flask
from flask import Flask, render_template,request, session,redirect,jsonify,make_response
import os
from Power_bi_functions import *
from flask.helpers import url_for,flash
import shutil


# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration

# sentry_sdk.init(
#     dsn="http://<key>@127.0.0.1:3000/<project>dashbord/<string:work_id>/<string:report_id>",
#     integrations=[FlaskIntegration()],
#     traces_sample_rate=1.0,
#     send_default_pii=True
# )

app=Flask(__name__)

UPLOAD_FOLDER = 'static/files/'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["POST","GET"])
def login_in():
    if request.method=="POST":
        session["email_connect"]=request.form.get("email_conect")
        session["password"]=request.form.get("password")
        if session["email_connect"]=="" and \
            session["password"]=="22":
            return redirect(url_for('table_period'))

    return render_template("login.html")

@app.route("/my_table_of_period",methods=["POST","GET"])
def table_period():
    return render_template('table_preriod.html')

@app.route("/dashbord",methods=["POST","GET"])
def dashbord():
    return render_template("Dashbord.html",d=Authentification_for_PowerBI().show_workspace())

@app.route('/dashbord/me')
def my_work():
    c=Authentification_for_PowerBI().get_my_workspace()['value']
    session['report_embded']=c
    print(c)
    return render_template('report.html',reports=c,workspace_id='me')

@app.route('/dashbord/<string:work_id>')
def workspace(work_id):
    workspace_id=work_id
    reports=Authentification_for_PowerBI().get_report_from_workspace(workspace_id)['value']
    session['report_embded']=reports
    return render_template('report.html',reports=reports,workspace_id=workspace_id)  

@app.route('/dashbord/<string:work_id>/<string:report_id>',methods=["POST","GET"])
def report_show(work_id,report_id):
    work_space=work_id
    report_id=report_id
    i=session['report_embded']
    print(work_space)
    screen_shot(1)
    for k in i:
        if k['id']==str(report_id):
            j=k
            j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()#'a23b80fb-03cf-48e7-b7ea-4a9094cff16c'
            # Authentification_for_PowerBI().download_pbi(work_space,report_id,j['name'])
            # session.pop('report_embded',None)
            session['report_name_for_send']=j['id']+"||"+j['name']
            
        else: 
            pass

    if request.method=='GET':
        # screen_shot(1)
        # Authentification_for_PowerBI().export_to_pdf('6341d428-a600-4ee6-8185-5ae8616fd093','test')
        return render_template('Show_report.html',work_space=work_space,report_id=report_id,j=j)

    val = request.json.get("c_check")
    print('test',val)
    print(request.json.get('data'))
    if val=='1':
        screen_shot(1)
        print('hi')

        # return redirect(url_for('send_mail'))

        return jsonify({"data": {"val": 'plz wait to export you file'}})
    
    # return render_template('Show_report.html',work_space=work_space,report_id=report_id,j=j)

@app.route("/send_mail",methods=["POST","GET"])
def send_mail():
    print(session['report_name_for_send'])
    if request.method=="POST":
        session["recieve"]=request.form.get("recieve_adr")
        session["subject"]=request.form.get("subject")
        session["msg"]=request.form.get("msg")
        print(session["recieve"],session["subject"])
        return redirect(url_for("time_selection_time"))

    return render_template("mail.html")

@app.route("/send_mail/define_time",methods=["POST","GET"])
def time_selection_time():
    if request.method=="POST":
        session["send_timing"]=request.form.get("time_to_send")
        session["which_day"]=request.form.get("value_for_day")
        session["every_"]=request.form.get("period_day")

        print(session["send_timing"],"\n",session["which_day"],session["every_"])
        
    return render_template("time.html")

if "__main__"==__name__:
    app.run(debug=True,port=3000)#,host='192.168.1.85')







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



