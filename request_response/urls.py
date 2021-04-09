from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather1),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather1),
    url(r'^str/$', views.get_query_string),
    url(r'^get_form/$', views.get_form),
    url(r'^get_json/$', views.get_json),
    url(r'^get_head/$', views.get_request_head),
    url(r'^', views.index),  # / 首页添加
]