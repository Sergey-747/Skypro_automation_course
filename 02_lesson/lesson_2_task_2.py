def is_year_leap(year):
    return year % 4 == 0

year = int(input("Введите год на проверку: "))
print("год:", year, is_year_leap(year) )