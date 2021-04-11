from django.shortcuts import render

# Create your views here.
from booktest.models import BookInfo, HeroInfo
from datetime import date
from django.db.models import F, Q, Sum, Avg  # 导入 F Q 对象 ，聚合Sum, Avg
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


# F对象
# 1.查询阅读量大于评论量的书籍
BookInfo.objects.filter(bread__gt=F('bcomment'))
# 2.查询阅读量大于2倍评论量的书籍
BookInfo.objects.filter(bread__gt=F('bcomment' * 2))

# Q对象
# 1.查询阅读量大于20，并且编号小于3的图书。
# BookInfo.objects.filter(bread__gt=20).filter(id__lt=3)  # 不这样用
# BookInfo.objects.filter(Q(bread__gt=20) & Q(id__lt=3))  # 不这样用 直接
BookInfo.objects.filter(bread__gt=20, id__lt=3)
# 2.查询阅读量大于20，或编号小于3的图书  注意Q一个属性Bo
BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
# 3.查询编号不等于3的书籍
BookInfo.objects.filter(~Q(id=3))  # BookInfo.objects.exclude(id=3)

# 聚合函数
# 1.统计总的阅读量
BookInfo.objects.aggregate(Sum('bread'))
# 2.统计平均的阅读量
BookInfo.objects.aggregate(Avg('bread'))

# 排序
BookInfo.objects.all().order_by('bread')  # 升序
BookInfo.objects.all().order_by('-bread')  # 降序

########################################################

# 基础关联查询
# 1.一查多：查询编号为1的图书中所有人物信息
book = BookInfo.objects.get(id=1)  # 获取书本对象
# 被外键的一方 自动生成 :类名小写_set
book.heroinfo_set.all()  # 查处属于该书本的所有英雄(heroinfo_set在模型中没有定义，是由多方 定义外键的时候 一的方自动生成的关系字段)

# 2.多查一：查询编号为1的英雄出自的书籍
hero = HeroInfo.objects.get(id=1)  # 获取英雄对象
hero.hbook  # 定义有关系字段 直接 使用


# 关联过滤查询 重点
# 1.多查一：查询书籍中人物的描述包含"降龙"的书籍
BookInfo.objects.filter(heroinfo__hcomment__contains='降龙')  # 多查一，filter里的条件 是用类名小写
# 2.一查多：查询书名为"天龙八部"的所有人物信息
HeroInfo.objects.filter(hbook__btitle='天龙八部')
