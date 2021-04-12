from django.contrib import admin

# Register your models here.
from .models import BookInfo, HeroInfo


class HeroInfoStackInLine(admin.TabularInline):  # 继承TabularInline类
    """关联展示信息"""
    model = HeroInfo  # 关联的 类模型
    extra = 1  # 额外的编辑框 数量， 就编辑页面 最后显示多一条可以编辑的框


class BookInfoAdmin(admin.ModelAdmin):
    """BookInfo模型管理类: 管理它在admin站点上的显示信息"""
    list_per_page = 2  # 每页显示多少条数据
    actions_on_bottom = False  # 添加底部动作选项
    actions_on_top = True  # 头部功能选项

    # 控制列表页面展示的那些列, 管理的书籍, 可以是BookInfo模型类 中属性 以及 方法
    list_display = ['id', 'btitle', 'pub_date_format', 'bread', 'bcomment', 'is_delete']
    ordering = ['btitle']

    # fields = ['btitle', 'bpub_date', 'is_delete']  # 控制列表界面所展示的字段,默认全部展示
    # fieldsets 可以设置 详情 列表 界面 的 分类显示 。将属性进行分类
    fieldsets = [
        ['基本', {'fields': ['btitle', 'bpub_date', 'is_delete', 'image']}],
        ['高级', {'fields': ['bread', 'bcomment'], 'classes': ['collapse']}]  # 'classes': ['collapse']} 样式卷起
    ]

    # 在图书的编辑界面到当前这本书关联的英雄都展示出来
    inlines = [HeroInfoStackInLine]


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    """控制HeroInfo 管理类 使用装饰器"""
    list_display = ['id', 'hname', 'hcomment', 'hbook', 'is_delete', 'book_read']
    # 过滤数据
    list_filter = ['hbook']
    # 搜索框
    search_fields = ['hname']


"""用管理类有两种方式:  1.注册参数 2. 装饰器"""

# 注册模型 在后台 可以操作 注册方法
# 1.注册参数 ： 参数2 是管理类, 使用 管理类  来管理注册应用的样式
admin.site.register(BookInfo, BookInfoAdmin)  # 在admin站点中注册模型
# admin.site.register(HeroInfo)  # 装饰器 添加 管理类就 不能使用 注册参数的方式  这两种方式 效果一样 只选其一


admin.site.site_title = "金华书城MIS"  # 网页窗口 顶上的标题
admin.site.site_header = "金华书城"  # 网页左上角的标题头
admin.site.index_title = '欢迎使用金华书城MIS'  # 网页左上角的标题头 下的欢迎语
