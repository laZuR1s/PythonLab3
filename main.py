import Truck as tr
from Truck import Truck


# Автор: Лазарев Александр Александрович 9 группа

# Задача №2. Класс «Truck» с полями «марка», «мощность двигателя», «коробка передач»
# (механика/автомат), «число осей». Декоратор приводит строку-результат функции
# к верхнему регистру. Декорировать все методы и функции, возвращающие строки.
# Добавить логический метод, который проверяет указанной ли марки тягач.

def validation(x, condition, message):
    print(message)
    while True:
        try:
            x = int(input(">>> "))
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
          f'5. Change brand\n'
          f'6. Change engine power\n'
          f'7. Change gearbox\n'
          f'8. Change number of axes\n'
          f'9. Check truck brand\n'
          f'10. Print to string\n'
          f'11. Exit')
    choice = 0
    choice = validation(choice, lambda x: (1 <= x <= 11) and (x % 1 == 0), '')
    return choice


def input_truck_data():
    brand = input('Enter brand: ')
    engine_power = 0
    engine_power = validation(engine_power, lambda x: x >= 0, 'Enter engine power')
    flag = False
    gearbox=''
    while not flag:
        gearbox = input('Enter type of gearbox: ')
        if gearbox.lower() == "automatic" or gearbox.lower() == "mechanic":
            flag = True
        else:
            print("Error")

    number_of_axes = 0
    number_of_axes = validation(number_of_axes, lambda x: x >= 0, 'Enter number of axes')
    return tr.Truck(brand, engine_power, gearbox, number_of_axes)


def intput_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Разделяем строку по запятой и создаем объект Truck
                data = line.strip().split(',')
                if len(data) == 4:
                    brand, engine_power, transmission, num_axles = data
                    truck1 = tr.Truck(brand, int(engine_power), transmission, int(num_axles))
                    return truck1
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except IOError:
        print(f"Ошибка чтения файла {file_path}.")


def write_to_file(file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            line = f"{truck.brand},{truck.engine_power},{truck.gearbox},{truck.number_of_axes}\n"
            file.write(line)
        print(f"Данные успешно записаны в файл {file_path}.")
    except IOError:
        print(f"Ошибка записи в файл {file_path}.")


truck = tr.Truck()
exit_flag = False

while not exit_flag:
    choice = main_menu()
    match choice:
        case 1:
            truck=input_truck_data()
        case 2:
            file_name = input("Enter file name: ")
            truck=intput_from_file(file_name)
        case 3:
            print(truck.brand)
            print(truck.engine_power)
            print(truck.gearbox)
            print(truck.number_of_axes)
        case 4:
            file_name = input("Enter file name: ")
            write_to_file(file_name)
        case 5:
            brand=input("Enter brand: ")
            truck.brand=brand
        case 6:
            engine_power=input("Enter engine power: ")
            truck.engine_power=engine_power
        case 7:
            gearbox=input("Enter gearbox: ")
            truck.gearbox=gearbox
        case 8:
            number_of_axes=input("Enter numbers of axes: ")
            truck.number_of_axes=number_of_axes
        case 9:
            brand=input("Enter brand: ")
            if truck.check_brand(brand):
                print("Same brand")
            else:
                print("Not same brand")
        case 10:
            print(truck)
        case 11:
            exit_flag=True

