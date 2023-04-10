
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
    list1F.sort()
    list2F.sort()

    for i in range(len(list1F)):
        
        if list1F[i] != list2F[i]:
            return False
        
    return True


if __name__ == '__main__':
    """should print
    true
    false
    true
    false
    true
    false
    false"""
    #list test
    a = [1,2]
    b = [2,1]

    print(exactSameCont(a, b))

    a = [1]
    b = []

    print(exactSameCont(a, b))
    #tuple test
    a = (1 , 2)
    b = (2, 1)
    print(exactSameCont(a, b))

    a = (1,)
    b = ()

    print(exactSameCont(a, b))

    #set test
    a = {1, 2, 4}
    b = {2, 4, 1}
    print(exactSameCont(a, b))

    a = {1}
    b = []

    print(exactSameCont(a, b))


    #dict test
    a = [1,2,3,4]
    b = { "name" : 1,
        "age" : 5,
        "b" : 3,
        "k" : 4}
    print(exactSameCont(a, b))
        