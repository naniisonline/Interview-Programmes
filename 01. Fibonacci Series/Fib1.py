# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms?"))

#first two terms

n1, n2 = 0, 1
count = 0

#check if the entered number is valid
if nterms<0:
  print("Please enter a positive integer!")
#if there is only one terms, return n1
elif nterms==0:
  print(n1)
#other than this generate fibonacci sequence
else:
  print("Fibonacci Series:")
  while count<nterms:
    print(n1)
    nth = n1 + n2
    #update values
    n1 = n2
    n2 = nth
    count += 1