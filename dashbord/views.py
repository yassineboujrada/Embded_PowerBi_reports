from django.shortcuts import render
from .Power_bi_functions import *
from .models import Post
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    request.session['work']=Authentification_for_PowerBI().show_workspace()
    return render(request,'blog/dashbord.html',{
        'work':request.session['work'] 
    })


def workspace(request,work):
    request.session['cuurent_space']=work
    if work == 'me':
        reports=Authentification_for_PowerBI().get_my_workspace()['value']
    else:
        reports=Authentification_for_PowerBI().get_report_from_workspace(work)['value']
    return render(request,'blog/workspace.html',{
        'work':request.session['work'],
        'report': reports
    })

def report(request,report):
    work_space=request.session['cuurent_space']
    report_id=report
    if work_space == 'me':
        j=Authentification_for_PowerBI().grab_my_report(report_id)
        j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
    else:
        request.session['report_embded']=Authentification_for_PowerBI().get_report_from_workspace(request.session['cuurent_space'])['value']
        i=request.session['report_embded']
        for k in i:
            if k['id']==str(report_id):
                j=k
                j['embedUrl']+='&autoAuth=true&ctid='+Authentification_for_PowerBI().get_tenant()
                j['webUrl']+='/ReportSection'
            else: 
                pass
    
    return render(request,'blog/report.html',{
        'current':request.session['cuurent_space'],
        'work':request.session['work'],
        'j':j
    })

def playlist(request):
    
    if request.method=="POST":
        order = request.POST.get('c_check', None)
        if order=='Edit':
            print('edit')
        else:
            print('remove')

    return render(request,'blog/playlist.html',{
        'work':request.session['work'],
        'db':Post.objects.all()
    })

def create_playlist(request):
    if request.method == 'POST':
        print(request.POST)
        messages.success(request,f'Youre playlist has been  added'+"\U0001f600")
        return HttpResponseRedirect('/history_of_playlist/')

    return render(request, 'blog/create.html', {'work':request.session['work']})