man = ("вода", "соль", "рыба")
human = ("в-да", "3lf", "dj_mkss_knj")
print("Недопустимые имена переменных: трудно читаются и непонятно что описывают,\n начинаются с цифры или состоят из более двух слов,\nдопустимые имена переменных выглядят противополжным образом:\n", man, human)
print(" ")
dinner = input("Привет. Какое твое любимое обеденное блюдо? ")
supper = input("Какое твое любимое блюдо на ужин? ")
print(" ")
print("Твое новое невиданное блюдо: ", dinner + supper)
print(" ")
bill = int(input("Введите сумму счета за обед в ресторане "))

print("Чаевые 15% - ", bill * 0.15, "Чаевые 20% - ", bill * 0.2)

print(" ")



cost_car = int(input("Это программа Автодилер! Сколько стоила ваша машина? "))

print("Налог 15% - ", cost_car * 0.15, "Регистрационный сбор 4% - ", cost_car * 0.04)

print(" ")

nalog = cost_car * 0.2
regist_pay = cost_car * 0.05
agent_pay = 5000
delivery_car = 4000
bill_itog = cost_car + nalog + regist_pay + agent_pay + delivery_car

print("Ваш счет: ", bill_itog, "\nСтоимость машины:", cost_car, "\nНалог:", nalog, "\nРегистрационный сбор:", regist_pay, "\nАгентский сбор:", agent_pay, "\nДоставка машины по месту назначения:", delivery_car)

input("\nНажмите Enter, чтобы выйти.")