name = input("enter your name👉")
mark = int(input("enter your mark👉"))

if mark >= 80:
    print(f"{name} you are topper 🔥")
elif mark >= 65:
    print(f"{name} you are Average 😎")
elif mark >= 50:
    print(f"{name} you are weak 🙁")
elif mark >= 10:
    print(f"{name} you are fail🤬,\nbut you are a warrior ☠️\nwho never give up 🧗‍♂️")
else:
    print("Invalid marks")
