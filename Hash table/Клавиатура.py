# Всем известно, что со временем клавиатура изнашивается, и клавиши на ней начинают залипать.
# Конечно, некоторое время такую клавиатуру еще можно использовать, но для нажатий клавиш
# приходиться использовать большую силу. При изготовлении клавиатуры изначально для каждой
# клавиши задается количество нажатий, которое она должна выдерживать. Если знать эти величины
# для используемой клавиатуры, то для определенной последовательности нажатых клавиш можно определить,
# какие клавиши в процессе их использования сломаются, а какие – нет. Требуется написать
# программу, определяющую, какие клавиши сломаются в процессе заданного варианта эксплуатации клавиатуры.

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
b = int(input())
quan = list(map(int, input().split()))
quan = Counter(quan)
for i in range(len(a)):
    if a[i] < quan[i + 1]:
        print('yes')
    else:
        print('no')
