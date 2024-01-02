a = 0 
b = 0 
c = 0
z = a + b + c 

while z != 1000:
    for i in range(1, 1000):
        for j in range(1, 1000):
            for k in range(1, 1000):
                if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                    a = i
                    b = j
                    c = k
                    z = a + b + c
                    break  
            if z == 1000:
                break  
        if z == 1000:
            break  

if z == 1000:
    print("a:", a, "b:", b, "c:", c)
    print("Product:", a * b * c)
