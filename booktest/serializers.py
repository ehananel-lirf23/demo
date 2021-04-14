from rest_framework import serializers


# .views -->  booktest.views   终端测试 识别不了 .views
from booktest.models import BookInfo  # 良好格式：导第三方的模块 和 自建模块 隔开一行


# class BookInfoModelSerializers(serializers.ModelSerializer):
#     """定义序列化器"""
#     class Meta:
#         model = BookInfo  # 给序列化器 指定 字段从那个模型去映射
#         fields = '__all__'  # 指定 需要从模型中 映射 哪些字段 (自动生成 对应的 序列化类器)
#         # fields = ['id', 'btitle']


class BookInfoSerializer(serializers.Serializer):  # Serializer 是  ModelSerializer 父类
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)  # read_only=True 只允许读 即 读出进行序列化
    btitle = serializers.CharField(label='名称', max_length=20)
    # required必传参数 参照 models.py 模型类的字段 未设置可以为null 以及有default
    bpub_date =serializers.DateField(label='发布日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)  # default=0
    image = serializers.ImageField(label='图片', required=False)  # null=True
    # 如果在一的序列器中要序列化多的那一方时,要多加 many=true
    heroinfo_set = serializers.PrimaryKeyRelatedField(label='英雄', read_only=True, many=True)
    # heroinfo_set = serializers.StringRelatedField(label='英雄', read_only=True, many=True)

    # 对单一字段进行额外追加校验逻辑时 固定写法 方法名: validate_字段名()
    def validate_btitle(self, value):  # 注意点 上面的属性定义的时候 校验该变量btible 然后 就会先校验这个方法，然后再到上面继续下一个字段
        if 'django' not in value.lower():
            raise serializers.ValidationError('图书不是关于Django的')
        return value  # 逻辑判断完后 一般原路返回

    # 多个字段 进行比较 验证时 固定写法方法： validate()
    def validate(self, attrs):  # ！！与单个字段 验证  不同的是 这多个字段 报错 不会指定到哪个字段上出错，且是校验以上所有字段定义的类似等条件后才进行校验这个多个字段 校验
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs

    def create(self, validated_data):  # 重写BaseSerializer中定义的方法
        """新建 模型类 对象"""
        # **validated_data 注意两颗心  需要关键字参数  Serializer(instance=None? data=None? **kwargs)
        return BookInfo.objects.create(**validated_data)  # create自动保存到数据库，相当于创建对象完成后  对象.save()
    
    def update(self, instance, validated_data):  # 传入的是参数1：要修改的实例对象， 参数2：校验完后 的 django中有序字典
        """更新，instance为要更新的对象实例"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()  # 更新结束后 保存到数据库
        return instance


class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )

    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描叙信息', max_length=200, required=False,  allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='书籍', read_only=True)  # 只序列化出外键的id
    # hbook = serializers.StringRelatedField(label='书籍', read_only=True)  # 序列化出外键对象的str方法返回值
    hbook = BookInfoSerializer()  # 在序列化外键时,会把外键对应的序列化器中的所有数据充列化出来
