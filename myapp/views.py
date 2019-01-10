from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import ATest, Question, Judge, Option
# Create your views here.
from .models import Dimension


def create_dimension(request):
    print('create_dimension')
    obj = json.loads(request.body)
    d_names_arr = obj['dimensions']
    t_id = obj['t_id']
    u_id = obj['u_id']
    try:
        print(d_names_arr)
        for i in d_names_arr:
            print(i)
            dimension = Dimension(d_name=d_names_arr.get(i), t_id=t_id)
            dimension.save()
        '''
        question_list = []
        for i in Question.objects.filter(t_id=t_id):
            question_list.append(i.q_name)
        print(question_list)
        '''
        response = {
            # "question_data": question_list
            "code": 200
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
        atest_list = []
        for i in ATest.objects.filter(u_id=u_id):
            atest_list.append([i.t_name, i.t_describe, i.t_status, i.t_due])
        response = {
            "data": atest_list
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def create_judge(request):
    obj = json.loads(request.body)
    t_id = obj['t_id']
    content = obj['content']
    print(content)
    try:
        for i in content:
            judge = Judge(t_id=t_id, d_id=i.get('d_id'), j_content=i.get('j_content'))
            judge.save()
        atest_list = []
        for i in ATest.objects.filter(u_id=u_id):
            atest_list.append([i.t_name, i.t_describe, i.t_status, i.t_due])
        response = {
            "data": atest_list
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


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
    dimension_id = []
    dimension_name = []
    test_info = Dimension.objects.filter(t_id=test_id)
    for i in range(len(test_info)):
        dimension_id.append(test_info[i].d_id)
        dimension_name.append(test_info[i].d_name)
    dimension['d_id'] = dimension_id
    dimension['d_name'] = dimension_name
    return JsonResponse(dimension)

def edit_question(request):
    obj = json.loads(request.body)
    question_id = obj["q_id"]
    message = {}
    option_name = []
    option_score = []
    dimension_id = []
    dimension_name = []
    question = Question.objects.get(q_id=question_id)
    message["q_name"] = question.q_name
    option_list = Option.objects.filter(q_id=question_id)
    for i in range(len(option_list)):
        option_name.append(option_list[i].o_name)
        dimension_id.append(option_list[i].d_id)
        option_score.append(option_list[i].score)
        dimension = Dimension(d_id=option_list[i].d_id)
        dimension_name.append(dimension.d_name)
    message["o_name"] = option_name
    message["d_id"] = dimension_id
    message["d_name"] = dimension_name
    message["score"] = option_score
    return JsonResponse(message)


def update_question(request):
    obj = json.loads(request.body)
    question_id = obj["q_id"]
    option_name = obj['o_name']
    option_score = obj['score']
    option_dimension = obj['d_id']
    option_list = Option.objects.filter(q_id=question_id)
    for i in range(len(option_list)):
        option_list[i].o_name = option_name[i]
        option_list[i].score = option_score[i]
        option_list[i].d_id = option_dimension[i]
        option_list[i].save()
    response = {
        "data": 200
    }
    return JsonResponse(response)
def set_dimension_page(request):
    obj = json.loads(request.body)
    test_id = obj['t_id']
    dimension = {}
    dimension_id = []
    dimension_name = []
    test_info = Dimension.objects.filter(t_id=test_id)
    for i in range(len(test_info)):
        dimension_id.append(test_info[i].d_id)
        dimension_name.append(test_info[i].d_name)
    dimension['d_id'] = dimension_id
    dimension['d_name'] = dimension_name
    return JsonResponse(dimension)

def set_deadline(request):
    obj = json.loads(request.body)
    test_id = obj['t_id']
    test_due = obj['t_due']
    test_message = {}
    test_info = ATest.objects.get(t_id=test_id)
    test_info.t_due = test_due
    test_info.save()
    test_update = ATest.objects.get(t_id=test_id)
    test_message['t_name'] = test_update.t_name
    test_message['t_status'] = test_update.t_status
    test_message['t_due'] = test_update.t_due
    return JsonResponse(test_message)
