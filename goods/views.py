from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from goods.models import GoodsCategory, GoodsInfo


def index(request):
    # 取所有分类
    categories = GoodsCategory.objects.all()

    # 取每个分类中的后4个商品
    for cag in categories:
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 取购物车中所有商品的信息
    # 新建列表用于存放商品列表
    cart_goods_list = list()
    # 设置商品默认总数量
    cart_goods_count = 0

    for goods_id, goods_num in request.COOKIES.items():
        # 遍历请求中的cookie 判断是否为商品id
        if not goods_id.isdigit():
            continue
        # 用商品id去数据库搜索 匹配商品并添加到cart_goods_list中
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 将商品的数量添加到商品属性中
        cart_goods.goods_num = goods_num
        # 添加到cart_goods_list中
        cart_goods_list.append(cart_goods)
        # 计算所有商品的总数量
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'index.html', {
        'categories': categories,
        'cart_goods_list': cart_goods_list,
        'cart_goods_count': cart_goods_count,
    })


def detail(request):
    # 商品类型
    categories = GoodsCategory.objects.all()
    # 取购物车里的数据
    # 空数组用于存放购物车中的商品列表
    cart_goods_list = list()
    # 购物车中商品总数量 初始值为0
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 判断是否为商品id
        if not goods_id.isdigit():
            continue
        # 通过商品id查询商品的信息
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 将商品的数量存放在商品信息里的goods_num属性中
        cart_goods.goods_num = goods_num
        # 将商品信息添加到购物车商品列表中
        cart_goods_list.append(cart_goods)
        # 将当前商品数量添加到购物车商品总数量中
        cart_goods_count = cart_goods_count + int(goods_num)

    # 当前商品的详细数据
    goods_id = request.GET.get('id', 2)
    goods_data = GoodsInfo.objects.get(id=goods_id)

    return render(request, 'detail.html', {
        'categories': categories,
        'cart_goods_list': cart_goods_list,
        'cart_goods_count': cart_goods_count,
        'goods_data': goods_data
    })


def goods(request):
    """类目下的商品列表"""
    # 当前类目的id
    cag_id = request.GET.get('cag', 1)
    # 获取当前类目下的对象
    current_cag = GoodsCategory.objects.get(id=cag_id)
    # 当前页码id
    page_id = request.GET.get('page', 1)


    # 当前类目下的所有商品数据
    # goods_data = GoodsInfo.objects.get(goods_cag_id=cag_id)
    # 用当前类目的对象调用他下面的表的_set属性
    goods_data = current_cag.goodsinfo_set.all()
    paginator = Paginator(goods_data, 12)
    page_data = paginator.page(page_id)
    # 获取所有商品分类
    categories = GoodsCategory.objects.all()

    cart_goods_list = list()
    cart_goods_count = 0
    # 购物车里的商品信息
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        else:
            cart_goods = GoodsInfo.objects.get(id=goods_id)
            cart_goods.goods_num = goods_num
            cart_goods_list.append(cart_goods)
            cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods.html', {
        'current_cag': current_cag,
        'goods_data': page_data,
        'categories': categories,
        'cart_goods_list': cart_goods_list,
        'cart_goods_count': cart_goods_count,
        'paginator': paginator,
        'cag_id': cag_id,
    })


def test(request):
    # a = 1/0
    return render(request, 'test.html', {'name': '张三', 'age': 28})
