
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def allPrimesUpTo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_less_than(n):
    return [x for x in range(2, n) if is_prime(x)]

# Example usage:
n = 100
print("Primes less than", n, ":", primes_less_than(n))