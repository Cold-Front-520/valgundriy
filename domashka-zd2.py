print('введите размер массива (желательно больше двух)')
a = []
n = int(input())
if n <= 2:
    print('не ну ты не быкуй да')
else:
    print('красава, теперь вводи элементы массива')
    for penis in range(n):
        a.append(int(input()))
a.sort()
print('всё норм! вот твой массив: ', a)
print('вот 2 максимальных числа: ', a[-1], a[-2])
print(a)

