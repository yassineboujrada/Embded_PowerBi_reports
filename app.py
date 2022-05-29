from datetime import datetime as d
from flask import Flask, render_template,request, session,redirect,jsonify
from Power_bi_functions import *
from flask.helpers import url_for,flash
from threading import Thread
import bcrypt


app=Flask(__name__)
UPLOAD_FOLDER = 'static/files/'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/",methods=["POST","GET"])
def login_in():
    if request.method=="POST":
        salt = bcrypt.gensalt()
        session["email_connect"]=request.form.get("email_conect")
        passwd =bytes(request.form.get("password"), 'utf-8')
        
        hashed = bcrypt.hashpw(passwd, salt)
        res=search_about("User","-N2hHzN_G51X1PurUwyB",session["email_connect"],salt)
        if res !=None:
            if hashed==res['password']:
                flash("vous êtes connecté avec succès","success")
                return redirect(url_for('table_period'))
            else:
                flash("mot de passe incorrecte","warning")
                return redirect(url_for('login_in'))
        else:
            flash("gmail ou mot de passe sont incorrecte","warning")
            return redirect(url_for('login_in'))
    return render_template("login.html")


@app.route("/my_table_of_period",methods=["POST","GET"])
def table_period():
    _,period_data=all_data("send_email_informations","-N2hHzKSrK4id3pKLCgF")
    return render_template('table_preriod.html',period_data=period_data)

@app.route("/dashbord",methods=["POST","GET"])
def dashbord():
    return render_template("Dashbord.html",d=Authentification_for_PowerBI().show_workspace())

@app.route('/dashbord/me')
def my_work():
    c=Authentification_for_PowerBI().get_my_workspace()['value']
    session['report_embded']=c
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
    if work_space == 'me':
        print('hi')
        j=Authentification_for_PowerBI().grab_my_report(report_id)
        j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
    else:
        session['report_embded']=Authentification_for_PowerBI().get_report_from_workspace(work_id)['value']
        i=session['report_embded']
        print(work_space)
        for k in i:
            if k['id']==str(report_id):
                j=k
                j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
                j['webUrl']+='/ReportSection'
            else: 
                pass
    
    pprint(Authentification_for_PowerBI().get_report_from_workspace(work_id))
    if request.method=='GET':
        return render_template('Show_report.html',work_space=work_space,report_id=report_id,j=j)

    val = request.json.get("c_check")
    
    if val:
        img_path=screen_matidhekech(j['webUrl'])
        path_of_pdf=transform_file_to_pdf(j['name'],img_path)
        session["path_pdf"]=path_of_pdf
        time.sleep(2)
        return jsonify({"data": {"val": "wait some minutes to export you're file","fun":"hhhhhhhhhh"}})
    

@app.route("/send_mail",methods=["POST","GET"])
def send_mail():
    print("\t",session["path_pdf"])
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
        if session["send_timing"]=="":
            session["send_timing"]=d.now().strftime("%H:%M")
        else:
            pass
        
        if send_pdf_file(session["msg"],session["recieve"],session["subject"],session["path_pdf"]):
            return redirect(url_for('dashbord'))
        
    return render_template("time.html")

@app.route('/send_mail/file_sending',methods=["POST","GET"])
def file_pdf_send():
    return render_template('file.html')




if "__main__"==__name__:
    c=ancienne_data()
    t = Thread(target=main, args=(c,))
    t.start()
    app.run(debug=True,port=3000)#,host='192.168.1.46')