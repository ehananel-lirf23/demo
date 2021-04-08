# 定义子应用的所有路由
from django.conf.urls import url
from . import views


urlpatterns = {
    url(r'^index/$', views.index)
}

