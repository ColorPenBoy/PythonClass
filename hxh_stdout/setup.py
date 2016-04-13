 # 从Python发布工具导入"setup"函数
from distutils.core import setup

setup(
		name = 'hxh_stdout',
		version = '1.2.0',
		# 将模块的元数据与setup函数的参数相关联
		py_modules = ['hxh_stdout'],
		author = 'colorPen',
		author_email = 'zq252125@163.com',
		url = 'colorpen.xyz',
		description = 'A simple printer of standard output',
		)
