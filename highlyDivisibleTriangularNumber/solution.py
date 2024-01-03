def count_divisors(num):
    divisors = 0
    for x in range(1, int(num**0.5) + 1):
        if num % x == 0:
            divisors += 2  
    return divisors

i = 1
z = 2

while count_divisors(i) <= 500:
    i += z
    z += 1

print("First number with more than 500 divisors:", i)