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
（先创建一个 setup.py -> 有固定格式的，拿过来一个仿写即可）
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


###函数 -> 最基本的一种代码抽象的方式
```*args```是可变参数，```args```接收的是一个tuple；

```**kw```是关键字参数，kw接收的是一个dict。

递归函数：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

使用递归函数需要注意防止栈溢出。

####Python高级特性
1、切片 -> 适用于 List、Tuple

List[0:3]列表取0~3个元素

List[-2:-1]列表去倒数第2个元素

2、迭代

```for .. in ...```

3、列表生成式
略

4、生成器

在Python中，这种一边循环一边计算的机制，称为生成器：generator。

创建一个列表：```L = [x * x for x in range(10)]```

创建一个生成器：```g = (x * x for x in range(10))```

5、迭代器：Iterator。

可以被```next()```函数调用并不断返回下一个值的对象称为迭代器。


####函数式编程 Functional Programming --> 允许把函数本身作为参数传入另一个函数，还允许返回一个函数

1、map(func,list) 
map的作用，把func作用在list的每一个元素上

2、reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

```reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)```

3、filter()函数用于过滤序列:

和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

4、sorted()排序函数 -> 默认从小到大，可以指定排序方式：key=abs

```
>>> sorted([36, 5, -12, 9, -21], key=abs)  

[5, 9, -12, -21, 36]

```

* 闭包（返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。）

* lambda -> 匿名函数

* 装饰器 -> 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。本质上，decorator就是一个返回函数的高阶函数






