from django.conf.urls import url

from . import views

urlpatterns = [
    # 获取列表数据/新增
    url(r'^books/$', views.BooksAPIView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
]
