input("Welcome to the Underwater World")
sam=input("'dive deeper' or 'surface': ")
if sam=='dive deeper':
    shr=input("You want to 'search for pearls' or 'catch the fish': ")
    if shr=='search for pearls':
        print(f"You found a rare pearl. You Win!")
    else:
            print('You got lost underwater. Game Over')
if sam=='surface':
    print("You returned safely")

