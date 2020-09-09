from django.db import models


# Create your models here.
# goods的数据表对应2张表

# 商品分类的信息 1个分类下面可以对应多个商品:
class GoodsCategory(models.Model):
    # 定义3个字段
    # 分类的名称  char类型必须指定最大长度 max_length
    cag_name = models.CharField(max_length=30)

    # 分类的css样式名
    cag_css = models.CharField(max_length=20)

    # 分类的图片 （需要指定upload_to 存放在数据库的图片路径）
    cag_img = models.ImageField(upload_to='cag')

    def __str__(self):
        return self.cag_name

# 商品的信息
class GoodsInfo(models.Model):
    # 商品名字
    goods_name = models.CharField(max_length=100, verbose_name='商品名称')

    # 商品价格
    goods_price = models.IntegerField(default=0, verbose_name='商品价格')

    # 商品描述
    goods_desc = models.CharField(max_length=2000, verbose_name='商品描述')

    # 商品图片
    goods_img = models.ImageField(upload_to='goods', verbose_name='商品图片')

    # 所属分类
    goods_cag = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE, verbose_name='所属分类')

    def __str__(self):
        return self.goods_name
