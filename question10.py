input("Welcome to the haunted castle")
sam=input("'enter the castle' or 'run away': ")
if sam=='enter the castle':
    shr=input("Choose the door'red' or 'green' or 'black': ")
    if shr=='red':
        print("You entered a room full of flames. Game Over.")
    elif shr=='green':
            print('You found the treasure. You Win')
    else:
         print('You were captured by ghost.Game Over')
if sam=='run away':
    print("You escaped safely")

