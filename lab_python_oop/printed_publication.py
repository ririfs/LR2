from abc import ABC, abstractmethod

class PrintedPublication(ABC):
    def __init__(self, title: str, price: float, publisher: str):
        self.__title = None
        self.__price = None
        self.__publisher = None
    

        
        self.title = title
        self.price = price
        self.publisher = publisher

    @property
    def title(self) -> str:
        """Название издания"""
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value or not value.strip():
            raise ValueError("Название не может быть пустым!")
        self.__title = value




    @property
    def price(self) -> float:
        """Цена издания"""
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = value

    
    @property
    def publisher(self) -> str:
        """Издательство"""
        return self.__publisher

    @publisher.setter
    def publisher(self, value: str):
        if not value or not value.strip():
            raise ValueError("Издательство не может быть пустым!")
        self.__publisher = value

    
    def is_periodic(self) -> bool:
        """Проверка на периодичность. По умолчанию False (не переодическое)."""
        return False

    @abstractmethod
    def get_category(self) -> str:
        """Получение категории издания (абстрактный метод)"""
        pass

    def __str__(self) -> str:
        """Строковое представление объекта"""
        return (f"[{self.get_category()}] Название: {self.title}, "
                f"Цена: {self.price} руб., Издательство: {self.publisher}")