def is_sorted(list):
    x=list[:]
    x.sort()
    if list==x:
        return True
    else:
        return False

list=[1,2,3,4,5,6,7,8,9]

print(is_sorted(list))