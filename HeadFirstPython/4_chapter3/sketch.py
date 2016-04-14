### split()
### find()
### with 

### Chi Jiu Hua Shu Ju
import pickle

man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) =  each_line.split(':', 1)
            line_spoken = line_spoken.strip( )
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing')

### Write To File
try:
    with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError:
    print('File Error.')
except pickle.PickleError as perr:
    print('Pickle Error:' + str(perr))
