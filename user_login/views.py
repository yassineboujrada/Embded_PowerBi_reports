from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from dashbord.Power_bi_functions import *
import os
from dashbord.models import microsoft_account
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def register_steps(request):    
    return render(request,'blog/steps_to_register.html')

def registre(request):
    if request.method=="POST":
        ####  user information
        new_user_email=request.POST.get('email')
        new_user_password=request.POST.get('password')
        ####  azuer information
        new_user_client_id=request.POST.get('id_key')
        new_user_tenant_id=request.POST.get('tenant')
        new_user_client_secret=request.POST.get('secret_key')

        super_user_email=request.POST.get('email_of_supervise')

        try:
            Authentification_for_PowerBI(client_id=str(new_user_client_id),user=str(new_user_email),\
                                passwd=str(new_user_password),tenant=str(new_user_tenant_id),\
                                client_secret=str(new_user_client_secret),file=str(new_user_email.split('@')[0]))
                                
            try:
                add_new_user(super_user_email,str(new_user_password),str(new_user_client_secret),str(new_user_email),str(new_user_client_id),str(new_user_tenant_id))
                messages.success(request,"you're request was send it succesffuly")
                return redirect('login')
            except:
                print("mesage didnt go")
                messages.success(request,"You enter invalid email in superuser")
                return redirect('registre_me')

        except :
            messages.success(request,"Ther's an error")
            return redirect('registre_me')
        # return redirect('validate')
        
    return render(request,'blog/register.html')

# @login_required(login_url='/add_user/')
def add(request):  

    if request.method=='POST':
        print(request.POST.get('add',''))
        if request.POST.get('add','')=="add":
            print(request.user)
            # User(user)
            user = User.objects.create_user(username=request.session['cc'], email=request.session['email'], password=request.session['passwd'])
            user.save()
            print(user)
            micro_new=microsoft_account(email_account=request.session['email'],password_accoount=request.session['passwd'],client_id=request.session['cle_id'],client_secret=request.session['cle_secret'],teneant_id=request.session['ten'],path_of_json=os.getcwd()+"\\dashbord\\__pycache__\\"+request.session['cc']+".jsonc",author_account=user)
            micro_new.save()
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

    if request.method=='GET':
        try:
            request.session['cc']=request.GET.get('q1','')
            # request.session['password']=request.GET.get('q1','')
            # request.session['client_secret']=request.GET.get('q2','')
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
                            
            print("mmmm",l.email_account,l.password_accoount,l.client_id,l.client_secret,l.teneant_id,l.path_of_json)
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