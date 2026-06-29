# Напишите функцию month_to_season() , которая принимает один аргумент — номер месяца 
# — и возвращает название сезона, к которому относится этот месяц. Например, передаем 2, 
# на выходе получаем «Зима».

def month_to_season(number):
       
    if number < 1 or number > 12:
        return ("На планете Земля только 12 месяцев в году")
    elif number == 1 or number == 2 or number ==12:
        return("Зима")
    elif  3 <= number <= 5:
        return("Весна")
    elif  6 <= number <= 8:
        return("Лето")
    else:
        return ("Осень")

num = int(input("Введите число месяца: "))
print(month_to_season(num))