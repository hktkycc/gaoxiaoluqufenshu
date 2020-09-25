# -*- coding: utf-8 -*-
import xlwt
import requests
import json
import time

school_name=[]
school_area=[]
school_score=[]
sp_name=[]
sp_batch=[]
sp_level=[]
sp_score=[]

school_x=0

f = xlwt.Workbook()
sheet1 = f.add_sheet('test', cell_overwrite_ok=True)

for i in range(1001,1300):
    try:
        url = 'https://static-data.eol.cn/www/2.0/school/'
        test = str(i)
        url = url + test + '/info.json'

        res = requests.get(url=url)
        time.sleep(3)

        text = res.text
        jsontext=json.loads(text)
        school_name = jsontext['data']['name']
        school_area = jsontext['data']['area']
        school_score = jsontext['data']['pro_type_min']['61'][0]['type']['1']
        print(i)

        if float(school_score)>=460 and float(school_score)<=500:
            surl = 'https://static-data.eol.cn/www/2.0/schoolspecialindex/2019/'
            surl = surl + test+ '/61/1/1.json'
            time.sleep(1)
            sres = requests.get(url=surl)
            stext = sres.text
            jstext=json.loads(stext)
            school_x += 1
            print(school_name)
            print(float(school_score))
            test_data = [[school_name,school_area,school_score]]
            for m in range(len(test_data)):
                t = test_data[m]
                for j in range(len(t)):
                    sheet1.write((school_x-1)*10, j, t[j])

            for index in range(0,9):
                sp_name = jstext['data']['item'][index]['spname']
                sp_batch = jstext['data']['item'][index]['local_batch_name']
                sp_level = jstext['data']['item'][index]['level2_name']
                sp_score = jstext['data']['item'][index]['min']
                print(sp_name,sp_batch,sp_level,sp_score)
                stest_data = [[sp_name,sp_batch,sp_level,sp_score]]
                for m in range(len(stest_data)):
                    t = stest_data[m]
                    for j in range(len(t)):
                        sheet1.write((school_x-1)*10+index, j+3, t[j])
    except:
        i = i + 1

f.save("d:\\test.xls")
