from datetime import datetime
start=datetime.now()

number = int(input('Number: '))

primes = []
for i in range(2, number):
    prime = True
    for num in range(2,9):
        if i % num == 0:
            prime = False
            break
    if prime:
        primes.append(i)
            
for prime in primes:
    print(prime)
print("Time taken: ", datetime.now()-start)
