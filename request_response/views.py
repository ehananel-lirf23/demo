from django.shortcuts import render
from django.http.response import HttpResponse
import json


# url(r'^weather/([a-z]+)/(\d{4})/$', views.weather)
# 注意urls 正则必须有 且位置参数 有顺序， 位置参数传参
def weather1(request, city, year):
    """提取正则组中的位置参数"""
    print(city)
    print(year)
    return HttpResponse('正则分组获 ^weather1/([a-z]+)/(\d{4}/)$')


# weather/？P<city>([a-z]+)/(?P<year>\d{4}/)
# 正则匹配分组有别名的形式 相当于 关键字传参
def weather2(request, year, city):
    """提取正则组中关键字参数"""
    print(city)
    print(year)
    return HttpResponse("正则分组取别名 ^weather2/？P<city>([a-z]+)/(?P<year>\d{4}/)$")


# str/?a=10&b=20&a=30
def get_query_string(request):
    """演示获取查询字符串数据"""
    # 注意点:request.GET 后面的GET只是一个属性而已和请求方法无关
    a = request.GET.get("a")
    b = request.GET.get("b")
    a_list = request.GET.getlist("a")
    str = "%s %s %s" % (a, b, a_list)  # 30 20 ['10', '30']
    return HttpResponse(str)


# POST get_form/ 表单提交 post 请求
def get_form(request):
    """演示获取表单数据"""
    like = request.POST.get("like")  # 多选 get 一个也只是得到最后一个
    print(like)
    b = request.POST.get("b")
    like_list = request.POST.getlist("like")
    s = "%s %s %s" % (like, b, like_list)  # 获取列表
    return HttpResponse("get_form")


def get_json(request):
    """获取json数据"""
    json_str_bytes = request.body  # 获取出来是json字符串的字节类型
    json_str = json_str_bytes.decode()  # 把字节类型转成字符串
    json_dict = json.loads(json_str)  # 把字符串的json字典转你json字典
    print(json_dict["a"])
    print(json_dict["b"])
    return HttpResponse(b"get_json success!")

