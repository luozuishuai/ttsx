from django.contrib import admin

# Register your models here.
from goods.models import GoodsCategory, GoodsInfo


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['goods_name', 'goods_price', 'goods_desc', 'goods_cag']
    list_per_page = 30
    search_fields = ['goods_name', 'goods_price', 'goods_desc', 'goods_cag__cag_name']


class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ['cag_name', 'cag_css']


admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
