print('Welcome to the Jungle Survival Challenge')
user_=input("Choose 'search for food','build a shelter': ")
if user_=='search for food':
    data_=input("choose between 'hunt' or 'gather': ")
    if data_=='hunt':
        print("You were attacked by wild animalas.Game Over")
    else:
        print("You found enough food.You Win")