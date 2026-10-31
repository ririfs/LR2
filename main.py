import emoji
from lab_python_oop.magazine import Magazine
from lab_python_oop.book import Book
from lab_python_oop.textbook import Textbook

def main():
    N = 18 
    
    while True:
        print(emoji.emojize("\n:books: ВЫБЕРИТЕ ОБЪЕКТ ДЛЯ ДЕМОНСТРАЦИИ :books:"))
        print("1. Журнал (Magazine)")
        print("2. Книга (Book)")
        print("3. Учебник (Textbook)")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == '0':
            print(emoji.emojize(":waving_hand: До встречи!"))
            break
        elif choice == '1':
            pub = Magazine("Наука и жизнь", N * 10.5, "Знание", N)
        elif choice == '2':
            pub = Book("Война и мир", N * 50.0, "Эксмо", "Л.Н. Толстой")
        elif choice == '3':
            pub = Textbook("Алгебра", N * 45.0, "Просвещение", "Макарычев", "Математика")
        else:
            print(emoji.emojize(":cross_mark: Неверный ввод! Попробуйте снова."))
            continue

        print("\n" + "="*40)
        print(emoji.emojize(f":white_check_mark: {pub}")) 
        
        print(f"Категория: {pub.get_category()}")
        print(f"Периодическое издание: {'Да' if pub.is_periodic() else 'Нет'}")
        print("="*40)

        try:
            print("\nПроверка валидации (пробуем установить отрицательную цену):")
            pub.price = -100
        except ValueError as e:
            print(f"Ошибка перехвачена: {e}")

if __name__ == "__main__":
    main()