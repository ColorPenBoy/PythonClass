import nester

print ("------------------我是分割线-------------------")

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Jones", "Eric Idle", "Terry Gilliam"]]]

# 调用函数
# 函数前面需要加上命名空间 -> 名字与包同名
nester.printListMethod(movies)
