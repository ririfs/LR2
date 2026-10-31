from lab_python_oop.printed_publication import PrintedPublication

class Book(PrintedPublication):
    def __init__(self, title: str, price: float, publisher: str, author: str):
        super().__init__(title, price, publisher)
        self.__author = None
        self.author = author

    @property
    def author(self) -> str:
        """Автор книги"""
        return self.__author

    @author.setter
    def author(self, value: str):
        if not value or not value.strip():
            raise ValueError("Имя автора не может быть пустым!")
        self.__author = value

    def get_category(self) -> str:
        return "Книга"

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Автор: {self.author}"