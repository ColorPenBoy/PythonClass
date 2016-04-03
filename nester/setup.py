# 从Python发布工具导入"setup"函数
from distutils.core import setup

setup(
		name = 'nester',
		version = '1.0.0',
		# 将模块的元数据与setup函数的参数相关联
		py_modules = ['nester'],
		author = 'colorPen',
		author_email = 'zq252125@163.com',
		url = 'colorpen.xyz',
		description = 'A simple printer of nested lists',
		)
