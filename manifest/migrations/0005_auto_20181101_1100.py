# Generated by Django 2.1.2 on 2018-11-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manifest', '0004_auto_20181101_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='area_code2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='区号2'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='construction_site',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='施工部位'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='floor_num2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='楼号2'),
        ),
    ]
