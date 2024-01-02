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

limit = 2000000
prime_numbers = sieve_of_eratosthenes(limit)
sum_of_primes = sum(prime_numbers)
print(prime_numbers)
print(sum_of_primes)