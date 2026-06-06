i = int(input("Enter number: "))
n = int(input("Enter number: "))
if i > n:
   print(i,"is prime")
elif i < n:
   print(n,"is prime")
elif i == n:
   print(f"{i} {n} both equal")
else:
   print("number error")
