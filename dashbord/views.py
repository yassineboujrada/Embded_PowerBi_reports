from datetime import datetime
from django.shortcuts import render, redirect
import joblib
from .Power_bi_functions import *
from .models import Post,microsoft_account
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserUpdateform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from threading import Thread
import time as time_
import _thread
import schedule
        
def f(title_of_report,who,form,url,every_what,email):
    try:
        k=screen_matidhekech(url,email,microsoft_account.objects.filter(email_account=email).get().password_accoount)
        pdf_path=transform_file_to_pdf(title_of_report,k,form)

        if send_pdf_file(recieve=who,subject="report of power bi: {}".format(title_of_report),path=pdf_path,mesg="Power BI report"):
            print("hola")
    except :
        print("it's just probleme in email")

def minute(title_of_report,who,form,url,every_what,every,email):
    schedule.every(int(every)).minutes.do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)
    

def hour_(title_of_report,who,form,url,every_what,every,email):
    schedule.every(int(every)).hours.do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)

def days(title_of_report,who,form,url,every_what,time,every,email):
    schedule.every(int(every)).days.at(str(time)).do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)

def week_(title_of_report,who,form,url,every_what,time,every,email):
    schedule.every(int(every)*7).days.at(str(time)).do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)

def month_(title_of_report,who,form,url,every_what,time,every,email):
    schedule.every(int(every)*30).days.at(str(time)).do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)

def year_(title_of_report,who,form,url,every_what,time,every,email):
    schedule.every(int(every)*365).days.at(str(time)).do(f,title_of_report,who,form,url,every_what,email)
    while True:
        schedule.run_pending()
        time_.sleep(1)

def main2():
    post=Post.objects.all()
    for i in post:
        title_of_report=i.title
        who=i.delivery
        form=i.format
        time=i.at
        every=i.every
        every_what=i.reccurence
        url=i.url_of_reports
        email=i.author.email
        if every_what == "minutes":
            _thread.start_new_thread(minute,(title_of_report,who,form,url,every_what,every,email))
        
        if every_what == "hour":
            _thread.start_new_thread(hour_,(title_of_report,who,form,url,every_what,every,email))
            
        if every_what == "day":
            _thread.start_new_thread(days,(title_of_report,who,form,url,every_what,time.strftime("%H:%M"),every,email))

        if every_what == "week":
            _thread.start_new_thread(week_,(title_of_report,who,form,url,every_what,time.strftime("%H:%M"),every,email))

        if every_what == "month":
            _thread.start_new_thread(month_,(title_of_report,who,form,url,every_what,time.strftime("%H:%M"),every,email))

        if every_what == "year":
            _thread.start_new_thread(year_,(title_of_report,who,form,url,every_what,time.strftime("%H:%M"),every,email))

# t = Thread(target=main2)
# t.start()
def make_it_easy(j):
    return Authentification_for_PowerBI(
                client_id=j['d']['client_id'],\
                user=j['d']['email'],\
                passwd=j['d']['password_accoount'],\
                tenant=j['d']['teneant_id'],\
                client_secret=j['d']['client_secret'],\
                file=j['d']['path_of_json'])
@login_required
def user_informations(request):
    form_up=UserUpdateform(instance=request.user)
    if request.method=="POST":
        form_up=UserUpdateform(request.POST,instance=request.user)
        if form_up.is_valid() :
            form_up.save()
            messages.success(request,f'nice')
            return redirect('userinfos')

    return render(request, 'blog/profile.html', {
        'form_up':form_up,
        'work':request.session['WORK_DATA'],
        'user':request.user,
        'acc_type':make_it_easy(request.session).CLIENT_POWER_BI.account_type,
        'capaities':make_it_easy(request.session).CLIENT_POWER_BI.capactities().get_capacities()['value'],
        'tenant':request.session['d']['teneant_id'],
        'key':request.session['d']['client_id']
    })

@login_required
def home(request):
    try:
        dd=request.session['WORK_DATA']
        request.session["all_report"]=make_it_easy(request.session).all_report()
        try:
            post_taille=Post.objects.filter(author=request.user.id).count()
        except:
            post_taille=0
    except KeyError:
        return HttpResponseRedirect('/login/')

    if request.method=="POST":
        Post.objects.filter(id=request.POST.get('id_to_delete','')).delete()
        return redirect('dashbord-home')

    return render(request,'blog/dashbord.html',{
        'work':dd,
        'len_playlist':post_taille,
        'len_report':request.session["all_report"][1],
        'db':Post.objects.filter(author=request.user.id)
    })

@login_required
def workspace(request,work):
    try:
        request.session['cuurent_space']=work
        if work == 'me':
            reports=make_it_easy(request.session).get_my_workspace()['value']
        else:
            reports=make_it_easy(request.session).get_report_from_workspace(work)['value']
    except KeyError:
        return HttpResponseRedirect('/login/')

    return render(request,'blog/workspace.html',{
        'work':request.session['WORK_DATA'],
        'report': reports
    })

@login_required
def pass_change(request):
    if request.method=="POST":
        new=request.POST.get('new_passwd')
        confirm=request.POST.get('confirm_passwd')
        if new==confirm and len(new)>=8:
            usr = User.objects.get(username=request.user.username)
            usr.set_password(new)
            usr.save()
            messages.success(request,f"You're password change successfully")
            return HttpResponseRedirect('/change_pass/')
    return render(request,'blog/change_pass.html')

@login_required
def report(request,report):
    work_space=request.session['cuurent_space']
    report_id=report
    print(request.session['d']['path_of_json'])
    if work_space == 'me':
        k=make_it_easy(request.session).grab_my_report(report_id)
        k['embedUrl']+='&autoAuth=true&ctid='+make_it_easy(request.session).get_tenant()
    else:
        request.session['report_embded']=make_it_easy(request.session).get_report_from_workspace(request.session['cuurent_space'])['value']
        i=request.session['report_embded']
        for k in i:
            if k['id']==str(report_id):
                k['embedUrl']+='&autoAuth=true&ctid='+make_it_easy(request.session).get_tenant()
                # k['webUrl']+='/ReportSection'
            else: 
                pass
    
    return render(request,'blog/report.html',{
        'current':request.session['cuurent_space'],
        'work':request.session['WORK_DATA'],
        'j':k
    })

@login_required
def select_report(request):
    try:
        request.session['d']
        d=request.session['WORK_DATA']
    except KeyError:
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        web_url = request.POST.get('c_check', None)
        
        if web_url != ":list:":
            request.session['url_web']=web_url.split(":list:")[0].split(",")
            request.session['names']=web_url.split(":list:")[1].split(",")
            return JsonResponse({'message':'ok'})
        else:
            return JsonResponse({'message':'not'})
    
    return render(request,'blog/report_select.html',{
        'all_work':d, 
        'all_report':request.session["all_report"][0],
        'tenant':make_it_easy(request.session).get_tenant(),
    })

ALLOWED_EMAIL_EXTENSIONS = set(['com', 'ma'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EMAIL_EXTENSIONS

@login_required
def create_playlist(request):
    try:
        name=" ".join(request.session['names'])
        url_=request.session['url_web']
    except KeyError:
        return HttpResponseRedirect('/playlist/create/select_report/')
    
    l=[]
    if request.method == 'POST':
        title=request.POST.get("title", "")
        email=request.POST.get("email", "")
        format=request.POST.get("format_file", "")
        every=request.POST.get("every", "")
        at=request.POST.get("at", "")
        reccurecy=request.POST.get("reccur_day", "")
        url=url_

        if every=="":
            every=2

        try:
            x=int(every)
            if isinstance(x, int):
                pass
            if at=="":
                at=datetime.now().strftime("%H:%M")
            for i in email.split(","):
                l.append(allowed_file(i))
            if True in l:   
                try:
                    f=Post(title=title,delivery=",".join(email.split(",")),format=format,at=at,every=every,reccurence=reccurecy,url_of_reports=",".join(url),author=request.user)
                    f.save()
                    del request.session['names']
                    del request.session['url_web']
                except:
                    messages.success(request,f'playlist did not saved')
                    return HttpResponseRedirect('/playlist/create/')
            else:
                messages.success(request,f'error in email input the acceptable domains are .com and .ma')
                return HttpResponseRedirect('/playlist/create/')
        except ValueError:
            messages.success(request,f'invalid input data')
            return HttpResponseRedirect('/playlist/create/')

        messages.success(request,f'Youre playlist has been added'+"\U0001f600")
        return HttpResponseRedirect('/')

    return render(request, 'blog/create.html', {'work':request.session['WORK_DATA'],'name':name})