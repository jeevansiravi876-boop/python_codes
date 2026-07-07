print(''' _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|''')
def add():
    global result
    result = n1 + n2

def sub():
    global result
    result = n1 - n2

def mul():
    global result
    result = n1 * n2

def div():
    global result
    result = n1 / n2

while True:
    n1 = int(input("1st no: "))
    operation = input("+\n-\n*\n/\npick an operation: ")
    n2 = int(input("2nd no: "))

    while True:
        if operation == "+":
            add()
        elif operation == "-":
            sub()
        elif operation == "*":
            mul()
        elif operation == "/":
            div()
        else:
            print("type properly operations!!!")

        print(f"{n1} {operation} {n2} = {result}")

        choice = input("press y to continue with this result, n to start new calc, q to quit: ")
        if choice == "n":
            break
        elif choice == "q":
            exit()

        n1 = result
        operation = input("+\n-\n*\n/\npick an operation: ")
        n2 = int(input("what is ur next no: "))
