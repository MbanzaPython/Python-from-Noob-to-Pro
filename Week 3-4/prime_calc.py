#This is the first calculator:

def prime_checker(number):
    if number == 2 or number == 3 or number == 7:
        print("It's a prime number.")
    elif number % 2 == 0 or number % 3 == 0 or number % 7 == 0 or number == 1:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)

#This is the second calculator:

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
