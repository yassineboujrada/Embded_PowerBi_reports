from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from dashbord.Power_bi_functions import *
import os
from dashbord.models import microsoft_account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import subprocess as sp

def getUrl(file,a):
    p = sp.run('py '+file+'.py',shell=True, stdout=sp.PIPE,input=a, encoding='ascii')
    print(p.stdout)
    if int(p.returncode)==1:
        return p.stdout.split("your account:")[1].split("Paste")[0]
    else:
        return int(p.returncode)

def register_steps(request):    
    return render(request,'blog/steps_to_register.html')

def termi(request): 
    try:
        initial_login=request.session['log']
        file_=request.session['file_py_for_redirection']
    except:
        return redirect('registre_me')

    if request.method=="POST":
        a=request.POST.get("url_redirect")
        if getUrl(file_,a) ==0:
            try:
                add_new_user(request.session['super_user_email'],str(request.session['new_user_password']),str(request.session['new_user_client_secret']),str(request.session['new_user_email']),str(request.session['new_user_client_id']),str(request.session['new_user_tenant_id']))
                messages.success(request,"you're request was send it succesffuly")
                return redirect('login')
            except:
                print("mesage didnt go")
                messages.success(request,"You enter invalid email in superuser")
                return redirect('registre_me')
    return render(request,'blog/cc.html',{"initial_login":initial_login})

def registre(request):
    if request.method=="POST":
        ####  user information
        request.session['new_user_email']=request.POST.get('email')
        request.session['new_user_password']=request.POST.get('password')
        ####  azuer information
        request.session['new_user_client_id']=request.POST.get('id_key')
        request.session['new_user_tenant_id']=request.POST.get('tenant')
        request.session['new_user_client_secret']=request.POST.get('secret_key')

        request.session['super_user_email']=request.POST.get('email_of_supervise')
        request.session['file_py_for_redirection']=request.session['new_user_email'].split('@')[0].split(".")[0]

        
        a="""
import os
from powerbi.client import PowerBiClient
class Authentification_for_PowerBI:
    def __init__(self,client_id,user,passwd,tenant,client_secret,file):
        self.CLIENT_ID=client_id 
        self.username=user
        self.password=passwd
        self.TENANT_ID=tenant
        self.AUTHORITY_URL = 'https://login.microsoftonline.com/'+self.TENANT_ID
        self.SCOPE = ["https://analysis.windows.net/powerbi/api/.default"]
        self.URL_TO_GET_GROUPS = 'https://api.powerbi.com/v1.0/myorg/groups'
        self.file=file
        self.CLIENT_POWER_BI = PowerBiClient(
            client_id=self.CLIENT_ID,
            client_secret=client_secret,
            scope=['https://analysis.windows.net/powerbi/api/.default'],
            redirect_uri="https://localhost/redirect",
            credentials=os.getcwd()+"/dashbord/__pycache__/"+self.file
        )
        self.reports_service = self.CLIENT_POWER_BI.reports()
Authentification_for_PowerBI("{}","{}","{}","{}","{}","{}")
    """.format(str(request.session['new_user_client_id']),str(request.session['new_user_email']),str(request.session['new_user_password']),str(request.session['new_user_tenant_id']),str(request.session['new_user_client_secret']),str(request.session['new_user_email'].split('@')[0]+".jsonc"))
        
        f = open(os.getcwd()+"/"+request.session['file_py_for_redirection']+".py", "w")
        f.write(a)
        f.close()

        request.session['log']= getUrl(request.session['file_py_for_redirection'],"")
        if request.session['log']==0:
            messages.success(request,"you're request already exist")
            return redirect('login')

        return redirect("termi")
        # try:
        #     add_new_user(request.session['super_user_email'],str(request.session['new_user_password']),str(request.session['new_user_client_secret']),str(request.session['new_user_email']),str(request.session['new_user_client_id']),str(request.session['new_user_tenant_id']))
        #     messages.success(request,"you're request was send it succesffuly")
        #     return redirect('login')
        # except:
        #     print("mesage didnt go")
        #     messages.success(request,"You enter invalid email in superuser")
        #     return redirect('registre_me')

        # return redirect('validate')
        
    return render(request,'blog/register.html')

# @login_required(login_url='/add_user/')
def add(request):  

    if request.method=='POST':
        print(request.POST.get('add',''))
        if request.POST.get('add','')=="add":
            print(request.user)
            # User(user)
            try:
                user = User.objects.create_user(username=request.session['cc'], email=request.session['email'], password=request.session['passwd'])
                user.save()
                print(user)
                micro_new=microsoft_account(email_account=request.session['email'],password_accoount=request.session['passwd'],client_id=request.session['cle_id'],client_secret=request.session['cle_secret'],teneant_id=request.session['ten'],path_of_json=os.getcwd()+"\\dashbord\\__pycache__\\"+request.session['cc']+".jsonc",author_account=user)
                micro_new.save()
            except:
                messages.success("this user is in database")
                return redirect("validate")

            return redirect("login")
        else:
            p = configparser.ConfigParser()
            with open(os.getcwd()+"\\dashbord\\__pycache__\\configfile.ini", "r") as f:
                p.readfp(f)

            # print(p.sections())
            g=p.remove_section(request.session['cc'])
            print(request.session['cc'])
            if g:
                print('delete')

            with open(os.getcwd()+"\\dashbord\\__pycache__\\configfile.ini", "w") as f:
                p.write(f)
                
            return redirect("login")

    if request.method=='GET':
        try:
            request.session['cc']=request.GET.get('q1','')
            print("mmdmmd",request.session['cc'])
            config_obj = configparser.ConfigParser()
            config_obj.read(os.getcwd()+"\\dashbord\\__pycache__\\configfile.ini")
            dbparam = config_obj[request.GET.get('q1','')]
            request.session['email'] = dbparam["email"]
            request.session['passwd'] = dbparam["passwd"]
            request.session['cle_secret'] = dbparam["cle_secret"]
            request.session['cle_id'] = dbparam["cle_id"]
            request.session['ten'] = dbparam["ten"]
        except:
            print('errir')
    
    print(User.objects.filter(username=request.session['cc']))
        # ,request.session['password'],request.session['client_secret'])

    return render(request,'blog/add.html',{
        'key':request.session['cle_id'],
        'ten':request.session['ten'],
    })

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # print(user)
        
        if user is not None:
            login(request,user)
            l=microsoft_account.objects.get(author_account=request.user.id)
            request.session['d']={
                'email':l.email_account,
                'password_accoount':l.password_accoount,
                'client_id':l.client_id,
                'client_secret':l.client_secret,
                'teneant_id':l.teneant_id,
                'path_of_json':l.path_of_json

            }
            request.session['WORK_DATA']=Authentification_for_PowerBI(
                client_id=request.session['d']['client_id'],\
                user=request.session['d']['email'],\
                passwd=request.session['d']['password_accoount'],\
                tenant=request.session['d']['teneant_id'],\
                client_secret=request.session['d']['client_secret'],\
                file=request.session['d']['path_of_json']).show_workspace()
                            
            # print("mmmm",l.email_account,l.password_accoount,l.client_id,l.client_secret,l.teneant_id,l.path_of_json)
            return redirect('dashbord-home')
        else: 
            messages.info(request,"Username or Password Incorrect !")

    return render(request,'blog/login.html', {
        
    })

def register_steps2(request):
    return render(request,'blog/steps_to_register2.html')

def user_logout(request):
    logout(request)
    return redirect('login')