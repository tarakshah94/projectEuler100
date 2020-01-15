# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the given number?

def primeFactor(number):

    primes = []

    for i in range(2,number+1):
        if number%i == 0:
            for j in range(2,int(i/2)):
                if i%j == 0:
                    break
            else:
                primes.append(i)

    return print(max(primes))

# primeFactor(600851475143)

# largestPrimeFactor(2) should return 2.
# largestPrimeFactor(3) should return 3.
# largestPrimeFactor(5) should return 5.
# largestPrimeFactor(7) should return 7.
# largestPrimeFactor(13195) should return 29.