
def exactSameCont(list1, list2):
    list1F = []
    list2F = []
    if len(list1) != len(list2):
        return False
    
    if isinstance(list1, dict):
        for i in list1.values():
            list1F.append(i)
    else:
        for i in list1:
            list1F.append(i)

    if isinstance(list2, dict):
        for i in list2.values():
            list2F.append(i)
    else:
        for i in list2:
            list2F.append(i)

    for i in list1F:
        
        if list1F[i -1] != list2F[i - 1]:
            return False
        
    return True



a = [1,2,3,4]
b = { "name" : 1,
     "age" : 5,
     "b" : 3,
     "k" : 4}
print(exactSameCont(a, b))
    