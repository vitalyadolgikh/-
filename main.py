from function import download_data, save_data, check_price, check_name, check_time
from class_service import Service 


def show_menu():
    MENU = """
========== АВТОСЕРВИС ==========
1. Добавить услугу
2. Показать все услуги
3. Удалить услугу
4. Изменить стоимость услуги
5. Рассчитать стоимость выбранных услуг
0. Выход
"""
    print(MENU)

def add_service(name, price, time):

    data = download_data()
    service_new = Service(name, price, time)
    data.append(service_new)
    save_data(data)
    
def print_service():

    data = download_data()
    for service in data:
        print(service)

def delete_service(name):
    
    flag = False
    data = download_data()
    new_data = []
    for service in data:
        if service.name != name:
            new_data.append(service)
        else:
            flag = True
    if flag:
        print("Услуга успешно удалена!")
    else:
        print("Услуга не найдена, список остался прежним!")
    save_data(new_data)

def change_price(name, price):

    flag = False
    data = download_data()
    new_data = []
    for service in data:
        if service.name == name:
            service.change_price(price)
            flag = True
        new_data.append(service)
    if flag:
        print("Стоимость услуги успешно отредактирована!")
    else:
        print("Услуга не найдена!")
    save_data(new_data)

def final_price(*names):

    final_price = 0
    data = download_data()
    for name in names:
        for service in data:
            if service.name == name:
                final_price += service.price
    return final_price





        

def main():

    while True:

        show_menu()

        choice = input("Выберите действие: ")

        if choice == "1":
            name = check_name()
            if name is not None:
                price = check_price()
                time = check_time()
                add_service(name, price, time)
            else:
                print("Данная услуга уже внесена в базу!")

        elif choice == "2":
            print_service()

        elif choice == "3":
            name = input("Введите название услуги для ее удаления: ")
            delete_service(name)

        elif choice == "4":
            name = input("Введите название услуги, стоимость которой хотите изменить: ")
            price = check_price()
            change_price(name, price)

        elif choice == "5":
            names_input = input("Введите названия услуг через ',' стоимость которых необходимо суммировать ")
            names = [name.strip() for name in names_input.split(",")]
            print(f"Итоговая стоимость выбранных услуг: {final_price(*names)}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option")



if __name__ == "__main__":
    main()