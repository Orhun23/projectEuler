def isPrime(number):
    if number< 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True, number

num = 1 
k=0
while k <=10001 : 
    if isPrime(num) is True:
        k+=1
    print(isPrime(num))
    num+=1
    #this