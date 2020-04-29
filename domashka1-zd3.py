print('введи циферку')
a = []
n = int(input())
vova = 0
print('введи массив теперь!')
for i in range(n):
    boris = int(input())
    if boris == 0:
        a.insert(vova, boris)
        vova +=1

    else:
        a.append(boris)

print('я тут намешаю - смотри: ', a)


