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

    def full_analysis(self):
        """Полный анализ: ввод данных, генерация и вывод результата."""
        choice = input("Вы хотите (1) ввести текст вручную или (2) сгенерировать текст? ")
        if choice == '1':
            self.input_data()
        elif choice == '2':
            self.generate_data()
        
        result = self.analyze_data()
        self.output_result(result)

class Menu:
    def __init__(self):
        self.analyzer = TextAnalyzer()

    def display_menu(self):
        """Основное меню приложения с обработкой ошибок."""
        while True:
            print("\n1) Полный анализ текста")
            print("2) Ввод данных вручную")
            print("3) Генерация данных")
            print("4) Выполнение алгоритма")
            print("5) Вывод результата")
            print("0) Завершение работы")

            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.analyzer.full_analysis()  # Вызов полного анализа
            elif choice == '2':
                self.analyzer.input_data()
            elif choice == '3':
                self.analyzer.generate_data()
            elif choice == '4':
                result = self.analyzer.analyze_data()
                print("Алгоритм выполнен.")
            elif choice == '5':
                self.analyzer.output_result(result)
            elif choice == '0':
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu = Menu()
    menu.display_menu()