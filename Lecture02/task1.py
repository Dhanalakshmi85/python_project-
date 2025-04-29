# Ask the user for an integer
num = int(input("Enter an integer: "))

# Check if the number is prime
if num < 2:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number.")
    else:
        print("Not a prime number.")

