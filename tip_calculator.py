print("Welcome to tip calculator!")


amount =float(input("what was the total amount of bill? $"))

tip = int(input("How much tip would you like to give? 10,12 or 15 "))

no_of_people = int(input("How many people to split bill in? "))

tip_as_per = tip/100
total_tip_amount = amount*tip_as_per
total_bill = total_tip_amount + amount
aamount = total_bill/no_of_people

print("each person should pay : $" + str(round(aamount,2)))