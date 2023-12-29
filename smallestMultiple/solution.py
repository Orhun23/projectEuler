t = 1

while True: 
    if all(t%i==0 for i in range(2,21)):
        print("desired value is ", t)
    else:
        t = t + 1
#kinda 