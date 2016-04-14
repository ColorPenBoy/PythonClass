# coding=utf-8

# 使用类来关联数据
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        # 初始化对象的代码
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top_three_times(self):
        return (sorted(set ([sanitize(item) for item in self]))[0:3])

# coding=utf-8
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(fileName):
    try:
        with open(fileName) as myfile:
            data = myfile.readline()
        templ = (data.strip().split(','))
        return (AthleteList(templ.pop(0), templ.pop(0),templ))
    except IOError as ioerr:
        print ('IOError:' + str(ioerr))
        return (None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')


print (james.name + "'s fastest times are:" + str(james.top_three_times()))
print (julie.name + "'s fastest times are:" + str(julie.top_three_times()))
print (mikey.name + "'s fastest times are:" + str(mikey.top_three_times()))
print (sarah.name + "'s fastest times are:" + str(sarah.top_three_times()))

# 测试
vera = AthleteList('vear vi')
vera.append('1.31')
vera.extend(['2.22', '1-21', '2:22'])
print (vera.name + str(vera.top_three_times()))