from django.conf.urls import url
from . import views

urlpatterns = [
    # url(路径, 函数视图)
    # as_view() 方法的作用就是  1.将类视图转换成函数视图, 也就是来什么请求方法 执行对象的函数视图
    # 2.根据请求方法动态分发找到对应的请求实例方法
    url(r'^demo_view/$', views.DemoView.as_view()),  # 注： as_view() 方法

    # url(r'^demo_view/$', views.my_decorator(views.DemoView.as_view())), # 直接在路由的地方 会装饰整个类个视图
]
