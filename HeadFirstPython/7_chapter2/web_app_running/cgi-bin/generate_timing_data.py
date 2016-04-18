#! /usr/local/bin/python3
# coding=utf-8

import cgi

# 启动Python的CGI跟踪
import cgitb
cgitb.enable()

import athletemodel
import yate

# 从模型中,获取所有运动员列表(数据结构--字典)
athletes = athletemodel.get_from_store()

# 处理选手数据
form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))    
print(yate.header("Athlete: " + athlete_name + ", DOB: " + athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))

# 将3个时间转换为一个无序HTML列表
# top_three_times加上了@property,所以变成了属性,调用不加()
print(yate.u_list(athletes[athlete_name].top3))

# 最下面的两个链接,一个返回首页,一个返回上一页重新选择
print(yate.include_footer({"Home": "/index.html", "Select another athlete": "generate_list.py"}))

