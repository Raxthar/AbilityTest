from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import ATest, Question, Judge, Option, Result
# Create your views here.
from .models import Dimension
import types


# 创建维度
def create_dimension(request):
    print('create_dimension')
    obj = json.loads(request.body.decode('utf-8'))
    d_names_arr = obj['dimensions']
    t_id = obj['tId']
    u_id = obj['uId']
    print(d_names_arr)
    try:
        for i in range(len(d_names_arr)):
            dimension = Dimension(d_name=d_names_arr[i].get('dName'), t_id=t_id)
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
    obj = json.loads(request.body.decode('utf-8'))
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
    obj = json.loads(request.body.decode('utf-8'))
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
    obj = json.loads(request.body.decode('utf-8'))
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
    obj = json.loads(request.body.decode('utf-8'))
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
            option = Option(
                o_name=option_name[o_name], q_id=question_info.q_id, score=option_score[score],d_id=option_dimension[d_id])
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


def question_chat(request):
    obj = json.loads(request.body.decode('utf-8'))
    question_name = obj['qName']
    test_id = obj['tId']
    o_name = obj['oName']
    score = obj['score']
    d_id = obj['dId']
    try:
        question = Question(q_name=question_name, t_id=test_id)
        question.save()
        question_info = Question.objects.get(q_name=question_name, t_id=test_id)
        for i in range(len(d_id)):
            option = Option(
                o_name=o_name[i], q_id=question_info.q_id, score=score[i], d_id=d_id[i])
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
    obj = json.loads(request.body.decode('utf-8'))
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
    list_describe = []
    try:
        test_info = ATest.objects.filter(u_id=u_id)
        for i in range(len(test_info)):
            list_name.append(test_info[i].t_name)
            list_status.append(test_info[i].t_status)
            list_due.append(test_info[i].t_due)
            list_id.append(test_info[i].t_id)
            list_describe.append(test_info[i].t_describe)
        message['tId'] = list_id
        message['tName'] = list_name
        message['tStatus'] = list_status
        message['tDue'] = list_due
        message['tDescribe'] = list_describe
        message['code'] = 200
        return JsonResponse(message)
    except Exception as e:
        message['code'] = 0
        return JsonResponse(message)


def set_dimension_page(request):
    obj = json.loads(request.body.decode('utf-8'))
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


def delete_question(request):
    obj = json.loads(request.body.decode('utf-8'))
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
    obj = json.loads(request.body.decode('utf-8'))
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


def search_atest_by(request):
    t_id = request.GET['tId']
    try:
        atest_old = ATest.objects.get(t_id=t_id)
        response = {
            "tName": atest_old.t_name,
            "tDescribe": atest_old.t_describe,
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def update_atest(request):
    obj = json.loads(request.body.decode('utf-8'))
    t_id = obj["tId"]
    t_name = obj["evaluationName"]
    t_describe = obj['evaluationDescribe']
    try:
        ATest.objects.filter(t_id=t_id).update(t_name=t_name, t_describe=t_describe)
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0
        }
    return JsonResponse(response)


def update_dimension(request):
    obj = json.loads(request.body.decode('utf-8'))
    t_id = obj["tId"]
    d_name = obj['dimensionName']
    try:
        dimension_list = Dimension.objects.filter(t_id=t_id)
        for i in range(len(dimension_list)):
            dimension_list[i].d_name = d_name[i]
            dimension_list[i].save()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0
        }
    return JsonResponse(response)


def search_stat(request):
    t_id = request.GET['tId']
    d_name_list = []
    d_id_list = []
    stat_list = []
    try:
        result_list = Result.objects.filter(t_id=t_id)
        d_list = []
        for i in range(len(result_list)):
            d_list.append(result_list[i].d_id)
        r_dic = get_stat(d_list)
        for v,k in r_dic.items():
            d_id_list.append(v)
            stat_list.append(k)
        for i in range(len(d_id_list)):
            d_name_list.append(Dimension.objects.get(d_id=d_id_list[i]).d_name)
        response = {
            "dName": d_name_list,
            "stat": stat_list,
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def get_stat(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result


def edit_judge(request):
    print('edit_judge')
    obj = json.loads(request.body.decode('utf-8'))
    d_id_list = obj['dimensionId']
    j_content_list = obj['judge']
    t_due = obj['due']
    t_id = obj['tId']
    try:
        ATest.objects.filter(t_id=t_id).update(t_due=t_due)
        j_list = Judge.objects.filter(t_id=t_id)
        if (len(j_list) == 0):
            for i in range(len(d_id_list)):
                judge = Judge(t_id=t_id, j_content=j_content_list[i], d_id=d_id_list[i])
                judge.save()
        else:
            for i in range(len(j_list)):
                j_list[i].t_id = t_id
                j_list[i].j_content = j_content_list[i]
                j_list[i].d_id = d_id_list[i]
                j_list[i].save()
        response = {
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)


def load_result(request):
    t_id = request.GET['tId']
    print(t_id)
    d_name_list = []
    rid_list = []
    try:
        result_list = Result.objects.filter(t_id=t_id)
        for i in range(len(result_list)):
            rid_list.append(result_list[i].result_id)
            d_name_list.append(Dimension.objects.get(d_id=result_list[i].d_id).d_name)
        response = {
            "resultId": rid_list,
            "dName": d_name_list,
            "code": 200
        }
    except Exception as e:
        response = {
            "code": 0,
            "errMsg": e
        }
    return JsonResponse(response)