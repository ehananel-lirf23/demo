from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # 获取列表数据/新增
    # url(r'^books/$', views.BooksAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),

    # 定义获取所有图书的接口
    # url(r'^books/$', views.BooksAPIView.as_view()),

    # # 定义获取所有图书
    # url(r'^books/$', views.BookListView.as_view()),
    # # 定义获取单一图书
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),

    # 定义获取所有图书   #  BookViewSet 路由到视图集上   视图集上的as_view 不再是之前的，这可以传参数
    url(r'^books/$', views.BookViewSet.as_view({'get': 'list'})),
    # 定义获取单一图书  #  视图集上的as_view 不再是之前的，这可以传参数
    url(r'^books/(?P<pk>\d+)/$', views.BookViewSet.as_view({'get': 'retrieve'})),


]

# 创建 路由器 对象
# router = DefaultRouter()
# # 注册路由  books注册 到路由器身上
# router.register(r'books', views.BookAPIViewSet)
# # 把路由器对象的url  追加到urlpatterns
# urlpatterns += router.urls
