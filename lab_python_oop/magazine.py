from lab_python_oop.printed_publication import PrintedPublication

class Magazine(PrintedPublication):
    def __init__(self, title: str, price: float, publisher: str, issue_number: int):
        super().__init__(title, price, publisher) 
        self.__issue_number = None
        self.issue_number = issue_number

    @property
    def issue_number(self) -> int:
        """Номер выпуска журнала"""
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Номер выпуска должен быть положительным целым числом!")
        self.__issue_number = value

    def get_category(self) -> str:
        return "Журнал"

    def is_periodic(self) -> bool:
        """ПЕРЕОПРЕДЕЛЕНИЕ: Журналы периодические"""
        return True

    def __str__(self) -> str:
        base_str = super().__str__()
        return f"{base_str}, Номер выпуска: {self.issue_number}"