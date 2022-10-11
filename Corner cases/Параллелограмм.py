#На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм. На перемене
# после урока они стали играть в игру: Петя называл координаты четырех точек в произвольном
# порядке, а Вася должен был ответить, являются ли эти точки вершинами параллелограмма.
# Вася, если честно, не очень понял тему про параллелограммы, и ему требуется программа,
# умеющая правильно отвечать на Петины вопросы. Напомним, что параллелограммом называется
# четырехугольник, противоположные стороны которого равны и параллельны.

n = int(input())
i = 0
while i < n:
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if (abs((x1 + x2) / 2 - (x3 + x4) / 2) < 10 ** -6 and
        abs((y1 + y2) / 2 - (y3 + y4) / 2) < 10 ** -6) or \
            (abs((x1 + x3) / 2 - (x2 + x4) / 2) < 10 ** -6 and
             abs((y1 + y3) / 2 - (y2 + y4) / 2) < 10 ** -6) or \
            (abs((x1 + x4) / 2 - (x3 + x2) / 2) < 10 ** -6 and
             abs((y1 + y4) / 2 - (y3 + y2) / 2) < 10 ** -6):
        print('YES')
        i += 1
        continue
    else:
        print('NO')
        i += 1


