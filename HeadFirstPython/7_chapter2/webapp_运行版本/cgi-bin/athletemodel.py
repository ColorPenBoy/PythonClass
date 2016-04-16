# coding=utf-8

# pickle用于数据的序列化与反序列化
import pickle

from athletelist import AthleteList

def get_coath_data(fileName):
    try:
        with open(fileName) as myfile:
            data = myfile.readline()
        templ = (data.strip().split(','))
        return (AthleteList(templ.pop(0), templ.pop(0),templ))
    except IOError as ioerr:
        print ('IOError:' + str(ioerr))
        return (None)

def put_to_store(files_list):
    all_athletes = {}

    for each_file in  files_list:
        athlete = get_coath_data(each_file)
        # 每个选手名字作为键,值是AthleteList实例
        all_athletes[athlete.name] = athlete
    try:
        with open('athletes.pickle', 'wb') as athf:
            # 将所有实例对象字典保存到pickle中
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print ('File error (put to store)' + str(ioerr))

    return (all_athletes)


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            # 从pickle中,读入字典
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print ('File error (get from store)' + str(ioerr))

    return  (all_athletes)