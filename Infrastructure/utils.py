
def mySearch(lst,condition):
    result = []
    for i in lst:
        if condition(i):
            result.append(i)
    return result

def mySort(list,relation):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if not relation(list[i],list[j]):
                list[i],list[j] = list[j],list[i]
    return list





def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]


