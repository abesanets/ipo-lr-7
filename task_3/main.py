# Бесанец Алексей
print("start code...\n")

import json
import os

# Имя файла с данными
filename = "cars.json"

# Проверяем, есть ли уже файл с записями. Если нет — создаем с 5 начальными данными.
if not os.path.exists(filename):
    data = [
        {"id": 1, "name": "Camry", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 60},
        {"id": 2, "name": "Model S", "manufacturer": "Tesla", "is_petrol": False, "tank_volume": 0},
        {"id": 3, "name": "Civic", "manufacturer": "Honda", "is_petrol": True, "tank_volume": 50},
        {"id": 4, "name": "Octavia", "manufacturer": "Skoda", "is_petrol": True, "tank_volume": 55},
        {"id": 5, "name": "X5", "manufacturer": "BMW", "is_petrol": True, "tank_volume": 70}
    ]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Счётчик операций (кроме выхода)
operations_count = 0

def allrecords():
    print("\nВсе записи:")
    for i, car in enumerate(cars):
        print(f"{i+1}. ID: {car['id']}, Модель: {car['name']}, "
              f"Производитель: {car['manufacturer']}, "
              f"Бензин: {'Да' if car['is_petrol'] else 'Нет'}, "
              f"Объем бака: {car['tank_volume']} л")
    global operations_count
    operations_count += 1

def idsearch():
        search_id = input("Введите id записи для поиска: ")
        found = False
        for i, car in enumerate(cars):
            if str(car["id"]) == search_id:
                print(f"\nНайдена запись (позиция {i+1}):")
                print(json.dumps(car, ensure_ascii=False, indent=4))
                found = True
                break
        if not found:
            print("Запись с таким id не найдена.")
        global operations_count
        operations_count += 1

def newcar():
        try:
            new_id = int(input("Введите id: "))
            name = input("Введите модель: ")
            manufacturer = input("Введите производителя: ")
            is_petrol_input = input("Бензиновая? (да/нет): ").strip().lower()
            is_petrol = True if is_petrol_input == "да" else False
            tank_volume = int(input("Введите объем бака (л): "))

            cars.append({
                "id": new_id,
                "name": name,
                "manufacturer": manufacturer,
                "is_petrol": is_petrol,
                "tank_volume": tank_volume
            })

            with open(filename, "w", encoding="utf-8") as f:
                json.dump(cars, f, ensure_ascii=False, indent=4)

            print("Запись успешно добавлена.")
        except ValueError:
            print("Ошибка ввода! Проверьте корректность данных.")
        global operations_count
        operations_count += 1

def deletecar():
        del_id = input("Введите id записи для удаления: ")
        found = False
        for i, car in enumerate(cars):
            if str(car["id"]) == del_id:
                del cars[i]
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(cars, f, ensure_ascii=False, indent=4)
                print("Запись успешно удалена.")
                found = True
                break
        if not found:
            print("Запись с таким id не найдена.")
        global operations_count
        operations_count += 1

def exit():
    print(f"\nКоличество выполненных операций: {operations_count}")
    print("Выход из программы...")

while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по id")
    print("3. Добавить запись")
    print("4. Удалить запись по id")
    print("5. Выйти из программы")

    choice = input("Выберите пункт меню (1-5): ")

    # Загружаем текущие данные
    with open(filename, "r", encoding="utf-8") as f:
        cars = json.load(f)

    if choice == "1":
        allrecords()

    elif choice == "2":
        idsearch()

    elif choice == "3":
        newcar()

    elif choice == "4":
        deletecar()

    elif choice == "5":
        exit()
        break
        
    else:
        print("Неверный пункт меню. Попробуйте снова.")


print("end code...\n\n")