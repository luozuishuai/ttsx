"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from goods.views import index, detail, test, goods
from cart.views import add_cart, show_cart, remove_cart, place_order, submit_order, submit_success


urlpatterns = [
    path('admin/', admin.site.urls),
    # 参数1是 匹配的路径的正则表达式 参数2是要访问的视图的函数名
    path('index/', index),                          # 主页
    path('detail/', detail),                        # 详情页
    path('test/', test),                            # 测试
    path('goods/', goods),                          # 商品分类列表页面
    path('cart/add_cart/', add_cart),               # 添加到购物车
    path('cart/show_cart/', show_cart),             # 购物车页面
    path('cart/remove_cart/', remove_cart),         # 从购物车中删除
    path('cart/place_order/', place_order),         # 结算页面
    path('cart/submit_order/', submit_order),       # 订单数据提交逻辑处理
    path('cart/success/', submit_success),   #订单提交成功


]
