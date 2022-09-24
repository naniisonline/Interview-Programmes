#Gundu's Program

num = int(input("Enter the number:\n"))

for i in range(2,num):
  if num % i == 0:
    print("Not prime!")
    break
else:
  print("Prime number!")