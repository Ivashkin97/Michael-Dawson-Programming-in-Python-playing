# Напишите программу, которая принимала бы текст из пользовательского ввода и печатала этот текст на экране наоборот

message = str(input("Введите любой текст и вы получите его наоборот: "))
new_message = " "
for i in message[::-1]:
    new_message +=i
print("А вот ваш новый текст: ", new_message)
input("\n\nНажмите Enter, чтобы выйти из программы...")