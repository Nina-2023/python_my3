def user_data(name, surname, year, city, email, phone):
# Вывод данных о пользователе в одну строку
    print("{name} {surname}, {year} года рождения, проживает в г. {city}, email: {email}, телефон: {phone}".format(name=name, surname=surname, year=year, city=city, email=email, phone=phone))

# Запрос у пользователя данных
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
phone = input('Введите телефон: ')

# Запуск функции
user_data(name, surname, year, city, email, phone)