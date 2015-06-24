# coding=utf-8
from django.shortcuts import render

# Create your views here.
import time
import copy
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import CommentRecord
from serializers import CommentRecordSerializer
from rest_framework.renderers import JSONRenderer
import urllib
import urllib2

from helloworld.utils import UrlParse


class JSONResponse(HttpResponse):
    """
    将JSON转为httpresponse
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def gethtml(request):
    content = UrlParse.UrlParse.get_html_content("http://www.sogou.com/web?query=jquery")
    return HttpResponse(content)


@csrf_exempt
def comment_record_list(request):
    if request.method == "GET":
        record_list = CommentRecord.objects.all()
        list_serializer = CommentRecordSerializer(record_list, many=True)
        return JSONResponse(list_serializer.data, status=200)
    elif request.method == "POST":
        data = copy.copy(request.POST)
        data['create_time'] = time.time()
        comment_record = CommentRecordSerializer(data=data)
        if comment_record.is_valid():
            try:
                comment_record.save()
                return JSONResponse(comment_record.data, status=200)
            except Exception as err:
                return JSONResponse({"msg": "save data error"}, status=400)
        else:
            return JSONResponse(comment_record.errors, status=400)