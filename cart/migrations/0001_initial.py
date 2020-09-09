# Generated by Django 2.2 on 2020-09-08 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('order_addr', models.CharField(max_length=100)),
                ('order_recv', models.CharField(max_length=50)),
                ('order_tele', models.CharField(max_length=11)),
                ('order_fee', models.IntegerField(default=10)),
                ('order_extra', models.CharField(max_length=200)),
                ('order_status', models.IntegerField(choices=[(1, '待付款'), (2, '待发货'), (3, '已发货'), (4, '已完成')], default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField()),
                ('goods_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsInfo')),
                ('goods_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.OrderInfo')),
            ],
        ),
    ]