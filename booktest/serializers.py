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
