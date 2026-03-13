#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Игра "Угадай число"
Компьютер загадывает число от 1 до 100, а пользователь пытается угадать
"""

import random

def guess_number():
    """Основная функция игры"""
    print("=" * 50)
    print("🎮 Добро пожаловать в игру 'Угадай число'!")
    print("=" * 50)
    print("Я загадал число от 1 до 100.")
    print("У тебя есть 7 попыток, чтобы его отгадать.\n")
    
    # Загадываем число
    secret = random.randint(1, 100)
    attempts = 7
    
    for attempt in range(1, attempts + 1):
        print(f"--- Попытка {attempt} из {attempts} ---")
        
        # Получаем ввод от пользователя
        try:
            guess = int(input("👉 Твой вариант: "))
        except ValueError:
            print("❌ Ошибка! Это не число. Попробуй снова.\n")
            continue
        
        # Проверяем корректность
        if guess < 1 or guess > 100:
            print("⚠️ Число должно быть от 1 до 100!\n")
            continue
            
        # Сравниваем с загаданным числом
        if guess == secret:
            print("\n" + "=" * 50)
            print(f"🎉 ПОЗДРАВЛЯЮ! Ты угадал число {secret}!")
            print(f"🏆 Тебе потребовалось {attempt} попыток.")
            print("=" * 50)
            break
        elif guess < secret:
            print("📈 Загаданное число БОЛЬШЕ\n")
        else:
            print("📉 Загаданное число МЕНЬШЕ\n")
    else:
        # Этот блок выполняется, если цикл завершился без break
        print("\n" + "=" * 50)
        print(f"😢 К сожалению, попытки закончились.")
        print(f"🤔 Я загадал число {secret}.")
        print("=" * 50)
    
    # Спрашиваем, хочет ли пользователь сыграть ещё
    play_again()

def play_again():
    """Спрашивает, хочет ли пользователь сыграть ещё"""
    answer = input("\n🔄 Сыграем ещё? (д/н): ").lower()
    if answer in ['д', 'да', 'y', 'yes']:
        print("\n" * 2)
        guess_number()
    else:
        print("\n👋 Спасибо за игру! До встречи!")

if __name__ == "__main__":
    guess_number()