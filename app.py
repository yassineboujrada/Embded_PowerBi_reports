from datetime import datetime as d
from random import randint
from secrets import randbits
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
                flash("MOT DE PASSE INCORRECTE","warning")
                return redirect(url_for('login_in'))
        else:
            flash("GMAIL OU MOT DE PASSE SONT INCORRECTE","warning")
            return redirect(url_for('login_in'))
    return render_template("login.html")

@app.route('/mot_de_pass',methods=["POST","GET"])
def forget():
    if request.method=="POST":
        session['email_verif']=request.form.get("email_verif")
        gg=search_about("User","-N2hHzN_G51X1PurUwyB",session['email_verif'],"")
        print(gg)
        print(request.form.get("email_verif"))
        if gg:
            global rand
            rand=str(randint(100000,999999))
            verif_msg(rand,session['email_verif'])
            return redirect(url_for('verif_code'))
        else:
            flash("YOUR EMAIL IS NOT REGISTERED IN DATABASE","warning")
            return redirect(url_for('forget'))

    return render_template('email_v.html')

@app.route('/mot_de_pass/code_auth',methods=["POST","GET"])
def verif_code():
    if request.method=="POST":
        if rand==request.form.get("code"):
            return redirect(url_for('new_pass'))
        else:
            flash("INCORRECT CODE","warning")
            return redirect(url_for('forget'))
    return render_template('pass.html')

@app.route('/mot_de_pass_change',methods=["POST","GET"])
def new_pass():
    if request.method=="POST":
        if request.form.get("conf_pass")==request.form.get("new_pass"):
            change(session['email_verif'],request.form.get("new_pass"))
            # return redirect(url_for('login_in'))
        else:
            flash("DIFFERENT PASSWORD","warning")
            return redirect(url_for('new_pass'))
    return render_template('change.html')


@app.route("/my_table_of_period",methods=["POST","GET"])
def table_period():

    _,period_data=all_data("send_email_informations","-N2hHzKSrK4id3pKLCgF")
    
    print('2',period_data)
    # drop()
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
        for k in i:
            if k['id']==str(report_id):
                j=k
                j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
                j['webUrl']+='/ReportSection'
            else: 
                pass
    
    if request.method=='GET':
        return render_template('Show_report.html',work_space=work_space,report_id=report_id,j=j)

    val = request.json.get("c_check")
    if val:
        print('ok')
        img_path=screen_matidhekech(j['webUrl'])
        path_of_pdf=transform_file_to_pdf(j['name'],img_path)
        session["path_pdf"]=path_of_pdf
        time.sleep(2)
        return jsonify({"data": {"val": "you're file was converting"}})

@app.route("/send_mail",methods=["POST","GET"])
def send_mail():
    if request.method=="POST":
        session["recieve"]=request.form.get("recieve_adr")
        session["subject"]=request.form.get("subject")
        session["msg"]=request.form.get("msg")
        session["send_timing"]=request.form.get("time_to_send")
        session["which_day"]=request.form.get("value_for_day")
        session["every_"]=request.form.get("period_day")
        if session["send_timing"]=="":
            session["send_timing"]=d.now().strftime("%H:%M")
        else:
            pass

        path=session["path_pdf"]
        name_repport_bi= path.split('/')[-1].split('.')[0]
        per=session["which_day"]+" "+session["every_"]

        if add(session["recieve"].split(','),path,name_repport_bi,per,session["subject"],session["send_timing"]):
            return redirect(url_for('dashbord'))

    return render_template('index.html')

# @app.route("/send_mail",methods=["POST","GET"])
# def send_mail():
#     print("\t",session["path_pdf"])
#     if request.method=="POST":
#         session["recieve"]=request.form.get("recieve_adr")
#         session["subject"]=request.form.get("subject")
#         session["msg"]=request.form.get("msg")
#         print(session["recieve"],session["subject"])
#         return redirect(url_for("time_selection_time"))

#     return render_template("mail.html")

# @app.route("/send_mail/define_time",methods=["POST","GET"])
# def time_selection_time():
#     if request.method=="POST":
#         session["send_timing"]=request.form.get("time_to_send")
#         session["which_day"]=request.form.get("value_for_day")
#         session["every_"]=request.form.get("period_day")
#         if session["send_timing"]=="":
#             session["send_timing"]=d.now().strftime("%H:%M")
#         else:
#             pass
        
#         if send_pdf_file(session["recieve"].split(','),session["subject"],session["path_pdf"],session["msg"]):
#             return redirect(url_for('dashbord'))
        
#     return render_template("time.html")

# @app.route('/send_mail/file_sending',methods=["POST","GET"])
# def file_pdf_send():
#     return render_template('file.html')




if "__main__"==__name__:
    # c=ancienne_data()
    # t = Thread(target=main, args=(c,))
    # t.start()
    app.run(debug=True,port=3000)#,host='192.168.1.46')