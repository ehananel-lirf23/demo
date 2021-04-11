from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo, HeroInfo
from datetime import date

"""演示增加数据  save和create"""
book = BookInfo()  # 创建一个记录对象
book.btitle = '西游记'
book.bpub_date = date(1991, 1, 1)  # date 会转像 下 '199-1-1’
book.bpub_date = "1991-1-1"
book.save()

# 创建对象时候 添加 实例属性
hero1 = HeroInfo(
    hname='孙悟空',
    hgender=1,
    hcomment='72变',
    # hbook_id=book.id
    hbook=book  # 一般使用 这种方式 指定外键 (上面已经实例的对象 赋值到 这个外键hbook实例属性)
)
# 记住要保存到数据库中
hero1.save()  # 实例对象上的方法 实质是 模型类 继承models.Model过来的方法
hero2 = HeroInfo(
    hname='猪八戒',
    hgender=1,
    hbook=book
)
hero2.save()

# 建议使用这种方法  BookInfo.objects.create 创建模型类对象，会自动保存
book2 = BookInfo.objects.create(
    btitle='梦三国',
    bpub_date='2011-11-11',
    bread=10,
    bcomment=10
)

