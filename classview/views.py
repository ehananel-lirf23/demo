from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View  # generic通用类 导入View
from django.http.response import HttpResponse


# 定义装饰器装饰视图
def my_decorator(view_func):
    """定义装饰器装饰视图"""
    def wrapper(request, *args, **kwargs):
        print('装饰器被调用了')
        print("请求的方法：%s" % request.method)

        # 调用被装饰的视图
        return view_func(request, *args, **kwargs)
    return wrapper


# method_decorator(要被转换装饰器, name=要装饰的方法) 如果写在类的上面时,name参数必须指定,如果写在内部方法上时,name不需要指定
@method_decorator(my_decorator, name='get')  # 指定get 就只是get实例方法 会被装饰
class DemoView(View):
    """类视图，继承于 generic通用类的View类"""
    #  处理get， 注意固定get固定写法 除非 重写 里面的定义
    # #直接装饰到实例方法上 相当于 指定对哪个 视图函数装饰
    @method_decorator(my_decorator)
    def get(self, request):  # request 必须 相当于函数视图
        """get请求业务逻辑"""
        return HttpResponse("get请求业务逻辑")

    def post(self, request):
        """post请求业务逻辑"""
        return HttpResponse("post请求业务逻辑")
