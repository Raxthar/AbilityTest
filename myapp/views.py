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
    print('create_dimension')
    obj = json.loads(request.body)
    d_names_arr = obj['dimensions']
    t_id = obj['t_id']
    u_id = obj['u_id']
    try:
        for d_name in d_names_arr:
            dimension = Dimension(d_name=d_name, t_id=t_id)
            dimension.save()
        question_list = []
        for i in Question.objects.filter(t_id=t_id):
            question_list.append(i.q_name)
        print(question_list)
        response = {
            "code": 200,
            "question_data": question_list
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def search_all_atest(request):
    obj = json.loads(request.body)
    u_id = obj['u_id']
    try:
        atest = serializers.serialize("json", Question.objects.filter(u_id=u_id))
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
    test = ATest(t_name=test_name, t_describe=test_describe, t_status=0, u_id=u_id, t_due="")
    test.save()
    test_info = ATest.objects.get(t_name=test_name, t_describe=test_describe, t_status=0, u_id=u_id, t_due="")
    test_id['data'] = test_info.t_id
    return JsonResponse(test_id)


def add_question(request):
    obj = json.loads(request.body)
    question_name = obj['q_name']
    test_id = obj['t_id']
    option_name = obj['o_name']
    option_score = obj['score']
    option_dimension = obj['d_id']
    question_list = {}
    question = Question(q_name=question_name, t_id=test_id)
    question.save()
    question_info = Question.objects.get(q_name=question_name, t_id=test_id)
    question_list['q_name'] = question_info.q_name
    question_list['q_id'] = question_info.q_id
    for (oName, score, dimension) in zip(option_name, option_score, option_dimension):
        option = Option(o_name=oName, q_id=question_info.q_id, score=score,
                        d_id=dimension)
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
