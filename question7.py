print("Welcome to the Forest Adventure")
_path=input("Choose a path 'left' or 'right': ")
if _path=='left':
    sam=input("pick between 'explore' or 'rest': ")
    if sam=='explore':
        print('You found treasure')
if sam=='rest':
    print('Your were attacked by wild animals.Game Over')
if _path=='right':
    print('You fell into a trap. Game Over')
