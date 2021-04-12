"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
"""
from django.views.generic import View
from .models import BookInfo
from django.http.response import JsonResponse, HttpResponse
import json


class BooksAPIView(View):
    """获取所有和新增"""

    def get(self, request):
        """查询所有图书"""
        # 1.查询所有图书模型数据
        books = BookInfo.objects.all()
        book_dict_list = []  # 保存图书字典
        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
            }
            book_dict_list.append(book_dict)
        return JsonResponse(book_dict_list, safe=False)  # safe 默认是True 设置safe=False，不安全，因为传列表里面有字典。

    def post(self, request):
        """新增书籍"""
        # 1.提取请求体中的数据
        json_str_bytes = request.body
        json_str = json_str_bytes.decode('utf8')
        json_dict = json.loads(json_str)
        # 此处省略数据的校验
        # 2.创建模型对象并保存到数据
        book = BookInfo.objects.create(
            btitle=json_dict['btitle'],
            bpub_date=json_dict['bpub_date'],
        )
        # 把模型转换成字典
        book_dict = {
            'bcomment': book.bcomment,
            'bread': book.bread,
            'bpub_date': book.bpub_date,
            'id': book.id,
            'btitle': book.btitle,
        }
        # 3.响应
        return JsonResponse(book_dict, status=201)  # 新增状态码 201


class BookAPIView(View):
    """更新/查单一/删除"""

    def get(self, request):  # 查单一
        pass

    def put(self, request):  # 更新修改
        pass

    def push(self, request):  # 删除
        pass
