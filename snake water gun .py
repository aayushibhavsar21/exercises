

print("_______snake , water , gun _______\n RULES: \nsnake can drink water \nwater can make gun faulty \ngun can kill snake")

import random

option = ["snake","water","gun"]
play=1
while(play):

    user_choice = input('\nselect one from "snake","water","gun":')
    comp_choice = option[random.randint(0,2)]
    print("computer choice:",comp_choice)
    
    if user_choice == comp_choice:
        print("draw")
        
    elif user_choice == "snake":
        if( comp_choice == "water" ):
            print(" you won ")
        else:
            print(" computer won ")
        
    elif user_choice == "water":
        if( comp_choice == "gun" ):
            print(" you won ")
        else:
            print(" computer won ")
        
    elif user_choice == "gun":
        if( comp_choice == "snake" ):
            print(" you won ")
        else:
            print(" computer won ")

    play=int(input("press 1 to play again and 0 to exit:"))


