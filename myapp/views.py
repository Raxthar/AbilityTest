from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import ATest, Question
# Create your views here.
from .models import Dimension


def createDimension(request):
    print('create')
    obj = json.loads(request.body)
    dNamesArr = obj['dimensions']
    tID = obj['tID']
    uID = obj['uID']
    try:
        for dName in dNamesArr:
            dimension = Dimension(dName=dName, tID_id=tID)
            dimension.save()
        question = serializers.serialize("json", Question.objects.filter(tID_id=tID))   # 查数据库找出测评号tID对应的所有题目
        print(question)
        response = {
            "code": 200,
            "question_data": question
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(response), content_type="application/json")

'''
def searchAllQuestions(request):
    content = request.GET['content']
    try:
        question = serializers.serialize("json", Question.objects.filter(tID=content))   # 查数据库找出测评号tID对应的所有题目
        res = {
            "code": 200,
            "data": question
        }
        print(question)
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")
'''


def create(request):
    obj = json.loads(request.body)
    name = obj['title']
    describe = obj['describe']
    try:
        book = ATest(tName=name, tDescribe=describe)
        book.save()
        res = {
            "code": 200,
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")


def create(request):
    obj = json.loads(request.body)
    test_name = obj['tName']
    test_describe = obj['tDescribe']
    _id = obj['uID']
    test_id = {}
    test = Test(tName=test_name, qDescribe=test_describe, status=0, id=_id, Due="")
    test.save()
    test1 = Test.objects.get(tName=test_name, qDescribe=test_describe, status=0, id=_id, Due="")
    print(test1.tID)
    test_id['data'] = test1.tID
    return JsonResponse(test_id)
