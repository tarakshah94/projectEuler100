def fibonacci_gen(number):
    fibonacci = []
    for i in range(1,number+1):
        if i <= 2:
            fibonacci.append(i)

        else:
            num = fibonacci[i-3]
            num1 = fibonacci[i-2]
            compute = num+num1

            fibonacci.append(compute)
    return fibonacci

list_of_fibonacci = fibonacci_gen(43)

even_nums = []

for i in list_of_fibonacci:
    if i % 2 == 0:
        even_nums.append(i)

output = sum(even_nums)
print(output)

# fiboEvenSum(10) should return 44.
# fiboEvenSum(18) should return 3382.
# fiboEvenSum(23) should return 60696.
# fiboEvenSum(43) should return 350704366.