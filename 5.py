L1=[1,2,2,3,3,4,4,5,5,6,6,7,7,8,9]
L2=[]

def unique_elements(L1):
    for i in L1:
        if i not in L2:
            L2.append(i)
    return L2

print(unique_elements(L1))
