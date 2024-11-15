import random
import string
from collections import Counter

class TextAnalyzer:
    def __init__(self):
        self.data = ""

    def input_data(self):
        """Ввод данных вручную."""
        self.data = input("Введите текст: ")

    def generate_data(self):
        """Генерация случайного текста."""
        length = random.randint(50, 200)
        self.data = ''.join(random.choices(string.ascii_letters + string.punctuation + ' ', k=length))
        print(f"Сгенерированный текст: {self.data}")

    def analyze_data(self):
        """Анализ данных и частотный анализ текста."""
        total_chars = len(self.data)
        if total_chars == 0:
            return {}
        
        frequency = Counter(self.data)
        frequency_analysis = {char: count / total_chars for char, count in frequency.items()}
        
        return frequency_analysis

    def output_result(self, result):
        """Вывод результата анализа."""
        if not result:
            print("Нет результатов для отображения.")
            return
        
        print("Частотный анализ текста:")
        for char, freq in result.items():
            print(f"'{char}': {freq:.4f}")

class Menu:
    def __init__(self):
        self.analyzer = TextAnalyzer()

    def display_menu(self):
        """Основное меню приложения с обработкой ошибок."""
        while True:
            print("\n1) Ввод данных вручную")
            print("2) Генерация данных")
            print("3) Выполнение алгоритма")
            print("4) Вывод результата")
            print("0) Завершение работы")

            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.analyzer.input_data()
            elif choice == '2':
                self.analyzer.generate_data()
            elif choice == '3':
                result = self.analyzer.analyze_data()
                print("Алгоритм выполнен.")
            elif choice == '4':
                self.analyzer.output_result(result)
            elif choice == '0':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()