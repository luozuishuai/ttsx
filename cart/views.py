import time

from cart.models import OrderInfo, OrderGoods
from django.shortcuts import render, redirect

# Create your views here.
from goods.models import GoodsInfo


def add_cart(request):
    """添加到购物车"""
    # 需要获取当前商品id
    goods_id = request.GET.get('id', '')

    if goods_id.isdigit:
        # 配置返回的页面
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        # 查找cookies中有没有当前商品id：
        goods_count = request.COOKIES.get(goods_id)
        # 如果有该商品 则+1
        if goods_count:
            goods_count = int(goods_count) + 1
        # 如果没有 则将数量设置为1
        else:
            goods_count = 1
        # 把商品id和数量添加到cookie中
        response.set_cookie(goods_id, goods_count)

        return response


def show_cart(request):
    """购物车页面"""
    # 需要从cookie中查询购物车数据
    # 购物车中商品总数量
    # 购物车中商品总金额
    cart_goods_list = list()
    cart_goods_count = 0
    total_need_pay = 0

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 单项商品的金额小结
        cart_goods.goods_need_pay = cart_goods.goods_price * int(goods_num)
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)
        # 所有商品总金额
        total_need_pay = total_need_pay + cart_goods.goods_need_pay

    return render(request, 'cart.html', {
        'cart_goods_list': cart_goods_list,
        'cart_goods_count': cart_goods_count,
        'total_need_pay': total_need_pay,
    })


def remove_cart(request):
    """从cookie中删除购物车中的商品"""
    goods_id = request.GET.get('id', '')
    if goods_id.isdigit:
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        response.delete_cookie(goods_id)

        return response


def place_order(request):
    cart_goods_list = list()
    cart_goods_count = 0
    cart_goods_total_money = 0

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 单个商品的数量
        cart_goods.goods_num = int(goods_num)
        # 单个商品的金额小结
        cart_goods.goods_money = int(goods_num) * cart_goods.goods_price
        cart_goods_list.append(cart_goods)
        # 购物车商品的累计总个数
        cart_goods_count = cart_goods_count + int(goods_num)
        # 购物车商品的累计总金额
        cart_goods_total_money = cart_goods_total_money + cart_goods.goods_money

    return render(request, 'place_order.html', {
        'cart_goods_list': cart_goods_list,
        'cart_goods_count': cart_goods_count,
        'cart_goods_total_money': cart_goods_total_money,
    })


def submit_order(request):
    # 先获取用户填写的信息
    addr = request.POST.get('addr', '')
    recv = request.POST.get('recv', '')
    tele = request.POST.get('tele')
    extra = request.POST.get('extra')

    # 将用户填写的信息保存到数据库
    order_info = OrderInfo()
    order_info.order_addr = addr
    order_info.order_extra = extra
    order_info.order_recv = recv
    order_info.order_tele = tele
    order_info.order_id = str((int(round(time.time() * 1000000)))) + str((int(round(time.perf_counter() * 10000))))

    order_info.save()

    # 获取购物车中的信息
    response = redirect('/cart/success/?id=%s' % order_info.order_id)
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)

        # 保存到订单商品信息表格
        order_goods = OrderGoods()
        order_goods.goods_info = cart_goods
        order_goods.goods_num = int(goods_num)
        order_goods.goods_order = order_info

        order_goods.save()
        # 删除购物车中对应的商品
        response.delete_cookie(goods_id)

    return response


def submit_success(request):
    # 取得get到的订单id
    get_id = request.GET.get('id')

    # 查询订单下的所有订单信息
    order_info = OrderInfo.objects.get(order_id=get_id)

    # 查询订单的商品信息
    goods_list = order_info.ordergoods_set.all()

    # 查询订单中商品的个数和价格
    order_total_money = 0
    order_total_count = 0

    for goods in goods_list:
        goods.goods_money = goods.goods_info.goods_price * goods.goods_num
        order_total_money += goods.goods_money
        order_total_count += goods.goods_num

    return render(request, 'success.html', {
        'order_info': order_info,
        'goods_list': goods_list,
        'order_total_money': order_total_money,
        'order_total_count': order_total_count,
    })
