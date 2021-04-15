from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView  # 导入GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ViewSet  # 视图集
from rest_framework import status  # 导入 DRF 提供的状态码 文件

from .models import BookInfo  # 导入模型类
from .serializers import BookInfoSerializer  # 导入 定义的序列化器 Serializer


"""这个是用  APIView   实现的获取列表视图"""
# class BooksAPIView(APIView):
#     """获取所有图书数据"""
#
#     def get(self, request):
#         """request已经不是django中的request 是DRF提供"""
#         # 1.获取所有数据
#         books = BookInfo.objects.all()
#         # Django 视图 的基类 BaseSerializer  def __init__(self, instance=None, data=empty, **kwargs):
#         serializer = BookInfoSerializer(books, many=True)  # many  对象多个/查询集 必须指定True
#         return Response(serializer.data)


"""这个是用  GenericAPIView   实现的获取列表视图"""
# 继承GenericView, 定义list且用于测试， MinXin 其实已经写好这些视图5个  list detail destroy create (继承object) ...
# GenericView 搭配 MinXin 才能起到作用
# class BookListView(GenericAPIView):
#     """获取所有图书数据"""
#     # 1.指定查询集, queryset只是GenericAPIView 是新增加的类属性，不是从 APIView 继承过来
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         """获取所有图书接口"""
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)
#
#
"""这个是用  GenericAPIView   实现的获取详情视图"""
# class BookDetailView(GenericAPIView):
#     #  1.获取要查询的 模型
#     queryset = BookInfo.objects.all()
#     # 2.指定序列化器类
#     serializer_class = BookInfoSerializer
#
#     def get(self, request, pk):
#         """获取单一图书"""
#         # pk 只要传就行 框架里已经定义好 pk 这个参数 接收处理 所以指定id=pk是特定写法
#         book = self.get_object()  # # get_object()方法根据pk参数查找queryset中的数据对象
#         # 3.返回序列化器对象
#         # self.get_serializer_class()  # 返回序列化器 类
#         serializer = self.get_serializer(book)
#         return Response(serializer.data)


"""五个接口实现 未视图集 分两个类 """
class BookListView(ListAPIView, CreateAPIView):  # ListAPIView 继承于 扩展类 ListModelMixin, CreateAPIView
    """查所有/创建"""  # CreateAPIView  继承于  扩展类CreateModelMixin与视图类CreateAPIView(扩展需要它的序列化器，查询集数据)
    # 因为继承 ListAPIView  CreateAPIView 已经自带有
    # 1.指定的查询集
    queryset = BookInfo.objects.all()
    # 2.指定的序列化器类
    serializer_class = BookInfoSerializer


class BookDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    """单一操作 查询/更新/删除"""
    # 1.指定的查询集
    queryset = BookInfo.objects.all()
    # 2.指定的序列化器类
    serializer_class = BookInfoSerializer


class BookViewSet(ViewSet):

    def list(self, request):
        """获取所有图书"""
        qs =BookInfo.objects.all()
        serializer = BookInfoSerializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """获取单一图书"""
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = BookInfoSerializer(book)
        return Response(serializer.data)
