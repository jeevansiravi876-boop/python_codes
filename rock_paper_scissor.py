import random
rock = '''  
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper ='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
 
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
print("welcome to rook paper scissor game chosse 0 for rock, 1 for paper or 2 for sissor")

my_choice =int(input("chosse 0 for rock, 1 for paper or 2 for sissor   "))

print("your choice is")
print(my_choice)

if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
else:
    print(scissor)


ur_choice = [0,1,2]
ur_choice = random.choice(ur_choice)
print("computer's choice")
print(ur_choice)

# if my_choice == 0:
#     print(rock)
# elif my_choice == 1:
#     print(paper)
# else:
#     print(scissor)

if ur_choice == 0:
    print(rock)
elif ur_choice == 1:
    print(paper)
else:
    print(scissor)


if my_choice == 0 and ur_choice ==1:
    print("you lose")
elif my_choice == 1 and ur_choice ==2:
    print("you lose")
elif my_choice == 2 and ur_choice == 0:
    print("you lose")
elif my_choice == 0 and ur_choice ==0:
    print("tie")
elif my_choice == 1 and ur_choice ==1:
    print("tie")
elif my_choice == 2 and ur_choice ==2:
    print("tie")
else:
    print("you won")


