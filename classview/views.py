from django.shortcuts import render
from django.views.generic import View  # generic通用类 导入View
from django.http.response import HttpResponse


# Create your views here.
class DemoView(View):
    """类视图，继承于 generic通用类的View类"""

    #  处理get， 注意固定get固定写法 除非 重写 里面的定义
    def get(self, request):  # request 必须 相当于函数视图
        """get请求业务逻辑"""
        return HttpResponse("get请求业务逻辑")

    def post(self, request):
        """post请求业务逻辑"""
        return HttpResponse("post请求业务逻辑")
