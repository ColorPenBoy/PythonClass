# coding=utf-8

import  athletemodel

print ('-----------取出资源文件,存入pickle中---------------')
# 资源文件在data文件夹下,需要添加上路径
the_files = ['data/sarah.txt', 'data/james.txt', 'data/mikey.txt', 'data/julie.txt']

data = athletemodel.put_to_store(the_files)

print ('---------打印资源文件-----------------')

print (data)

for each_athlete in  data:
    print (data[each_athlete].name + ' ' + data[each_athlete].dob)


print ('------------从pickle中取出--------------')

data_copy = athletemodel.get_from_store()

for each_athlete in  data_copy:
    print (data[each_athlete].name + ' ' + data[each_athlete].dob)