




if __name__=='__main__':
    dict1 = { }
    while True:
        e = input('name: ')
        d = input('value: ')
        try:
            e = str(e)
            d = int(d)
        except ValueError as r:
            print(r)
            break
        dict1.update({e:d})
    print(dict1)
    list1 =[]
    for i in dict1.values():
        list1.append(i)
    set1= set(list1)
    list2 = list(set1)
    list2.sort()
    runner = list2[-2]
    for i in dict1:
        if dict1[i] == runner:
            print(i)
    
    
    
