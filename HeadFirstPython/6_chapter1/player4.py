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
        return ({
            # 返回前两项,并赋值
            'Name': templ.pop(0),
            'DOB' : templ.pop(0),

            # 剩余时间进行去重,排序并返回
            'Times' : str(sorted(set ([sanitize(item) for item in templ]))[0:3])
        })
    except IOError as ioerr:
        print ('IOError:' + str(ioerr))
        return (None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')


print (james['Name'] + "'s fastest times are:" + james['Times'])
print (julie['Name'] + "'s fastest times are:" + julie['Times'])
print (mikey['Name'] + "'s fastest times are:" + mikey['Times'])
print (sarah['Name'] + "'s fastest times are:" + sarah['Times'])