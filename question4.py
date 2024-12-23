num=int(input("Enter a number: "))
if num%2==0:
    print(f"{num} is divisible by 2")
    if num%5==0:
        print(f"{num} is divisble by 5")
    else:
        print(f"{num} is not divisible by 5")
else:
    print(f"{num} is not divisble by 2")


