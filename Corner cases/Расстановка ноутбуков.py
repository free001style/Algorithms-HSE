#В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука.
# Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола.
# Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились,
# и площадь стола была минимальна.

a, b, c, d = map(int, input().split())
db = {}
mul = 1
mb_answer = ((max(a, c), b + d), (max(a, d), b + c),
             (a + c, max(b, d)), (a + d, max(c, b)))
for i in mb_answer:
    for x in i:
        mul *= x
    db[mul] = i
    mul = 1
min_key = min(db.keys())
print(*db[min_key])
