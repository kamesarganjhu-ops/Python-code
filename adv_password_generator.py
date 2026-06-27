import random 
from colorama import Fore 
a="(1)random number"
b="(2)random alphabet"
c="(3)mixed password"
d="(4)enter your choice..."
e="(5)EXIT"
try:
   while True:
      print(Fore.LIGHTCYAN_EX+f"{a}\n{b}\n{c}\n{d}\n{e}")
      option=int(input(Fore.LIGHTYELLOW_EX+"enter option: "))
      if option == 1:
         a1=int(input(Fore.LIGHTGREEN_EX+"enter password length: "))
         try:
            while True:
               nums="1234567890"
               password1=""
               for i in range(a1):
                  password1 += random.choice(nums)
               print(Fore.LIGHTGREEN_EX+password1)
         except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX+"\nCODE END")
      elif option == 2:
         a2=int(input(Fore.LIGHTGREEN_EX+"enter password length: "))
         try:
            while True:
               alpha="abcdefghijklmnopqrstuvwxyz"
               password2=""
               for i in range(a2):
                  password2 += random.choice(alpha)
               print(Fore.LIGHTGREEN_EX+password2)
         except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX+"\nCODE END")
      elif option == 3:
         a3=int(input(Fore.LIGHTGREEN_EX+"enter password length: "))
         try:
            while True:
               mixed="12abcdefgh34ijklmn56opqrst78uvwx90yz"
               password3=""
               for i in range(a3):
                  password3 += random.choice(mixed)
               print(Fore.LIGHTGREEN_EX+password3)
         except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX+"\nCODE END")  
      elif option == 4:
         ch=input(Fore.LIGHTYELLOW_EX+"enter characters: ")
         a4=int(input(Fore.LIGHTGREEN_EX+"enter password length: "))
         try:
            while True:
               m=ch
               n=a4
               password4=""
               for i in range(n):
                  password4 += random.choice(m)
               print(Fore.LIGHTGREEN_EX+password4)
         except KeyboardInterrupt:
            print(Fore.LIGHTRED_EX+"\nCODE END")
      elif option == 5:
         print(Fore.LIGHTRED_EX+"CODE ENDED")
         break
      else:
         print(Fore.LIGHTRED_EX+"ERROR")
         continue
except KeyboardInterrupt:
   print(Fore.LIGHTRED_EX+"CODE SAFELY END")
except ValueError:
   print(Fore.LIGHTRED_EX+"INVALID INPUT")
