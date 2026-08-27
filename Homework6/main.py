
# Task1
# Описание задания: Напишите программу, которая сначала спрашивает у пользователя его имя, а затем выводит персональное приветствие, используя это имя

# Листинг task1
name = input("Как тебя зовут? \n")
print(f"Привет, {name}! Приятно познакомиться")

# Task2
# Описание задания: Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника. После получения данных программа должна вычислить и вывести на экран площадь этого прямоугольника

# Листинг task2
length = int(input("Введите длину прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
square = length * width
print(f"Площадь прямоугольника: {square}")

# Task3
# Описание задания: Напишите программу, которая запрашивает у пользователя температуру в градусах Цельсия, переводит её в градусы Фаренгейта и выводит результат на экран

# Листинг task3
degree_сelsius = float(input("Введите температуру в градусах Цельсия: "))
degree_fahrenheit = degree_сelsius * 9 / 5 + 32
print(f"{degree_сelsius}°C это {degree_fahrenheit}°F")

# Task4
# Описание задания: Напишите программу, которая запрашивает у пользователя целое число и определяет, является ли оно чётным или нечётным

# Листинг task4
digit = int(input("Введите целое число: "))
if digit % 2 == 0:
    print(f"Число {digit} - чётное")
else:
    print(f"Число {digit} - нечётное")

# Task5
# Описание задания: Напишите программу, которая генерирует случайное число от 1 до 20. У пользователя есть 5 попыток, чтобы его угадать. На каждом шаге программа подсказывает («Слишком много!» или «Слишком мало!») и сообщает, сколько попыток осталось. Игра завершается, если число угадано или закончились попытки

# Листинг task5
import random

random_number = (random.randint(1, 20))
min_attemps = 1
attempts = 5
print("Я загадал число от 1 до 20. У тебя есть 5 попыток!")
while attempts > 0:
    user_number = int(input(f"Попытка {min_attemps}. Введите число: "))
    if user_number == random_number:
        print("Ты угадал! Отличная работа.")
        break
    attempts -= 1
    min_attemps += 1
    if user_number > random_number:
        print(f"Слишком много! Осталось попыток: {attempts}")
    if user_number < random_number:
        print(f"Слишком мало! Осталось попыток: {attempts}")

# Task6
# Описание задания: Напишите программу, которая работает как простой калькулятор. Программа должна запросить у пользователя два числа и символ операции (+, -, *, /), а затем выполнить расчёт и вывести результат

# Листинг task6
while True:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    operator = input("Выбери оператор (+, -, *, /)")

    if operator == "+":
        resault = first_number + second_number
        print(f"Результат: {first_number} + {second_number} = {resault}")
    elif operator == "-":
        resault = first_number - second_number
        print(f"Результат: {first_number} - {second_number} = {resault}")
    elif operator == "*":
        resault = first_number * second_number
        print(f"Результат: {first_number} * {second_number} = {resault}")
    elif operator == "/":
        if second_number == 0:
            print("Делить на ноль нельзя")
        else:
            resault = first_number / second_number
            print(f"Результат: {first_number} / {second_number} = {resault}")
    else:
        print("Вы ввели неправильный оператор попробуйте еще раз!")
        continue

    answer = input("Хотите продолжить? (дa/нет): ")
    if answer == "нет":
        print("Пока!")
        break
    elif answer == "да":
        print()
        continue
