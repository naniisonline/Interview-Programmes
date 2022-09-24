num = int(input("Enter your number:"))

n1, n2 = 0, 1
sum = 0
if num<=0:
    print("Please enter a number reater than zero!")
else:
    for i in range(0, num):
        print(sum, end=" ")
        n1 = n2
        n2 = sum
        sum = n1 + n2
