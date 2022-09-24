# Written by me or b = s[::-1]

s = input("Enter the String:")
b = reversed(s)

if s == b:
    print("This is a PALINDROME!")
else:
    print("This is not a PALINDROME")