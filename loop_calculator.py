while True:

    a = int(input("enter number: "))
    n = input("enter(+)(-)(×)(÷): ")
    b = int(input("enter number: "))
    if n == "+":
       print("👉: ",a+b,"\n type (E) for exit")
    elif n == "-":
       print("👉: ",a-b,"\n type (E) for exit")
    elif n == "×":
       print("👉: ",a*b,"\n type (E) for exit")
    elif n == "÷":
       print("👉: ",a/b,"\n type (E) for exit")
    elif a or n or b  == "E":
        break
    else:
       print("number error⁉️")

