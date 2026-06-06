import random
a = "123456789abcdefghijklmnopqrstuvwxyz"
password = ""
for i in range(8):
   password += random.choice(a)
print("Your stronge password👉: ",password)
