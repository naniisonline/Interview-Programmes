#The most efficient way
#Geeks for geeks

num = int(input("Enter the number:"))  # if we not wish to ask user ip give directly number value
# If given number is greater than 1

if num > 1:
    for i in range(2, int(num/2)+1):    #here int(num/2) gives round of value of division, we are checking for half only
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if num % i == 0:
            print(num, "is not a prime number!")
            break
    else:
        print(num, "is a prime number!")
elif num == 1:
    print(num, "is not a prime number!")
else:
    print("Negative numbers cannot be Prime numbers!")