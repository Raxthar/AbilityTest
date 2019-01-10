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


# 创建维度
def create_dimension(request):
    print('create_dimension')
    obj = json.loads(request.body)
    d_names_arr = obj['dimensions']
    t_id = obj['t_id']
    u_id = obj['u_id']
    try:
        for i in d_names_arr:
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


def search_all_questions(request):
    t_id = request.GET['t_id']
    try:
        question_name_list = []
        question_id_list = []
        for i in Question.objects.filter(t_id=t_id):
            question_id_list.append(i.q_id)
            question_name_list.append(i.q_name)
        response = {
            "question_id": question_id_list,
            "question_name": question_name_list,
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
    test_name = obj['t_name']
    test_describe = obj['t_describe']
    u_id = obj['u_id']
    test_id = {}
    try:
        test = ATest(t_name=test_name, t_describe=test_describe, t_status=0, u_id=u_id, t_due="")
        test.save()
        test_id['t_id'] = test.t_id
        test_id['code'] = 200
        return JsonResponse(test_id)
    except Exception as e:
        test_id['code'] = 0
        return JsonResponse(test_id)


def add_question(request):
    obj = json.loads(request.body)
    question_name = obj['q_name']
    test_id = obj['t_id']
    option_name = obj['o_name']
    option_score = obj['score']
    option_dimension = obj['d_id']
#    question_list = {}    
    try:
        question = Question(q_name=question_name, t_id=test_id)
        question.save()
        question_info = Question.objects.get(q_name=question_name, t_id=test_id)
#    question_list['q_name'] = question_info.q_name
#    question_list['q_id'] = question_info.q_id
        for (o_name, score, d_id) in zip(option_name, option_score, option_dimension):
            option = Option(o_name=o_name, q_id=question_info.q_id, score=score,d_id=d_id)
            option.save()
        response = {
                "code": 200
            }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


# 找所有的维度
def search_dimensions(request):
    t_id = request.GET['content']
    dimension = {}
    dimension_id = []
    dimension_name = []
    try:
        dimension_info = Dimension.objects.filter(t_id=t_id)
        for i in range(len(dimension_info)):
            dimension_id.append(dimension_info[i].d_id)
            dimension_name.append(dimension_info[i].d_name)
        dimension['d_id'] = dimension_id
        dimension['d_name'] = dimension_name
        dimension['code'] = 200
    except Exception as e:
        dimension['code'] = 0
        dimension['errMsg'] = e
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


def test_list(request):
    u_id = request.GET['u_id']
    test_message = {}
    list_name = []
    list_status = []
    list_due = []
    list_id = []
    try:
        test_info = ATest.objects.filter(u_id=u_id)
        for i in range(len(test_info)):
            list_name.append(test_info[i].t_name)
            list_status.append(test_info[i].t_status)
            list_due.append(test_info[i].t_due)
            list_id.append(test_info[i].t_id)
        test_message['t_id'] = list_id
        test_message['t_name'] = list_name
        test_message['t_status'] = list_status
        test_message['t_due'] = list_due
        test_message['code'] = 200
        return JsonResponse(test_message)
    except Exception as e:
        test_message['code'] = 0
        return JsonResponse(test_message)


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
