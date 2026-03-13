#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Калькулятор на списках
Запрашивает 5 чисел и выполняет различные операции
"""

def get_numbers():
    """Функция для ввода 5 чисел"""
    numbers = []
    print("🔢 Введите 5 чисел:")
    
    for i in range(5):
        while True:  # Цикл для повторного ввода при ошибке
            try:
                num = float(input(f"Число {i+1}: "))
                numbers.append(num)
                break  # Выходим из цикла while, если ввод успешен
            except ValueError:
                print("❌ Ошибка! Введите число (можно с десятичной точкой)")
    
    return numbers

def calculate_sum(numbers):
    """Вычисляет сумму чисел"""
    return sum(numbers)

def calculate_average(numbers):
    """Вычисляет среднее арифметическое"""
    if numbers:  # Проверяем, что список не пустой
        return sum(numbers) / len(numbers)
    else:
        return 0

def find_max(numbers):
    """Находит максимальное число"""
    if numbers:
        return max(numbers)
    else:
        return None

def find_min(numbers):
    """Находит минимальное число"""
    if numbers:
        return min(numbers)
    else:
        return None

def reverse_list(numbers):
    """Возвращает список в обратном порядке"""
    return numbers[::-1]  # Срез с шагом -1

def main():
    """Главная функция программы"""
    print("=" * 50)
    print("📊 КАЛЬКУЛЯТОР НА СПИСКАХ")
    print("=" * 50)
    
    # Получаем числа от пользователя
    numbers = get_numbers()
    
    # Выводим исходный список
    print("\n📋 Введённые числа:", numbers)
    
    # Вычисления
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_max(numbers)
    minimum = find_min(numbers)
    reversed_nums = reverse_list(numbers)
    
    # Выводим результаты
    print("\n📊 РЕЗУЛЬТАТЫ:")
    print(f"   Сумма: {total}")
    print(f"   Среднее: {average:.2f}")
    print(f"   Максимум: {maximum}")
    print(f"   Минимум: {minimum}")
    print(f"   В обратном порядке: {reversed_nums}")
    
    # Дополнительно: сортировка
    print(f"   По возрастанию: {sorted(numbers)}")
    print(f"   По убыванию: {sorted(numbers, reverse=True)}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()