from datetime import datetime

number = int(input('Number: '))
start=datetime.now()

primes = []
for i in range(2, number):
    prime = True
    for num in range(2,3):
        if i % num == 0:
            prime = False
            break
    if prime:
        primes.append(i)
            
for prime in primes:
    print(prime)
print("Time taken: ", datetime.now()-start)
