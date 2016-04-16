# coding=utf-8
#!/usr/local/bin/python3

import athletemodel
import yate
import glob

# 查询一个文件列表
data_files = glob.glob("data/*.txt")

# 由数据文件创建一个选手字典
athletes = athletemodel.put_to_store(data_files)

print (yate.start_response())
print (yate.include_header("Coach Kelly's List of Athletes"))
print (yate.start_form("generate_timing_data.py"))
print (yate.para("Selete an athlete from the list to work with: "))

for each_athlete in athletes:
    print (yate.radio_button("which_athlete", athletes[each_athlete].name))

print (yate.end_form("Select"))
print (yate.include_footer({"Home": "/index.html"}))