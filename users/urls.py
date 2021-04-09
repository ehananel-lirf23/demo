# 定义子应用的所有路由
from django.conf.urls import url
from . import views


# 注意点： urlpatterns 必须是列表 不能是字典定义 。
urlpatterns = [
    # 定义路由时,必须要有严格的开始和结束 ^ $
    # url(r'^index/$', views.index),

    url(r'^user/index/$', views.index, name="index"),
    url(r'^user/say/$', views.say),
    url(r'^user/sayHello/$', views.say_hello),
    url(r'^user/redirect_index/$', views.redirect_index),
]

