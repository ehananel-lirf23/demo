from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    """创建视图函数，测试视图和路由匹配"""
    # param：  request: HttpRequest类型对象, 表示请求报文信息
    # return: response
    # HttpResponse类型的对象, 表示响应报文信息
    return HttpResponse("hello world")
