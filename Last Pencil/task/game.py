print("How many pencils would you like to use:")
pencils = int(input())
first_name = "Cameron"
second_name = "Sarah"
print(f"Who will be the first ({first_name}, {second_name}):")
first = input()
first_name_turn = True
if first == second_name:
    first_name_turn = False

while pencils > 0:
    print("|" * pencils)
    if first_name_turn:
        print(f"{first_name}'s turn:")
    elif not first_name_turn:
        print(f"{second_name}'s turn:")
    pencils -= int(input())
    first_name_turn = not first_name_turn
