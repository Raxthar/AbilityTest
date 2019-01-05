from django.shortcuts import render

from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.
from .models import Book


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()  # 存入数据库
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)  # 使用JSON格式来包装数据


@require_http_methods(['GET'])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()  # 从数据库中查询会得到符合条件的model对象的列表？
        response['list'] = json.loads(serializers.serialize("json", books))  # 这里将得到的books列表序列化变成json格式对象
        # json.load()是将json格式数据转换为字典
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)




