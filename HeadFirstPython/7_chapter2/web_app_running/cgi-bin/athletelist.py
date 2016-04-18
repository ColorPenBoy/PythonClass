# coding=utf-8
# 使用类来关联数据
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        # 父类初始化函数
        list.__init__([])
        # 初始化对象的代码
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    @staticmethod
    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return(time_string) 
        (mins, secs) = time_string.split(splitter)
        return (mins + '.' + secs)


    @property
    def top3(self):
        return (sorted(set ([self.sanitize(item) for item in self]))[0:3])