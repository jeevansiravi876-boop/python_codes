import random
print("Welcome to guess the number :\ni am thinking about a number between 1 and 100")
my_choice = input("chosse the level 'e' for easy and 'h' for hard:")


if my_choice == "e":
    n = 15
    comp_choice = random.randint(1,100)
    while n>0:
        print(f"u have {n} chances to guess the number")
        
        #print(comp_choice)
        make_ur_choice = int(input("make choice : "))
        n = n-1
        if comp_choice == make_ur_choice :
            print("you won!!!")
            break
        elif comp_choice >= make_ur_choice :
            print("too low")
        elif comp_choice <= make_ur_choice :
            print("too high")
        elif n==0:
            print("u lose")
            break

elif my_choice == "h":
    n = 5
    comp_choice = random.randint(1,100)
    while n>0:
        print(f"u have {n} chances")
        
        #print(comp_choice)
        make_ur_choice = int(input("make choice : "))
        n = n-1
        if comp_choice == make_ur_choice :
            print("you won!!!")
            break
        elif comp_choice >= make_ur_choice :
            print("too low")
        elif comp_choice <= make_ur_choice :
            print("too high")
        elif n==0:
            print("u lose")
            break
else:
    print("type e for easy or h for hard\nnot other random words on keybord")