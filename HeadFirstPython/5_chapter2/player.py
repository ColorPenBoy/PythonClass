
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)


with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for item in james:
    clean_james.append(sanitize(item))
for item in julie:
    clean_julie.append(sanitize(item))
for item in mikey:
    clean_mikey.append(sanitize(item))
for item in sarah:
    clean_sarah.append(sanitize(item))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
