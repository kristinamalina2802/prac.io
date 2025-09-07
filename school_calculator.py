

class SchoolCalculator:
    def __init__(self):
        self.grades = []
    
    def add_grade(self, grade):
        """Добавляет оценку в список"""
        if 2 <= grade <= 5:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена!")
        else:
            print("Оценка должна быть от 2 до 5!")
    
    def calculate_average(self):
        """Рассчитывает средний балл"""
        if not self.grades:
            return "Нет оценок для расчета"
        
        average = sum(self.grades) / len(self.grades)
        return round(average, 2)
    
    def what_grade_needed(self, target_average, future_grades_count=1):
        """Рассчитывает, какие оценки нужны для целевого среднего"""
        if not self.grades:
            return "Сначала добавьте текущие оценки"
        
        current_total = sum(self.grades)
        total_grades = len(self.grades) + future_grades_count
        needed_total = target_average * total_grades
        grade_per_exam = (needed_total - current_total) / future_grades_count
        
        if grade_per_exam > 5:
            return "Невозможно достичь такого среднего балла"
        elif grade_per_exam < 2:
            return "Цель уже достигнута или превышена!"
        else:
            return f" Нужно получить {round(grade_per_exam, 2)} за каждый из {future_grades_count} экзаменов"
    
    def save_to_file(self, filename="grades_history.txt"):
        """Сохраняет оценки в файл"""
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"Оценки: {self.grades}\n")
            f.write(f"Средний балл: {self.calculate_average()}\n")
            f.write("-" * 30 + "\n")
        print(f"Данные сохранены в файл {filename}")
    
    def show_grades(self):
        """Показывает все текущие оценки"""
        if self.grades:
            print(f"Ваши оценки: {self.grades}")
            print(f"Средний балл: {self.calculate_average()}")
        else:
            print("Пока нет оценок")

def main():
    calculator = SchoolCalculator()
    
    print("Добро пожаловать в Умный калькулятор оценок!")
    print("=" * 50)
    
    while True:
        print("\n Меню:")
        print("1. Добавить оценку")
        print("2. Посмотреть текущие оценки и средний балл")
        print("3. Узнать, какая оценка нужна для цели")
        print("4. Сохранить данные в файл")
        print("5. Выйти")
        
        choice = input("\nВыберите действие (1-5): ")
        
        if choice == "1":
            try:
                grade = float(input("Введите оценку (2-5): "))
                calculator.add_grade(grade)
            except ValueError:
                print("❌ Пожалуйста, введите число!")
        
        elif choice == "2":
            calculator.show_grades()
        
        elif choice == "3":
            try:
                target = float(input("Какой средний балл хотите?: "))
                count = int(input("Сколько экзаменов осталось?: "))
                result = calculator.what_grade_needed(target, count)
                print(f" {result}")
            except ValueError:
                print(" Пожалуйста, введите числа!")
        
        elif choice == "4":
            calculator.save_to_file()
        
        elif choice == "5":
            print(" До свидания! Удачи в учебе!")
            break
        
        else:
            print(" Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()