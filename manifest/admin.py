from django.contrib import admin

# Register your models here.
from manifest.models import InputRepository,ProductDetail

# class InputRepositoryInline(admin.TabularInline):
#     list_display = ('input_date', 'supply_company', 'input_name', 'input_car_num', 'input_weight', 'input_actual_weight', 'input_discount_weight', 'input_time', 'input_price', 'input_amount', 'amount_paid', 'amount_not_paid', 'amount_discount', 'confirm', 'note')
#     model = InputRepository


class InputRepositoryAdmin(admin.ModelAdmin):
    list_display = ('input_date', 'supply_company', 'input_name', 'input_car_num', 'input_weight', 'input_actual_weight', 'input_discount_weight', 'input_time', 'input_price', 'input_amount', 'amount_paid', 'amount_not_paid', 'amount_discount', 'confirm', 'note')
    # 激活过滤器，这个很有用
    list_filter = ('input_date', 'supply_company')
    search_fields = ('supply_company','input_car_num','input_weight','note')
    ordering = ('-input_date',)
    date_hierarchy = 'input_date'    # 详细时间分层筛选

class ProductDetailAdmin(admin.ModelAdmin):
    list_display=('prod_date', 'prod_name', 'area_code', 'floor_num', 'area_code2', 'floor_num2', 'construction_site', 'jiaozhufangshi', 'strength_grade', 'total_sum', 'sum_car_count', 'begin_time', 'end_time', 'cement_content', 'medium_sand_content', 'silver_sand_content', 'cobblestone_content', 'flyash_content', 'water_reducer_content', 'breeze_content', 'Harborsandy_content', 'lushan_content', 'kuangjiang_content')
    list_filter = ('prod_date', 'prod_name')
    search_fields = ('prod_name','area_code','floor_num','construction_site','jiaozhufangshi')
    ordering = ('-prod_date',)
    date_hierarchy = 'prod_date'    # 详细时间分层筛选

admin.site.register(InputRepository, InputRepositoryAdmin)

admin.site.register(ProductDetail, ProductDetailAdmin)

admin.site.site_header = '入库存档'
admin.site.site_title = 'admin'