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


james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

# clean_james = [sanitize(item) for item in james]
# clean_julie = [sanitize(item) for item in julie]
# clean_mikey = [sanitize(item) for item in mikey]
# clean_sarah = [sanitize(item) for item in sarah]
#
# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

#推导列表
# print(sorted([sanitize(item) for item in james]))
# print(sorted([sanitize(item) for item in julie]))
# print(sorted([sanitize(item) for item in mikey]))
# print(sorted([sanitize(item) for item in sarah]))

print ('-----------------手动去重-------------------------------------')
# unique_james = []d
#
# for item in clean_james:
#     if item not in unique_james:
#         unique_james.append(item)
# print (unique_james)


print ('-----------------使用Set去重-------------------------------------')

print(sorted (set ([sanitize(item) for item in james]))[0:3])
print(sorted (set ([sanitize(item) for item in julie]))[0:3])
print(sorted (set ([sanitize(item) for item in mikey]))[0:3])
print(sorted (set ([sanitize(item) for item in sarah]))[0:3])



