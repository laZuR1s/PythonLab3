from turtledemo.forest import doit1

import Truck as tr


def validation(x, condition, message):
    print(message)
    while True:
        try:
            x = float(input(">>> "))
            if condition(x):
                return x
            else:
                print("Input error!")
        except ValueError:
            print("Input error!")


def main_menu():
    print(f'\n1. Enter Truck data (console)\n'
          f'2. Enter Truck data (file)\n'
          f'3. Print data (console)\n'
          f'4. Print data (file)\n'
          f'5. Print brand\n'
          f'6. Print engine power\n'
          f'7. Print gearbox\n'
          f'8. Print number of axes\n'
          f'9. Exit')
    choice = 0
    choice = validation(choice, lambda x: (1 <= x <= 9) and (x % 1 == 0), '')
    return choice


truck = tr.Truck()
exit_flag = False

while (not exit_flag):
    choice = main_menu()
    match choice:
    case1:

    case2:
    case3:
    case4:
    case5:
    case6:
    case7:
    case8:
    case9:
    case10:

print(truck.check_brand("volvo"))
print(truck.check_brand("scania"))

# Получение бренда
print(truck.get_brand)
print(truck.get_gearbox)
print(truck.get_engine_power)
