first = int(input('Введите первое число: '))
second = int(input('Введите второе чмсло: '))
third = int(input('Ввелите третье число: '))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывыд: 2')
else:
    print('Вывод: 0')