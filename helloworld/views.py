#coding=utf-8
from django.shortcuts import render

from django.template.loader import get_template
from django.template import Context
from django.http import HttpRequest


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import json

import subprocess

import time

from helloworld.models import Check_Task

# Create your views here.
def hello(request):
    return render_to_response('test.html', {})

def home(request):
    return render_to_response('home.html', {})

def new_check_task(request):
    return render_to_response('new_check_task.html', {}, context_instance=RequestContext(request))

# @csrf_exempt
def add_task(request):
    if request.POST.has_key('name'):
        task = Check_Task()
        task.name = request.POST['name']
        task.create_time = time.strftime("%Y-%m-%d %H:%M:%S")
        task.save()
        # print task.id
        # print task.name
    return HttpResponseRedirect('/check_task_list/')

def upload(request):
    print "llll"
    if request.method == 'POST':
        file = request.FILES['package']
        handle_uploaded_file(file)
    return HttpResponseRedirect('/check_task_list/')

def handle_uploaded_file(f):
    with open("D:/test/" + f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def task_detail(request):
    if request.GET.has_key('id'):
        id = request.GET['id']
        try:
            task = Check_Task.objects.get(id=id)
        except:
            #应该返回错误页
            return render_to_response('test.html', {})
    else :
        print "error"
    return render_to_response('task_detail.html', {'task': task})

def show_list():
    task_list = Check_Task.objects.all()
    # return HttpRequest('succeed:0')
    return render_to_response('check_task_list.html', {'task_list': task_list})

def check_task_list(request):
    task_list = Check_Task.objects.all()
    # return HttpRequest('succeed:0')
    return render_to_response('check_task_list.html', {'task_list': task_list}, context_instance=RequestContext(request))

# @csrf_exempt
def test_ajax(request):
    try:
        id = request.POST['id']
        task = Check_Task.objects.get(id=id)
        task.sql_check = request.POST['sql-check']
        task.db_compare = request.POST['db-compare']
        task.config_check = request.POST['config-check']
        task.pause_point_check = request.POST['pause-point-check']
        task.log_monitor = request.POST['log-monitor']
        task.checklist = request.POST['checklist']
        task.save()
    except:
        print "出错了"
    # result = 1
    # result = json.dumps(result)
    # print result
    # return HttpRequest(result, mimetype='application/javascript')

def get_table_check(request):
    try:
        p = subprocess.Popen('C:\\Python27\\python.exe test.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        retval = p.wait()
        # print "start"
        test = ""
        for line in p.stdout.readlines():
            # print line
            test += line
        # print "finished"
        print test
        # test = "lalal"
        # print type(test)
        return render_to_response('info.html', {'content': test})
    except:
        return