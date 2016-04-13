import sys

def StandardOutputMethod(moviesList, indent = False, level = 0, fh = sys.stdout):
    for each_item in moviesList:
        if isinstance(each_item, list):
            StandardOutputMethod(each_item, indent, level + 1, fh)
        else:
            if indent:
                for teb_stop in range(level):
                    print("\t",end='', file=fh)
            print(each_item, file=fh)
