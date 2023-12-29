nterms = int(input("how many term big mans? "))
count = 0 
a = 1 
b = 2 
z = 0

if nterms > 0 : 
    while count < nterms and a <4000000:
        if a%2 == 0:
            z += a 
            #print(a)     
        ntw = a + b 
        a = b 
        b = ntw
        count = count + 1

print("sum is", z)
#work?