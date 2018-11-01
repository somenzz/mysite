#encoding=utf-8

import  os
import django
import random
import datetime
from openpyxl import load_workbook

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")



django.setup()


from manifest.models import *

def insertRepos():
    InputRepository_list = []
    for i in range(100):
        t = InputRepository()
        t.input_date= datetime.date(2018,10,random.choice([5,6,7,8,9]))
        t.supply_company = '鲁山河沙'
        t.input_name = '鲁山河沙'
        t.input_car_num = random.choice(['93691','95503','8868','76354'])
        t.input_weight = random.choice([31.06,35.06,41.06,31.96,55.06])
        t.input_time = datetime.datetime.now().time()
        t.input_price = random.choice([180.84, 179.5, 180.3, 182.49, 177.27, 180.9, 183, 181.84])
        t.input_amount = t.input_weight * t.input_price
        t.amount_paid = random.choice([t.input_amount,0])
        t.amount_not_paid = t.input_amount - t.amount_paid
        t.note=f"{random.choice([1,3,4,5,6,7,8])}日"
        InputRepository_list.append(t)

    InputRepository.objects.bulk_create(InputRepository_list)



def insertProd_detail():
    ProductDetail_list = []
    for i in range(100):
        t = ProductDetail()
        t.prod_date= datetime.date(2018,10,random.choice([5,6,7,8,9,10,11,12,13,14]))
        t.prod_name = random.choice(['袁坊环保桶', '杜良项目部', '曲兴项目部', '杜良路面', '杜良环保桶', '杜良外卖',])
        t.area_code = random.choice(['A区', 'B区', 'E区', '村委会', 'C区', '西区', '东区', 'D区', 'F区', '沙盘',])
        t.floor_num = random.choice(['1#','2#','3#','4#'])
        t.construction_site = random.choice(['二次结构', '内粉', '内墙', '外粉', '外墙', '五层构造柱二次结构', '四层二次结构', '七层梁板柱梯天沟', '二层构造柱', '七层天沟', '首层垫层', '窗台压顶', '五层梁板柱', '升降梯基础', '五层梁板柱梯', '七层梁板柱梯', '四层构造柱', '二次结构构造柱', '构造柱', '六层反水', '一层构造柱', '五层楼梯飘窗', '七层楼梯', '六层楼梯', '四层梁板柱梯墙', '三层梁板柱梯墙', '机房层墙柱梁板',])
        t.jiaozhufangshi = random.choice(['自卸', '泵送', '塔吊',])
        t.strength_grade = random.choice([])
        t.total_sum = random.choice([])
        t.sum_car_count = random.choice([])
        t.begin_time = random.choice([])
        t.end_time = random.choice([])
        t.cement_content = random.choice([])
        t.medium_sand_content = random.choice([])
        t.silver_sand_content = random.choice([])
        t.cobblestone_content = random.choice([])
        t.flyash_content = random.choice([])
        t.water_reducer_content = random.choice([])
        t.breeze_content = random.choice([])
        t.Harborsandy_content = random.choice([])
        t.lushan_content = random.choice([])
        t.kuangjiang_content = random.choice([])

        ProductDetail_list.append(t)

    ProductDetail.objects.bulk_create(ProductDetail_list)


def loadExcel_ProductDetail():
    ProductDetail_list = []
    ProductDetail.objects.all().delete()
    wb = load_workbook(r'10月份原材料.xlsx')
    prod_mx = wb.get_sheet_by_name("生产明细")
    for row in prod_mx:
        if row[0].value is None:
            break;
        if row[0].value == '日期':
            continue
        t = ProductDetail()
        t.prod_date = datetime.date(2018, 10, random.choice([5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
        t.prod_name = '-' if row[1].value is None else row[1].value
        t.area_code = row[2].value
        #print(t.area_code)
        t.floor_num = row[3].value

        t.area_code2 = row[4].value
        t.floor_num2 = row[5].value
        t.construction_site = '-' if row[6].value is None else row[6].value
        t.jiaozhufangshi = '-' if row[7].value is None else row[7].value
        t.strength_grade = '-' if row[8].value is None else row[8].value
        t.total_sum = 0 if row[9].value is None else row[9].value
        t.sum_car_count = 0 if row[10].value is None else row[10].value
        t.begin_time = (datetime.datetime.now()-datetime.timedelta(days=2)).time()
        t.end_time = datetime.datetime.now().time()
        t.cement_content = 0 if row[13].value is None else row[13].value
        t.medium_sand_content = 0 if row[15].value is None else row[15].value
        t.silver_sand_content = 0 if row[17].value is None else row[17].value
        t.cobblestone_content = 0 if row[19].value is None else row[19].value
        t.flyash_content = 0 if row[21].value is None else row[21].value
        t.water_reducer_content = 0 if row[23].value is None else row[23].value
        t.breeze_content = 0 if row[25].value is None else row[25].value
        t.Harborsandy_content = 0 if row[27].value is None else row[27].value
        t.lushan_content = 0 if row[29].value is None else row[29].value
        t.kuangjiang_content = 0 if row[31].value is None else row[31].value
        ProductDetail_list.append(t)

    ProductDetail.objects.bulk_create(ProductDetail_list)


        #
        # for cell in row:
        #     print(cell.value,end=' ')
        # print('\n')




if __name__ == '__main__':
    loadExcel_ProductDetail()