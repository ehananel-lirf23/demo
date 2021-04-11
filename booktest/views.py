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

"""演示基本查询  get  all  count"""
# try:
#     BookInfo.objects.get(id=1)
# except BookInfo.DoesNotExist:
#     print()
# 查询出全部对象 返回的是一个 查询集 [ ]
BookInfo.objects.all()
BookInfo.objects.count()


# 基本条件查询
# 1.查询id为1的书籍
# BookInfo.objects.filter(id__exact=1)  # __exact 直接写 '=' 即可
BookInfo.objects.filter(id=1)

# 2.查询书名包含‘湖’的书籍  like %湖%
BookInfo.objects.filter(btitle__contains='湖')

# 3.查询书名以‘部’结尾的书籍 （endswith 、startswith）like %部  部%
BookInfo.objects.filter(btitle__endswith='部')

# 4.查询书名不为空的书籍
BookInfo.objects.filter(btitle__isnull=False)

# 5.查询编号为2或4的书籍
BookInfo.objects.filter(id__in=[2, 4])

# 6.查询编号大于2的书籍  gt >   gte >=   lt <   lte  <=
BookInfo.objects.filter(id__gt=2)

# 7.查询id不等于3的书籍
BookInfo.objects.exclude(id=3)

# 8.查询1980年发表的书籍
BookInfo.objects.filter(bpub_date__year='1980')

# 9.查询1990年1月1日后发表的书籍
BookInfo.objects.filter(bpub_date__gt='1990-1-1')
