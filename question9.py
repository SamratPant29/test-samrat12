input("Welcome to the space Adventure")
sam=input("'land on mars' or 'fly to jupiter': ")
if sam=='land on mars':
    shr=input("You want to 'explore' or 'build a base': ")
    if shr=='explore':
        print("You found artifacts.You win")
    else:
            print('You ran out of resources.Game over')
if sam=='fly to jupiter':
    print("Your spaceship crashed.Game Over")




