# Клуб Юных Хакеров организовал на своем сайте форум. Форум имеет следующую структуру: каждое сообщение
# либо начинает новую тему, либо является ответом на какое-либо предыдущее сообщение и принадлежит
# той же теме. После нескольких месяцев использования своего форума юных хакеров заинтересовал вопрос
# - какая тема на их форуме наиболее популярна. Помогите им выяснить это.

n = int(input())
message = []
for i in range(n):
    num = int(input())
    if num == 0:
        topic = input()
        message.append(topic)
        mes = input()
    else:
        mes = input()
        message.append(message[num - 1])
print(max(message, key=message.count))
