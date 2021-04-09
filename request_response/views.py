from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
import json
from django.shortcuts import reverse


# GET /cookie_demo/
def cookie_demo(request):
    """演示cookie读写"""
    # 设置cookie
    response = HttpResponse("cookie_demo")
    # 设置cookie   set_cookie(key, value, 过期时间单秒(秒))
    response.set_cookie("name", "jack", max_age=3600)
    # 读取cookie,cookie 存在浏览器端
    print(request.COOKIES.get("name"))
    return response


# ===============================


def redirect_index(request):
    """重定向到index"""
    # 起了命名空间 那就必须格式：  命名空间：路由名
    return redirect(reverse('request_response:index'))


# GET /json_response/
def json_response(request):
    """演示响应json数据"""
    # JSON字典中的引号必须要用双引号
    json_dict = {
        "name": "jack",
        "age": 20
    }
    # JsonResponse 继承 HttpResponse 这个返回主要用来接受json字典的形式， 自动处理 得到响应体 还是通过HttpResponse返回
    # 源码；kwargs.setdefault('content_type', 'application/json')
    # 源码；data = json.dumps(data, cls=encoder, **json_dumps_params)
    # 源码；super(JsonResponse, self).__init__(content=data, **kwargs)
    return JsonResponse(json_dict)


def response_demo(request):
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # 必须传递响应体,其它可以用默认的
    return HttpResponse('response_demo', content_type='text/plain', status=201)


# =================================================================


def index(request):
    """index"""
    # 命名空间：路由名   无命令空间容易与其他子应用重叠，执行结果会是靠近项目根路径的，所以一般都设定一个命名空间 一般与子应用同名
    # print(reverse("index"))
    return HttpResponse("django index")


def get_request_head(request):
    """演示获取请求头信息"""
    print(request.META.get('CONTENT_TYPE'))  # 注 大写 才能获取
    print(request.user)  # AnonymousUser    未登录  默认是匿名用户
    return HttpResponse("get_request_head")


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

