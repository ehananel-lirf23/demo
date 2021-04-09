from django.shortcuts import render, reverse
from django.http.response import HttpResponse


def redirect_index(request):
    """user中反向解析"""
    print(reverse("users:index"))
    return HttpResponse("redirect_index")


def index(request):
    """创建视图函数，测试视图和路由匹配"""
    # param：  request: HttpRequest类型对象, 表示请求报文信息
    # return: response
    # HttpResponse类型的对象, 表示响应报文信息
    return HttpResponse("hello world")


def say(request):
    return HttpResponse("say!")


def say_hello(request):
    return HttpResponse("say hello")


