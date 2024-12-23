sarda=int(input("Emter a number: "))
if sarda%2==0 and sarda%7==0:
    print("double seven")
elif sarda % 2 == 0:
    print("Even")
elif sarda % 7 == 0:
    print("Lucky Seven")
else:
    print(sarda)
