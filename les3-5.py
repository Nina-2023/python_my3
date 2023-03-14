total = 0

while True:
    numbers = input('Введите числа: ')
    if numbers == 'q':
        break
    numbers = [int(x) for x in numbers.split()]
    total += sum(numbers)
    print('Сумма чисел:', total)