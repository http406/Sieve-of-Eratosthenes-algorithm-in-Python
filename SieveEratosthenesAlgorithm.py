def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(limit + 1)]
    p = 2
    while p ** 2 <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p ** 2, limit + 1, p):
                prime[i] = False
        p += 1

    # Generate the list of prime numbers
    primes = [p for p in range(2, limit + 1) if prime[p]]
    return primes

# Example usage:
limit = 10000
print("Prime numbers up to", limit, "are:")
print(sieve_of_eratosthenes(limit))
