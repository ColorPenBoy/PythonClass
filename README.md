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

* 偏函数

当函数的参数个数太多，需要简化时，使用```functools.partial```可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单

```functools.partial```就是帮助我们创建一个偏函数的，不需要我们自己定义（P.S -> 在函数外嵌套一个函数，写死某些特定参数）


####面向对象

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

```
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
```

####多重继承、定制类、元类
Python是动态语言，随时可以给Class中添加属性，但是使用```__slots__```可以限制除规定属性外，其它属性的添加。

```__slots__```定义的属性仅对当前类实例起作用，对继承的子类是不起作用。

* 多继承习惯命名在主要类层次外，添加其它继承时给父类类名后加上'MixIn'

* 定制类 ->> 自己重写__init__、__str__、__next__、__iter__等方法。

* 使用类Class可以创建出实例Instance，使用元类metaClass可以创建出类Class


####错误处理
抛出异常：

```
try:

except:

finally:
```
断言：

```
// 如果n == 0，抛出异常
assert n != 0, 'n is Zero!' 
```


```logging```的好处，它允许你指定记录信息的级别，有```debug，info，warning，error```等几个级别，当指定```level=INFO```时，```logging.debug```就不起作用了。

指定```level=WARNING```后，```debug```和```info```就不起作用了。可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

```logging```的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如```console```和文件。

###单元测试
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

###IO编程
使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。

###常用内建库
 * datetime是Python处理日期和时间的标准库。
 * collections是Python内建的一个集合模块，提供了许多有用的集合类。
 * Base64是一种用64个字符来表示任意二进制数据的方法。
 * Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
 * Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
 * Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
 * Python提供了HTMLParser来非常方便地解析HTML。
 * urllib提供了一系列用于操作URL的功能。

###强大的第三方库
PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。

由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。


###virtualenv
在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被pip安装到Python3的site-packages目录下。

如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？

这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

virtualenv为应用提供了隔离的Python运行环境，解决了不同应用间多版本的冲突问题。

* 创建一个独立的Python运行环境

	```$ virtualenv --no-site-packages venv```


* 进入所创建的Python环境

	```$ source venv/bin/activate```

* 退出创建的Python环境

	```$ deactivate ```
	

