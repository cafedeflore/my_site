# coding=utf-8

from django.shortcuts import render_to_response
from serializers import DealTaskSerializer
from models import DealTask
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    """
    将内容转为JSON格式的HttpResponse
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.
# @csrf_exempt
def task_show_page(request):
    if request.method == "GET":
        data = request.GET
        try:
            id = data['id']
        except KeyError:
            return render_to_response('dealsupplier/deal_task_page.html')
        return render_to_response('dealsupplier/deal_task_page.html', {'id': id})
    return render_to_response('dealsupplier/error.html', {})


@csrf_exempt
def deal_task_list(request):
    if request.method == "GET":
        data = DealTask.objects.all()
        task_lists = DealTaskSerializer(data, many=True)
        return JSONResponse(task_lists.data)
    elif request.method == "POST":
        deal_task = DealTaskSerializer(data=request.POST)
        if deal_task.is_valid():
            try:
                deal_task.save()
                return JSONResponse(deal_task.data, status=201)
            except Exception as err:
                return JSONResponse({"msg": "save data error"}, status=400)
        return JSONResponse(deal_task.errors, status=400)


@csrf_exempt
def deal_task(request, id):
    try:
        task = DealTask.objects.get(id=id)
    except DealTask.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        task_serializer = DealTaskSerializer(task)
        return JSONResponse(task_serializer.data, status=200)
    elif request.method == "POST":
        task_serializer = DealTaskSerializer(task, data=request.POST)
        if task_serializer.is_valid():
            task_serializer.save()
            return JSONResponse(task_serializer.data, status=200)
        return JSONResponse(task.errors, status=400)
    elif request.method == "DELETE":
        task.delete()
        return JSONResponse({"msg": "delete succeed"}, status=200)
    else:
        return HttpResponse(status=404)