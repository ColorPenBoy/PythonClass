# PythonClass
本仓库记录零基础学习Python的全过程

Python3

IDEL

table（另类的数组，功能远远强大于数组） - 列表的功能是用来处理数据，强大的列表，可以存放任何类型的数据，字符串、数字甚至是文件，这些都可以混合存放，table也可以嵌套table。

函数 def methodName(parameter)

BIF - 内置函数
组Suite - Python代码块，通过缩进指示分组。

name space - 命名空间

[PYPI网站](http://pypi.python.org)

#####本地发布模块
python3 setup.py sdist
#####模块安装在本地
sudo python3 setup.py instal

#####注册pypi账号
python3 setup.py register

#####发布模块
python3 setup.py sdist upload


####字典(Dict的key必须是不可变对象)
通过```'Key' in Dictonary```或者```Dictionary.get('Key')``` 判断Dictionary中是否存在Key这个键。

删除 -> pop(key)


|   list  |   dict   |
| ----    | ------   |
|查找和插入的时间随着元素的增加而增加；|查找和插入的速度极快，不会随着key的增加而变慢；|
| 占用空间小，浪费内存很少。| 需要占用大量的内存，内存浪费多。|


####Set（不可以放入可变对象） -> Key的集合，没有重复的Key
* 重复元素被自动过滤
* add -> 添加
* remove -> 删除

