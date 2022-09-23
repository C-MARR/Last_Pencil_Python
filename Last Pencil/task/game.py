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
    pencils -= int(input())
    first_name_turn = not first_name_turn

