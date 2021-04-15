from rest_framework.views import APIView
from rest_framework.response import Response

from .models import BookInfo  # 导入模型类
from .serializers import BookInfoSerializer  # 导入 定义的序列化器 Serializer


class BooksAPIView(APIView):
    """获取所有图书数据"""

    def get(self, request):
        """request已经不是django中的request 是DRF提供"""
        # 1.获取所有数据
        books = BookInfo.objects.all()
        # Django 视图 的基类 BaseSerializer  def __init__(self, instance=None, data=empty, **kwargs):
        serializer = BookInfoSerializer(books, many=True)  # many  对象多个/查询集 必须指定True
        return Response(serializer.data)
