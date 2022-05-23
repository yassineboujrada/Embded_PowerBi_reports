
from datetime import datetime as d
from flask import Flask, render_template,request, session,redirect,jsonify,make_response
# from parso import parse
from Power_bi_functions import *
from flask.helpers import url_for,flash
from threading import Thread


app=Flask(__name__)
UPLOAD_FOLDER = 'static/files/'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.secret_key = "5791628bb0b13ce0c676dfde280ba245"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# app = Flask(__name__)

try:
    from urllib.parse import unquote  # PY3
except ImportError:
    from urllib import unquote

@app.route('/v1/<path:param>')  # NOTE: <path:param> is required to match /
def f(param=''):
    return (
        f"param: {param}\ndecoded param: {unquote(param)}\n",
        200,
        {'content-type': 'text/plain'}
    )

@app.route("/",methods=["POST","GET"])
def login_in():

    if request.method=="POST":
        session["email_connect"]=request.form.get("email_conect")
        session["password"]=request.form.get("password")
        res=search_about("User","-N2hHzN_G51X1PurUwyB",session["email_connect"])
        if res !=None:
            if session["password"]==res['password']:
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
    # Authentification_for_PowerBI().nwita()
    print(work_space)
    for k in i:
        if k['id']==str(report_id):
            j=k
            j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
            session['report_name_for_send']=j['id']+"||"+j['name']   
        else: 
            pass

    if request.method=='GET':
        return render_template('Show_report.html',work_space=work_space,report_id=report_id,j=j)

    val = request.json.get("c_check")
    pages=Authentification_for_PowerBI().get_pages_number(work_space,report_id)
    
    if val:
        g=screen_shot(val,len(pages['value']))
        # Authentification_for_PowerBI().nwita()
        path_of_pdf=transform_file_to_pdf(j['name'],g)
        session["path_pdf"]=path_of_pdf
        time.sleep(2)
        return jsonify({"data": {"val": "wait some minutes to export you're file","fun":"hhhhhhhhhh"}})
    

@app.route("/send_mail",methods=["POST","GET"])
def send_mail():
    print(session['report_name_for_send'],"\t",session["path_pdf"])
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

        # return redirect(url_for('file_pdf_send'))

    return render_template("time.html")

@app.route('/send_mail/file_sending',methods=["POST","GET"])
def file_pdf_send():
    return render_template('file.html')




if "__main__"==__name__:
    # t = Thread(target=main, args=('test','legend.eleve@gmail.com','ok','./files/file.pdf',))
    # t.start()
    app.run(debug=True,port=3000)#,host='192.168.1.42')
    







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



