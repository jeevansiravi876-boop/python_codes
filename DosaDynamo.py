dosa_menu = {
    "Plain Dosa": {
        "ingredients": {
            "batter": 150,
            "chatni": 30,
            "sambar": 200
        },
        "cost": 60
    },
    "Masala Dosa": {
        "ingredients": {
            "batter": 150,
            "chatni": 30,
            "aloo": 80,
            "sambar": 200
        },
        "cost": 80
    },
    "Mysore Masala Dosa": {
        "ingredients": {
            "batter": 150,
            "chatni": 30,
            "aloo": 80,
            "sambar": 200
        },
        "cost": 100
    }
}
profit = 0
resources = {
    "batter" : 500,
    "chatni" : 100,
    "aloo": 200,
    "sambar": 500,
}

menu_choices = {
    1: "Plain Dosa",
    2: "Masala Dosa",
    3: "Mysore Masala Dosa",
}
is_on = "yes"
while is_on.lower() == "yes":
    choice = int(input("what would you like to have \n1. Plain Dosa                     ₹60\n2. Masala Dosa                    ₹80 \n3. Mysore Masala Dosa             ₹100\nfor turning off press 4 and for information about resources press 5 : "))
    if choice == 4:
        break

    elif choice == 5:
        print(f"orignal_amount_of_batter_left : {resources['batter']}ml")
        print(f"orignal_amount_of_chatni_left : {resources['chatni']}ml")
        print(f"orignal_amount_of_aloo_left : {resources['aloo']}gm")
        print(f"orignal_amount_of_sambar_left : {resources['sambar']}ml")
        print(f"Money : ₹{profit}\n")

    elif choice in menu_choices:
        selected_item = menu_choices[choice]
        cost = dosa_menu[selected_item]["cost"]
        ingredients = dosa_menu[selected_item]["ingredients"]
        can_make = all(resources[item] >= amount for item, amount in ingredients.items())

        if not can_make:
            print("Sorry, not enough ingredients for that dosa.\n")
            break

        for item, amount in ingredients.items():
            resources[item] -= amount

        print("please insert money")
        ten_ruppe = int(input("₹10 note :"))
        twenty_ruppe = int(input("₹20 note :"))
        fifty_ruppe = int(input("₹50 note :"))
        money_paid = ten_ruppe*10 + twenty_ruppe*20 + fifty_ruppe*50
        money_left = money_paid - cost
        print(f"You total paid ₹{money_paid}, here is your change ₹{money_left}")
        print(f"here is ur {selected_item} enjoy!!!")
        profit += cost
        is_on = input("would u like to continue order anything else (yes/no)")
        if is_on == "no":
            break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")
        break
