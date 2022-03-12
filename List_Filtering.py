def filter_list(l):
 lst = []
 for i in l:
    if type(i) is not str:
        lst.append(i)
 return lst