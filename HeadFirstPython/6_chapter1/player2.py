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
        return (data.strip().split(','))
    except IOError as ioerr:
        print ('IOError:' + str(ioerr))
        return (None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

# 返回前两项,并赋值
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)

# 剩余时间进行去重,排序并返回
print(sarah_name + "'s fastest times are:" + str(sorted (set ([sanitize(item) for item in sarah]))[0:3]))

