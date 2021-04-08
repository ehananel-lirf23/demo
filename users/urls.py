# 定义子应用的所有路由
from django.conf.urls import url
from . import views


urlpatterns = {
    # 定义路由时,必须要有严格的开始和结束 ^ $
    # url(r'^index/$', views.index),

    url(r'^user/index/$', views.index),
    url(r'^user/say$', views.say),
    url(r'^user/sayHello$', views.say_hello),
}

