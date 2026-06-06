word=input("Enter word to change lowercase or uppercase:")
if word.isupper():
   print(word.lower())
elif word.islower():
   print(word.upper())
else:
   print("wrong word please try again")
