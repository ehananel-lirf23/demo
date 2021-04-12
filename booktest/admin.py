from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo

# 注册模型 在后台 可以操作
admin.site.register(BookInfo)  # 在admin站点中注册模型
admin.site.register(HeroInfo)
