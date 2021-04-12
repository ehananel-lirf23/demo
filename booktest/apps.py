from django.apps import AppConfig


class BooktestConfig(AppConfig):
    """配置 子应用 信息"""
    name = 'booktest'  # 加载子应用时,name表示所加载的是那个名字的应用,尽量不要改
    verbose_name = "图书管理系统"  # admin站点上显示子应用的名字
