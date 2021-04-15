from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    # 获取列表数据/新增
    # url(r'^books/$', views.BooksAPIView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
    # 定义获取所有图书的接口
    url(r'^books/$', views.BooksAPIView.as_view()),
]

# 创建 路由器 对象
# router = DefaultRouter()
# # 注册路由  books注册 到路由器身上
# router.register(r'books', views.BookAPIViewSet)
# # 把路由器对象的url  追加到urlpatterns
# urlpatterns += router.urls
