from django.conf.urls import url
from . import views

urlpatterns = [
    # url(路径, 函数视图)
    # as_view() 方法的作用就是将类视图转换成函数视图, 也就是来什么请求方法 执行对象的函数视图
    url(r'^demo_view/$', views.DemoView.as_view()),
]
