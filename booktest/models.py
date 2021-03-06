from django.db import models
# Create your models here.


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # 创建字段：models. 类型 (  参数设置 )       verbose_name 在admin站点中显示的字段名称
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # ImageField 它将来会在站点中自动生成上传图片的表单
    # upload_to 表示上传的文件具体的存储目录,它是基于media/booktest/11.png
    # null=True 如果模型对象的表已经存在,并且已经有记录了,此时后追加的字段必须(要么给个默认值,要么可以为空)
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle

    # 定义一个方法，来显示出 固定格式的 信息
    def pub_date_format(self):
        """返回指定格式的日期"""
        return self.bpub_date.strftime('%Y-%m-%d')  # 日期转换 字符串固定格式 Y 年 m 月  d 日    M小写表示秒
    pub_date_format.short_description = '发布日期'  # 修改它在站点上显示的名字
    pub_date_format.admin_order_field = 'bpub_date'  # 指定此方法依赖那个字段进行排序


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def book_read(self):
        """返回英雄所在书籍的阅读量"""
        return self.hbook.bread
    book_read.short_description = '阅读量'
