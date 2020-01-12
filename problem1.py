# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.


num_list = []

def multiplesOf3and5(number):
    for i in range(1,number):
        if (i % 3 == 0 or i % 5 == 0):
            num_list.append(i)

    return print(sum(num_list))

multiplesOf3and5(1000)

#multiplesOf3and5(1000) should return 233168