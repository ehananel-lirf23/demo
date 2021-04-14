from rest_framework import serializers

from .views import BookInfo  # 良好格式：导第三方的模块 和 自建模块 隔开一行


class BookInfoModelSerializers(serializers.ModelSerializer):
    """定义序列化器"""
    class Meta:
        model = BookInfo  # 给序列化器 指定 字段从那个模型去映射
        fields = '__all__'  # 指定 需要从模型中 映射 哪些字段 (自动生成 对应的 序列化类器)
        # fields = ['id', 'btitle']
