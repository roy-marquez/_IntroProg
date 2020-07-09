primes = {1, 2, 3, 5, 7}
composites = {4, 6, 8, 9, 10}
evens = {2, 4, 6, 6, 8, 10}
odds = {1, 3, 5, 7, 9}

print (primes.intersection(composites))
print (primes.intersection(evens))
print (primes.intersection(odds))

print (primes.difference(composites))
print (composites.difference(primes))
print (primes.difference(evens))
print (primes.difference(odds))