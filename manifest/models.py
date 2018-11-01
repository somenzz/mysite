from django.db import models

# Create your models here.

class InputRepository(models.Model):
    """
    日期     供货单位    物料名称    车牌号    重量（吨）    对方实重    扣吨数
    时间    单价    金额    已付    未付    优惠    核对否    备注
    """
    input_date = models.DateField(verbose_name='日期')
    supply_company = models.CharField(max_length=100,verbose_name='供货单位')
    input_name = models.CharField(max_length=100,verbose_name='物料名称')
    input_car_num = models.CharField(max_length=10,verbose_name='车牌号')
    input_weight = models.FloatField(verbose_name='重量（吨）')
    input_actual_weight = models.FloatField(verbose_name='对方实重',blank =True,null=True)
    input_discount_weight = models.FloatField(verbose_name='扣吨数',blank =True,null=True)
    input_time = models.TimeField(verbose_name='时间')
    input_price = models.FloatField(verbose_name ='单价')
    input_amount = models.FloatField(verbose_name='金额')
    amount_paid = models.FloatField(verbose_name='已付')  # 已付
    amount_not_paid = models.FloatField(verbose_name='未付',blank =True,null=True)  # 未付
    amount_discount = models.FloatField(verbose_name='优惠',blank =True,null=True) # 优惠
    confirm = models.CharField(max_length=50,verbose_name='核对否',blank =True,null=True) #核对否
    note = models.CharField(max_length=200,verbose_name='备注',blank =True,null=True)  #备注

    def __str__(self):
        return f"入库{self.pk}"
    class Meta:
        verbose_name = "入库"
        verbose_name_plural = "入库"





class ProductDetail(models.Model):
    """

    日期	工程名称	区号	楼号	 区号 楼号	施工部位	浇筑方式	强度等级	合计方量	累计车次	开始时间	结束时间
    水泥用量	中砂用量	细砂用量	石子用量	粉煤灰用量	减水剂用量	矿粉用量	港砂	鲁山河沙	砂浆添加剂用量

    """
    prod_date = models.DateField(verbose_name='日期')
    prod_name = models.CharField(max_length=100,verbose_name='工程名称')
    area_code  = models.CharField(max_length=100,verbose_name='区号',blank =True,null=True) #区号
    floor_num = models.CharField(max_length=10,verbose_name='楼号',blank =True,null=True)  #楼号
    area_code2 = models.CharField(max_length=100,verbose_name='区号2',blank =True,null=True)  # 区号
    floor_num2 = models.CharField(max_length=10, verbose_name='楼号2',blank =True,null=True)  # 楼号
    construction_site = models.CharField(max_length=100, verbose_name='施工部位',blank =True,null=True)  # 施工部位
    jiaozhufangshi = models.CharField(max_length=100, verbose_name='浇筑方式')  # 浇筑方式
    strength_grade = models.CharField(max_length=100, verbose_name='强度等级')  # 强度等级
    total_sum = models.FloatField(verbose_name='合计方量')  # 合计方量
    sum_car_count = models.IntegerField(verbose_name='累计车次')
    begin_time = models.TimeField(verbose_name='开始时间')
    end_time = models.TimeField(verbose_name='结束时间',blank =True,null=True)
    cement_content = models.FloatField(verbose_name='水泥用量')  # 水泥用量
    medium_sand_content = models.FloatField(verbose_name='中砂用量')  # 中砂用量
    silver_sand_content = models.FloatField(verbose_name='细砂用量')  # 细砂用量
    cobblestone_content = models.FloatField(verbose_name='石子用量')  # 石子用量
    flyash_content = models.FloatField(verbose_name='粉煤灰用量')  # 粉煤灰用量
    water_reducer_content = models.FloatField(verbose_name='减水剂用量')  # 减水剂用量
    breeze_content = models.FloatField(verbose_name='矿粉用量')  # 矿粉用量
    Harborsandy_content = models.FloatField(verbose_name='港砂')  # 港砂
    lushan_content = models.FloatField(verbose_name='鲁山河沙')  # 鲁山河沙
    kuangjiang_content = models.FloatField(verbose_name='砂浆添加剂用量')  # 砂浆添加剂用量

    class Meta:
        verbose_name = "生产明细"
        verbose_name_plural = "生产明细"

