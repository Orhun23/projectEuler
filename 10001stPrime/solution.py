def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    for number in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[number]:
            primes.append(number)

    return primes

def find_nth_prime(n):
    limit = 10**6  
    primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]

print(find_nth_prime(10001))
#will
