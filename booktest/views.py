"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
"""
from django.views.generic import View
from django.http.response import JsonResponse, HttpResponse
import json
from rest_framework.viewsets import ModelViewSet

from .models import BookInfo
# from .serializers import BookInfoModelSerializers
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from booktest.models import BookInfo, HeroInfo

"""序列化单个模型对象"""
# 获取模型数据
# 创建序列化器并完成序列化  # shell 启动 测试
book = BookInfo.objects.get(id=1)
serializer = BookInfoSerializer(book)
serializer.data  # {'id': 1, 'btitle': '射雕英雄传0', 'bpub_date': '1980-05-01', 'bread': 12, 'bcomment': 34, 'image': None}

"""序列化多个模型对象"""
# book = BookInfo.objects.all()
# serializer = BookInfoSerializer(instance=book, many=True)
# serializer.data

#  ========================
# 关联对象嵌套序列化！！
hero = HeroInfo.objects.get(id=1)
serializer_hero = HeroInfoSerializer(instance=hero)
serializer_hero.data


"""反序列化"""
# 新建
data = {'btitle': 'django三国演义', 'bpub_date': '1996-5-1', 'bcomment': 10, 'bread': 30}
serializer = BookInfoSerializer(data=data)  # 新建 没有参数instance，看重写的create方法 只传入一个参数
# serializer.is_valid()  # 返回布尔值
serializer.is_valid(raise_exception=True)  # 如果出现异常自动抛出
# serializer.errors  # is_valid 返回 False,看错误信息
# serializer.validated_data  # OrderedDict([('btitle', '三国演义'), ('bpub_date', datetime.date(1996, 5, 1))])
serializer.save()  # 执行继承的方法 实质 选择方法(update/create 方法里保存到数据库)

# 更新
book = BookInfo.objects.get(id=9)
data = {'btitle': '大国django三国演义', 'bpub_date': '1996-6-6', 'bcomment': 10, 'bread': 30}
serializer = BookInfoSerializer(instance=book, data=data)
serializer.is_valid(raise_exception=True)
serializer.save()  # 序列化中的saexitve实质 依靠方法模型自身的save()


# class BookAPIViewSet(ModelViewSet):
#     """定义视图集完成五个接口"""
#
#     # 指定查询集
#     queryset = BookInfo.objects.all()
#
#     # 指定序列化器
#     serializer_class = BookInfoModelSerializers


# class BooksAPIView(View):
#     """获取所有和新增"""
#
#     def get(self, request):
#         """查询所有图书"""
#         # 1.查询所有图书模型数据
#         books = BookInfo.objects.all()
#         book_dict_list = []  # 保存图书字典
#         for book in books:
#             book_dict = {
#                 'id': book.id,
#                 'btitle': book.btitle,
#                 'bpub_date': book.bpub_date,
#                 'bread': book.bread,
#                 'bcomment': book.bcomment,
#             }
#             book_dict_list.append(book_dict)
#         return JsonResponse(book_dict_list, safe=False)  # safe 默认是True 设置safe=False，不安全，因为传列表里面有字典。
#
#     def post(self, request):
#         """新增书籍"""
#         # 1.提取请求体中的数据
#         json_str_bytes = request.body
#         json_str = json_str_bytes.decode('utf8')
#         json_dict = json.loads(json_str)
#         # 此处省略数据的校验
#         # 2.创建模型对象并保存到数据
#         book = BookInfo.objects.create(
#             btitle=json_dict['btitle'],
#             bpub_date=json_dict['bpub_date'],
#         )
#         # 把模型转换成字典
#         book_dict = {
#             'bcomment': book.bcomment,
#             'bread': book.bread,
#             'bpub_date': book.bpub_date,
#             'id': book.id,
#             'btitle': book.btitle,
#         }
#         # 3.响应
#         return JsonResponse(book_dict, status=201)  # 新增状态码 201
#
#
# class BookAPIView(View):
#     """更新/查单一/删除"""
#
#     def get(self, request, pk):  # 查单一, 正则组规定变量名为pk  方法接收
#         """查询指定的某本书"""
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({'message': 'pk不存在'}, status=400)
#         # 2.把模型转字典
#         book_dict = {
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bcomment': book.bcomment,
#             'bread': book.bread,
#         }
#         return JsonResponse(book_dict)
#
#     def put(self, request, pk):  # 更新修改
#         json_str_bytes = request.body
#         json_str = json_str_bytes.decode('utf8')
#         json_dict = json.loads(json_str)
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({'message': 'pk不存在'}, status=400)
#
#         # 3.更新
#         book.btitle = json_dict['btitle']
#         book.bpub_date = json_dict['bpub_date']
#         book.save()  # 更新 注意更新到 数据库
#         # 且 前后端分类 要 将修改后数据 返回给前端
#         book_dict = {
#             'id': book.id,
#             'btitle': book.btitle,
#             'bpub_date': book.bpub_date,
#             'bcomment': book.bcomment,
#             'bread': book.bread,
#         }
#         return JsonResponse(book_dict)
#
#     def delete(self, request, pk):  # 删除
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return HttpResponse({'message': 'pk不存在'}, status=400)
#         if not book:
#             return HttpResponse({'message': 'pk不存在'}, status=400)
#         book.delete()  # 对象删除  与 查询集的删除 不同一个方法
#         return HttpResponse(status=204)  # 204删除状态码
