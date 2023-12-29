def square(num) :
    dum = 0
    for i in range(1, num+1) :
        dum= dum + (i * i)
    return dum


print(square(100))

def squared(num) :
    sum = 0
    for j in range(1, num+1) :
        sum= sum + j
    sum = sum ** 2    
    return sum

print(squared(100))

x = squared(100) - square(100)
print(x)