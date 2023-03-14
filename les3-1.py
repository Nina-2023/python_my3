def division(a, b):
# Проверка на деление на ноль
    if b == 0:
        print('На ноль делить нельзя!')
        return

    return a / b

# Запрос у пользователя двух чисел
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

# Запуск функции и вывод результата
result = division(a, b)

if result is not None:
    print('Результат деления:', result)