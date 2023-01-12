num = int(input("Enter a number: "))
if num < 2:
    print(num, "is not a prime number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("{} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))
