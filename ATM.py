from colorama import Fore

a = "(1)Check balance"
b = "(2)Withdraw"
c = "(3)deposit"
d = "(4)Exit"
balance = 30000
try:
    while True:
       print(Fore.LIGHTCYAN_EX+f"{a}\n{b}\n{c}\n{d}")
       n = int(input(Fore.LIGHTRED_EX+"Enter option: "))
       if n == 1:
          print(Fore.LIGHTGREEN_EX+f"Total balance: {balance}")
       elif n == 2:
          w = int(input(Fore.LIGHTYELLOW_EX+"Enter amount: "))
          balance -= w 
          print(Fore.LIGHTGREEN_EX+"Withdraw Successfully")
       elif n == 3:
          m = int(input(Fore.LIGHTYELLOW_EX+"Enter amount: "))
          balance += m
          print(Fore.LIGHTGREEN_EX+"Deposit successfully")
       elif n == 4:
          print(Fore.LIGHTRED_EX+"Code End")
          break
       else:
          print(Fore.LIGHTRED_EX+"ERROR")
except ValueError:
    print(Fore.LIGHTRED_EX+"Invalid input")
          
