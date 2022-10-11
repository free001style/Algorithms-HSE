#Имеется N кг металлического сплава. Из него изготавливают заготовки массой K кг каждая.
# После этого из каждой заготовки вытачиваются детали массой M кг каждая (из каждой
# заготовки вытачивают максимально возможное количество деталей).Если от заготовок
# после этого что-то остается, то этот материал возвращают к началу производственного
# цикла и сплавляют с тем, что осталось при изготовлении заготовок. Если того сплава,
# который получился, достаточно для изготовления хотя бы одной заготовки, то из него
# снова изготавливают заготовки, из них – детали и т.д. Напишите программу, которая
# вычислит, какое количество деталей может быть получено по этой технологии из
# имеющихся исходно N кг сплава.

N, K, M = map(int, input().split())
quan_det = 0
while N >= K and K >= M:
    quan_det += (N // K) * (K // M)
    N -= M * (N // K) * (K // M)
print(quan_det)
