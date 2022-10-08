def print_possible_pencils():
    print("Possible values: '1'", end='')
    if pencils == 2:
        print(" or '2'")
    else:
        print(", '2' or '3'")


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
        print(f"{first_name}'s turn:")
    elif not first_name_turn:
        print(f"{second_name}'s turn:")
    while True:
        console_input = input()
        if not console_input.isdigit():
            pencils_to_take = 0
        else:
            pencils_to_take = int(console_input)
        if pencils_to_take not in range(1, 4):
            print_possible_pencils()
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


