from django.db import models
# Create your models here.
# 购物车模块下有2张表:
# 订单信息表和订单下的商品数据


# 订单信息表
class OrderInfo(models.Model):
    status = (
        (1, '待付款'),
        (2, '待发货'),
        (3, '已发货'),
        (4, '已完成'),
    )
    # 订单编号
    order_id = models.CharField(max_length=100)
    # 收货人地址
    order_addr = models.CharField(max_length=100)
    # 收货人姓名
    order_recv = models.CharField(max_length=50)
    # 收货人电话
    order_tele = models.CharField(max_length=11)
    # 运费
    order_fee = models.IntegerField(default=10)
    # 备注信息
    order_extra = models.CharField(max_length=200)
    # 订单状态
    order_status = models.IntegerField(default=1, choices=status)
    # 订单创建时间
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id


# 订单下的商品模型 （一个订单有多个商品）
class OrderGoods(models.Model):
    # 所属商品
    goods_info = models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE)

    # 商品数量
    goods_num = models.IntegerField()

    # 商品所属订单
    goods_order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE)


