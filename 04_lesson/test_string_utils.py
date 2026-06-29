import pytest
from string_utils import StringUtils

# capitalize: Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст 
@pytest.mark.positive
@pytest.mark.parametrize("line, result", [
    #1. Перобразует "skip" в слов с заглавной буквой "Skip"
    ("skip", "Skip"), 
    ])
def test_capitalize_positive(line, result):
    util = StringUtils() 
    res = util.capitalize(line)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize("line, expected_result", [
    # 1. Абсолютно пустая строка
    ("", ""),
    # 2. Строка состоит только из одного или нескольких пробелов
    (" ", " "),
    ("   ", "   "),
    # 3. Строка уже начинается с заглавной буквы (остается без изменений)
    ("Python", "Python"),
    # 4. Строка состоит только из цифр или спецсимволов
    ("12345", "12345"),
    ("@#$%", "@#$%"),
    # 5. Первая буква уже заглавная, но остальные буквы в РАЗНОМ регистре
    ("ПрИвЕт", "Привет") 
])
def test_capitalize_negative(line, expected_result):
    util = StringUtils()
    res = util.capitalize(line)
    assert res == expected_result


# trim: Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.mark.positive
@pytest.mark.parametrize("line, result",
    # 1. Принимает текст с одним пробелом
[(" Текст с пробелом", "Текст с пробелом"),
    # 2. Принимает текст с двумя пробелами
 ("  Текст с двумя пробелами","Текст с двумя пробелами"),
    # 3. Принимает текст с несколькими пробелами
 ("     Текст с пятью пробелами","Текст с пятью пробелами")
 ])
def test_trim_positive(line, result):
    util = StringUtils()
    res = util.trim(line)
    assert  res == result

@pytest.mark.negative
@pytest.mark.parametrize("line, result", [
    # 1. Пустая строка
    ("", ""),
    # 2. Строка, состоящая только из пробелов, должна стать пустой
    (" ", ""),
    ("     ", ""),
    # 3. Строка без пробелов в начале, должна остаться без изменений
    ("Текст", "Текст"),
    # 4. Пробелы стоят только в конце строки, текст должен остаться без изменения
    ("Текст с пробелом в конце ", "Текст с пробелом в конце "),
])
def test_trim_negative(line, result):
    util = StringUtils()
    res = util.trim(line)
    assert res == result

# contains: Возвращает `True`, если строка содержит искомый символ и `False` - если нет
@pytest.mark.positive
@pytest.mark.parametrize("line, symbol, result", 
    # 1. Поиск в начале текста
 [("Простоквашено","П", True),
  # 2. Поиск в середине текста
  ("Выселки-Белкина","е", True),
  # 3. Поиск спец символа
  ("Pen@45","@", True)
 ])
def test_contains_positive(line, symbol, result):
    util = StringUtils()
    res = util.contains(line, symbol)
    assert res == result   

@pytest.mark.negative
@pytest.mark.parametrize("line, symbol, result", [
    # 1. Символ  отсутствует в строке
    ("Простоквашено", "х", False),
    # 2. Регистр не совпадает
    ("Простоквашено", "п", False),  # Маленькая 'п' вместо большой 'П'
    ("Pen@45", "PEN", False),
     # 3. Искомый символ длиннее, чем сама строка
    ("Слон", "Слоненок", False),
     # 4. Поиск в абсолютно пустой строке
    ("", "А", False),
])
def test_contains_negative(line, symbol, result):
    util = StringUtils()
    res = util.contains(line, symbol)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize("line, symbol, result", [
  # 1. Удаление подстроки в конце строки
("Простоквашено","квашено", "Просто"), 
  # 2. Удаление подстроки в начале строки
 (" Чудо-Юдо","Юдо", " Чудо-"), 
  # 3. Удаление подстроки состоящей из цифр
 ("Home 45", "45", "Home "),
 # 4. Удаление подстроки со спец символом
 ("Tree@mail.ru", "@", "Treemail.ru"),
 # 5. Удаление регистрационно-зависимых одинаковых символов
    ("ТриЧетыреТри", "Три", "Четыре"),
 # 6. Удаление пробела 
    ("Children of the world", " ", "Childrenoftheworld"),
#  7. Множественные вхождения 
    ("сорока", "о", "срка"),
    ("яблоко,киви,слива", "киви,", "яблоко,слива"),
])
def test_delete_symbol_positive(line, symbol, result):
    util = StringUtils()
    res = util.delete_symbol(line, symbol)
    assert res == result
    print(res)

@pytest.mark.negative
@pytest.mark.parametrize("line, symbol, result", [
    # 1. Символа/подстроки нет в строке (строка не должна измениться)
    ("Ресторан", "л", "Ресторан"),
    # 2. Искомый символ передан в другом регистре (метод должен быть регистрозависимым)
    ("Ресторан", "р", "Рестоан"),     # Из примера: маленькая 'р' удаляется
    ("Ресторан", "Н", "Ресторан"),    # Большая 'Н' отсутствует, строка не меняется
    # 3. Передана пустая строка для обработки
    ("", "снег", ""),
    # 4. Передан пустой символ для удаления
    ("Ресторан", "", "Ресторан"),
    # 5. И строка, и символ пустые
    ("", "", ""),
    # 6. Символ совпадает со всей строкой полностью (должна получиться пустая строка)
    ("Ресторан", "Ресторан", ""),
    # 7. Подстрока встречается несколько раз (метод должен удалить ВСЕ вхождения, как указано в описании)
    ("папайя", "па", "йя")
])
def test_delete_symbol_negative(line, symbol, result):
    util = StringUtils()
    res = util.delete_symbol(line, symbol)
    assert res == result





        




