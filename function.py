import json

def download_data() -> list[dict]:
    """
    Считываем данные с файла сразу превращая их в данные типа dict
    Возвращаем список словарей
    Если ошибка в отсутствии файла или он поврежден, программа выводит пустой список
    """
    data = []                                        
    try:
        with open("service.json", "r", encoding="utf-8") as f:
            data = json.load(f)                           
        return data                                       
    except (FileNotFoundError, json.JSONDecodeError):     
        return data

    
def save_data(data: list[dict]) -> None:
    """Функция открывает файл и перезаписывает в него данные, переданные ей"""
    with open("service.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)    


def check_name() -> None | str:
    """Функция запрашивает название услуги и проверяет, есть ли уже такая услуга в базе"""
    name = input("Введите название услуги: ")
    data_service = download_data()
    for data in data_service:
        if name == data["name"]:
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



