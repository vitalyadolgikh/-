import json
from class_service import Service

def download_data() -> list[Service]:
    """
    Считываем данные с файла сразу превращая их в объекты класса Service
    Возвращаем список Объектов класса
    Если ошибка в отсутствии файла или он поврежден, программа выводит пустой список
    """
    data_obj = []                                        
    try:
        with open("service.json", "r", encoding="utf-8") as f:
            services_data = json.load(f)
            for service in services_data:
                service_obj = Service(**service)
                data_obj.append(service_obj)                           
        return data_obj                                       
    except (FileNotFoundError, json.JSONDecodeError):     
        return data_obj

    
def save_data(service: list[Service]) -> None:
    """
    Преобразует список объектов Service в словари
    и сохраняет данные в JSON-файл.
    """
    service_dict = [service_obj.to_dict() for service_obj in service]
    with open("service.json", "w", encoding="utf-8") as f:
        json.dump(service_dict, f, ensure_ascii=False, indent=4)    


def check_name() -> None | str:
    """Функция запрашивает название услуги и проверяет, есть ли уже такая услуга в базе"""
    name = input("Введите название услуги: ")
    data_service = download_data()
    for data in data_service:
        if name == data.name:
            return None
    return name


def check_price() -> int:
    """Функция запрашивает стоимость услуги у пользователя, проверяет правильность введенных данных, в случае ошибки запрашивает их снова"""
    while True:
        try:
            price = int(input("Введите стоимость услуги: "))
            if price < 0: 
                raise ValueError("Стоимость не может быть отрицательной!")
            return price
        except ValueError:
            print("Ошибка: Введены неверные данные. Введите стоимость целым числом")


def check_time() -> float:
    """Функция запрашивает времяя оказания услуги у пользователя, проверяет правильность введенных данных, в случае ошибки запрашивает их снова"""
    while True:
        try:
            time = float(input("Введите время оказания услуги (дробное число): "))
            if time < 0: 
                raise ValueError("Время не может быть отрицательным!")
            return time
        except ValueError:
            print("Ошибка: Введены неверные данные. Введите дробное число!")



