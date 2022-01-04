age = int(input('Input your age: '))

if age < 18:
    print('Ждем тебя в школе')
elif age >= 18 and age <= 30:
    print('Иди в универ')
elif age > 30 and age < 40:
    print('Иди работай!')
    job = input('Что ты делаешь? ')
    if job == 'Бездельник':
        print('Так найди работу!')
    else:
        print('Ну тогда все норм...')
else:
    print('Ты уже стар')
    print('Пора вешаться')
print('end')
