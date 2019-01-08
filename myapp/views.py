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


def create_dimension(request):
    print('create')
    obj = json.loads(request.body)
    d_names_arr = obj['dimensions']
    tID = obj['tID']
    uID = obj['uID']
    try:
        for dName in d_names_arr:
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


def search_all_atest(request):
    obj = json.loads(request.body)
    u_id = obj['u_id']
    try:
        atest = serializers.serialize("json", Question.objects.filter(u_id=u_id))   # 查数据库找出测评号tID对应的所有题目
        res = {
            "code": 200,
            "data": atest
        }
        print(question)
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
    test_info = Test.objects.get(tName=test_name, qDescribe=test_describe, status=0, id=_id, Due="")
    test_id['data'] = test_info.tID
    return JsonResponse(test_id)


def add_question(request):
    obj = json.loads(request.body)
    question_name = obj['qName']
    test_id = obj['tID']
    option_name = obj['oName']
    option_score = obj['score']
    option_dimension = obj['dID']
    question_list = {}
    question = Question(qName=question_name, tID_id=test_id)
    question.save()
    question_info = Question.objects.get(qName=question_name, tID_id=test_id)
    question_list['name'] = question_info.qName
    question_list['qID']=question_info.qID
    for (oName, score, dimension) in zip(option_name, option_score, option_dimension):
        option = Option(oName=oName, qID_id=question1.qID, score=score,
                        dID=dimension)
            option.save()
    return JsonResponse(question_list)


def set_evaluate(request):
    obj = json.loads(request.body)
    test_id = obj['t_id']
    dimension = {}
    test_info = Dimension.objects.get(t_id=test_id)
    dimension['d_id'] = test_info.d_id
    dimension['d_name'] = test_info.d_name
    return JsonResponse(dimension)
