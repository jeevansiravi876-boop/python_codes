print("Welcome to the rollercoster")
height = int(input("what is your height?(in cm) "))
bill = 0
if height >= 120:
    print("you can ride the rollercaster ")
    age = int(input("what is your age? "))
    if age <= 12:
        print("pay 5$")
        bill = 5
    elif 18 > age >12:  
        print("pay 7$")
        bill = 7
    else:
        print("pay 12$")  
        bill = 12
    wants_photo = input("do you want photos?\ntype yes for photos\n")
    if wants_photo =="yes":
        bill += 3

    print(f"your total bill is ${bill}")
else:
    print("you can't ride the rollercoster")