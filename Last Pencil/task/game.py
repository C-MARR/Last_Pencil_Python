from random import randint


def print_possible_pencils(valid=True):
    print("Possible values: '1'", end='')
    if pencils == 2 and valid:
        print(" or '2'")
    else:
        print(", '2' or '3'")


def bot_turn():
    bot_pick = ""
    if pencils % 4 == 0:
        bot_pick = "3"
    if pencils % 4 == 3:
        bot_pick = "2"
    elif pencils % 4 == 1 or pencils % 4 == 2:
        bot_pick = "1"
    print(bot_pick)
    return bot_pick


print("How many pencils would you like to use:")
pencils = input()
while not pencils.isnumeric() or pencils == "0":
    if pencils == "0":
        pencils = input("The number of pencils should be positive\n")
    else:
        pencils = input("The number of pencils should be numeric\n")
pencils = int(pencils)
first_name = "Cameron"
second_name = "Sarah"
print(f"Who will be the first ({first_name}, {second_name}):")
first = input()
first_name_turn = True
while first != first_name and first != second_name:
    first = input(f"Choose between {first_name} and {second_name}\n")
if first == second_name:
    first_name_turn = False

while pencils > 0:
    print("|" * pencils)
    if first_name_turn:
        print(f"{first_name}'s turn!")
    elif not first_name_turn:
        print(f"{second_name}'s turn:")
    while True:
        if first_name_turn:
            console_input = input()
        else:
            console_input = bot_turn()
        if not console_input.isdigit():
            pencils_to_take = 0
        else:
            pencils_to_take = int(console_input)
        if pencils_to_take not in range(1, 4):
            print_possible_pencils(False)
        else:
            if pencils - pencils_to_take < 0:
                print("Too many pencils were taken")
            else:
                pencils -= pencils_to_take
                break
    first_name_turn = not first_name_turn
    if pencils == 0:
        if first_name_turn:
            print(f"{first_name} won!")
        elif not first_name_turn:
            print(f"{second_name} won!")
        break
