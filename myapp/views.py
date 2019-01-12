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
    t_id = obj['tId']
    u_id = obj['uId']
    try:
        for i in d_names_arr:
            dimension = Dimension(d_name=d_names_arr.get(i), t_id=t_id)
            dimension.save()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def search_all_questions(request):
    t_id = request.GET['tId']
    try:
        question_name_list = []
        question_id_list = []
        for i in Question.objects.filter(t_id=t_id):
            question_id_list.append(i.q_id)
            question_name_list.append(i.q_name)
        response = {
            "questionId": question_id_list,
            "questionName": question_name_list,
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
    u_id = obj['uId']
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
    t_id = obj['tId']
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
    u_id = obj['uId']
    response = {}
    try:
        test = ATest(t_name=test_name, t_describe=test_describe, t_status=0, u_id=u_id, t_due="")
        test.save()
        response['tId'] = test.t_id
        response['code'] = 200
        return JsonResponse(response)
    except Exception as e:
        response['code'] = 0
        return JsonResponse(response)


def add_question(request):
    obj = json.loads(request.body)
    question_name = obj['qName']
    test_id = obj['tId']
    option_name = obj['oName']
    option_score = obj['score']
    option_dimension = obj['dId']
    try:
        question = Question(q_name=question_name, t_id=test_id)
        question.save()
        question_info = Question.objects.get(q_name=question_name, t_id=test_id)
        for (o_name, score, d_id) in zip(option_name, option_score, option_dimension):           
            option = Option(o_name=option_name[o_name], q_id=question_info.q_id, score=option_score[score],d_id=option_dimension[d_id])
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


# 找t_id对应的所有的维度
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
        dimension['dId'] = dimension_id
        dimension['dName'] = dimension_name
        dimension['code'] = 200
    except Exception as e:
        dimension['code'] = 0
        dimension['errMsg'] = e
    return JsonResponse(dimension)


def edit_question(request):
    question_id = request.GET['qId']
    message = {}
    option_name = []
    option_score = []
    dimension_id = []
    dimension_name = []
    try:
        question = Question.objects.get(q_id=question_id)
        message["qName"] = question.q_name
        option_list = Option.objects.filter(q_id=question_id)
        for i in range(len(option_list)):
            option_name.append(option_list[i].o_name)
            dimension_id.append(option_list[i].d_id)
            option_score.append(option_list[i].score)
            dimension = Dimension(d_id=option_list[i].d_id)
            dimension_name.append(dimension.d_name)
        message["oName"] = option_name
        message["dId"] = dimension_id
        message["dName"] = dimension_name
        message["score"] = option_score
        message['code'] = 200
    except Exception as e:
        message['code'] = 0
        message['errMsg'] = e
    return JsonResponse(message)


def update_question(request):
    obj = json.loads(request.body)
    question_id = obj["qId"]
    new_q_name = obj["newQuestionName"]
    new_option_data = obj['newOptionData']
    try:
        Question.objects.filter(q_id=question_id).update(q_name=new_q_name)
        option_list = Option.objects.filter(q_id=question_id)
        for i in range(len(option_list)):
            option_list[i].o_name = new_option_data[i].get('oName')
            option_list[i].score = new_option_data[i].get('score')
            option_list[i].d_id = new_option_data[i].get('dId')
            option_list[i].save()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0
        }
    return JsonResponse(response)


def test_list(request):
    u_id = request.GET['uId']
    message = {}
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
        message['tId'] = list_id
        message['tName'] = list_name
        message['tStatus'] = list_status
        message['tDue'] = list_due
        message['code'] = 200
        return JsonResponse(message)
    except Exception as e:
        message['code'] = 0
        return JsonResponse(message)


def set_dimension_page(request):
    obj = json.loads(request.body)
    test_id = obj['tId']
    dimension = {}
    dimension_id = []
    dimension_name = []
    test_info = Dimension.objects.filter(t_id=test_id)
    for i in range(len(test_info)):
        dimension_id.append(test_info[i].d_id)
        dimension_name.append(test_info[i].d_name)
    dimension['dId'] = dimension_id
    dimension['dName'] = dimension_name
    return JsonResponse(dimension)


def set_deadline(request):
    obj = json.loads(request.body)
    test_id = obj['tId']
    test_due = obj['tDue']
    test_message = {}
    test_info = ATest.objects.get(t_id=test_id)
    test_info.t_due = test_due
    test_info.save()
    test_update = ATest.objects.get(t_id=test_id)
    test_message['tName'] = test_update.t_name
    test_message['tStatus'] = test_update.t_status
    test_message['tDue'] = test_update.t_due
    return JsonResponse(test_message)


def delete_question(request):
    obj = json.loads(request.body)
    q_id = obj['qId']
    try:
        Question.objects.filter(q_id=q_id).delete()
        Option.objects.filter(q_id=q_id).delete()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def delete_evaluation(request):
    obj = json.loads(request.body)
    t_id = obj['tId']
    try:
        ATest.objects.filter(t_id=t_id).delete()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)
