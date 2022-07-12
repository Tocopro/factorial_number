def prime_number(num_1):
    if num_1 == 0:
        return 1
    else:
        return num_1 * (prime_number(num_1 - 1))


num = int(input("Enter a Number: "))
answer = prime_number(num)
print(answer)

