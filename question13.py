input("Welcome to the Wizarding World")
sam=input("'spells' or 'potions': ")
if sam=='spells':
    shr=input("You want to 'practice magic' or 'compete in deuls': ")
    if shr=='practice magic':
         print("You mastered a powerful spell. You Win!")
    else:
            print('You lost to a rival wizard. Game Over')
if sam=='potions':
   fut=input("'brew an elixir' or 'create poison': ")
   if fut=='brew an elixir':
        print('You healed a village.You win')
   else:
        print('Your potion backfired.Game over')


