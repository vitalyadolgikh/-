class Service:
    def __init__(self, name: str, price: int, time: float):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной!")
        if time < 0:
            raise ValueError("Время не может быть отрицательным")
        self.name = name
        self.price = price
        self.time = time
    
    def __str__(self):
        return f"Название услуги: {self.name}, стоимость: {self.price}, длительность: {self.time}" 
    
    def to_dict(self) -> dict[str, str | int | float]:
        return {"name": self.name, "price": self.price, "time": self.time}
    
    def change_price(self, new_price: int) -> None:
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.price = new_price
    
    def __repr__(self):
        return (
        f"Service("
        f"name = {self.name!r}, "
        f"price = {self.price}, "
        f"time = {self.time})"
    )