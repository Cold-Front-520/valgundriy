x = []
razm = int(input("введите количество элементов и сами значения "))
for i in range(razm):
    x.append(int(input()))

print("это твой массив короче: ", x, "теперь введи циферку - скажу где она")
f = int(input())

for i in range(razm):
    if f == x[i]:
        slot = i + 1
        print("эта циферка стоит на ", slot, "слоте")

#   я подумал что для юзера будет полезнее видеть не конкретно "индекс"
#   а типо номер в списке. так будет типо понятнее для юзера. поэтому сделал i+1
