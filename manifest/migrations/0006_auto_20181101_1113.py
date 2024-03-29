# Generated by Django 2.1.2 on 2018-11-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manifest', '0005_auto_20181101_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputrepository',
            name='amount_discount',
            field=models.FloatField(blank=True, verbose_name='优惠'),
        ),
        migrations.AlterField(
            model_name='inputrepository',
            name='amount_not_paid',
            field=models.FloatField(blank=True, verbose_name='未付'),
        ),
        migrations.AlterField(
            model_name='inputrepository',
            name='confirm',
            field=models.CharField(blank=True, max_length=50, verbose_name='核对否'),
        ),
        migrations.AlterField(
            model_name='inputrepository',
            name='input_actual_weight',
            field=models.FloatField(blank=True, verbose_name='对方实重'),
        ),
        migrations.AlterField(
            model_name='inputrepository',
            name='input_discount_weight',
            field=models.FloatField(blank=True, verbose_name='扣吨数'),
        ),
        migrations.AlterField(
            model_name='inputrepository',
            name='note',
            field=models.CharField(blank=True, max_length=200, verbose_name='备注'),
        ),
    ]
