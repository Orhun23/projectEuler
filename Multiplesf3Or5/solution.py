def getMul1(num , aimedNumber):
    i = 0
    mList =[]
    while num*i < aimedNumber:
        mList.append(num*i)
        i += 1
    return mList
 
def getMul2(num , aimedNumber):
    j = 0
    zList =[]
    while num*j < aimedNumber:
        zList.append(num*j)
        j += 1
    return zList

result = getMul1(3, 1000)
result1 = getMul2(5 ,1000)
w = set(result).union(result1) #important step 
t = sum(w)

print("sum is ", t)
#awards eerlijk
#wtf main