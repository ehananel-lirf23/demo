"""
GET     /books/         提供所有记录
POST    /books/         新增一条记录
GET     /books/<pk>/    提供指定id的记录
PUT     /books/<pk>/    修改指定id的记录
DELETE  /books/<pk>/    删除指定id的记录

响应数据    JSON
"""
from django.views.generic import View


class BooksAPIView(View):
    """获取所有和新增"""

    def get(self, request):
        pass

    def post(self, request):
        pass


class BookAPIView(View):
    """更新/查单一/删除"""

    def get(self, request):  # 查单一
        pass

    def put(self, request):  # 更新修改
        pass

    def push(self, request):  # 删除
        pass