# Создайте программу, которая будет выводить список слов в случайном порядке. На экране должны печататься без повторений все слова 
# из представленного списка.

import random

print("Введите 4 слова для демонстрации программы:")
a = input("Первое слово: \n")
b = input("Второе слово \n")
c = input("Третье слово \n")
d = input("Четвертое слово: \n")

WORDS = [a, b, c, d]

print("\nИзначальный список: \n", WORDS)

random.shuffle(WORDS)

print("\nСписок в случайном порядке: \n", WORDS)

input("\n\nНажмите Enter, чтобы выйти.")

