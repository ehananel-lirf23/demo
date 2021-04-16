from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView  # 导入GenericAPIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet  # 视图集
from rest_framework import status  # 导入 DRF 提供的状态码 文件
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin  # 导入扩展类
from rest_framework.decorators import action  # DRF包中装饰器模块 导入 action
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.throttling import UserRateThrottle
from rest_framework.filters import OrderingFilter

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


"""继承视图集 ViewSet """
# class BookViewSet(ViewSet):
#
#     def list(self, request):
#         """获取所有图书"""
#         qs =BookInfo.objects.all()
#         serializer = BookInfoSerializer(qs, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         """获取单一图书"""
#         try:
#             book = BookInfo.objects.get(id=pk)
#         except BookInfo.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         serializer = BookInfoSerializer(book)
#         return Response(serializer.data)


"""继承 视图集GenericViewSet 和 扩展类Mixin实现"""
# class BookViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
#     """使用扩展类Mixin"""
#     # 查询集 GenericViewSet类中的 两者搭配
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


class MyPermission(BasePermission):  # 继承于 基础权限管理的类
    # 测试，实际情况是 根据用户信息来设定权限等
    # 是否可以访问数据对象， view表示当前视图， obj为数据对象
    def has_object_permission(self, request, view, obj):
        """控制对obj对象的访问权限，此案例决绝所有对对象的访问"""
        return False  # False表示拒绝访问，这只是测试，没有逻辑判断导致 所有都没有对象访问


"""ModelViewSet 就是 视图集GenericViewSet和扩展类Mixin分别搭配 成的 五种接口"""
class BookViewSet(ModelViewSet):  # 继承已经实现了 基本的五个接口 添加 附加latest update_bread
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    # 来自APIView 继承过来的 认证  局部验证

    # from rest_framework.authentication import SessionAuthentication, BasicAuthentication
    # # 视图中 局部 认证
    # authentication_classes = (SessionAuthentication, BasicAuthentication)

    # 指定访问当前整个类视图时指定的权限
    # permission_classes = [IsAuthenticated, MyPermission]

    # 指定当前整个视图 限流  且按照 用户身份的形式。
    # throttle_classes = [UserRateThrottle, ]

    # 注意写到视图上的请求
    filter_fields = ['btitle', 'bread']  # 指定过滤的字段

    # 添加 附加的 需求接口 action
    @action(['get'], detail=False)  # detail它是来控制router生成路由时,需不需要加pk  路径:books/latest/
    def latest(self, request):
        """获取倒序后的最新书籍数据"""
        book = BookInfo.objects.latest('id')  # latest取到id为最后的对象
        serializer = BookInfoSerializer(book)
        return Response(serializer.data)

    @action(['put'], detail=True)  # detail为True，表示路径:books/{pk}/update_bread/
    def update_bread(self, request, pk):
        """修改书籍阅读量"""
        book = self.get_object()
        book.bread = request.data.get('bread')
        book.save()

        serializer = BookInfoSerializer(book)
        return Response(serializer.data)

