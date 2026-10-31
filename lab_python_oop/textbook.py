from lab_python_oop.book import Book

class Textbook(Book):
    def __init__(self, title: str, price: float, publisher: str, author: str, subject: str):
        super().__init__(title, price, publisher, author)
        self.__subject = None
        self.subject = subject

    @property
    def subject(self) -> str:
        """Учебный предмет"""
        return self.__subject

    @subject.setter
    def subject(self, value: str):
        if not value or not value.strip():
            raise ValueError("Предмет не может быть пустым!")
        self.__subject = value

    def get_category(self) -> str:
        return "Учебник"

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Предмет: {self.subject}"