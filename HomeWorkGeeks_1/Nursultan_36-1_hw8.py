results_dict = {}

with open('results.txt', 'r') as file:
    for i in file:
        parts = i.strip().split()
        if len(parts) == 2:
            name, score = parts
            results_dict[name] = int(score)

#Сортировка словаря
sort_results = dict(sorted(results_dict.items(), key=lambda item: item[1], reverse = True))

#Топ 3
print("Топ 3 лучших студента по оценке:")

top_3 = list(sort_results.items())[:3]
for name, score in top_3:
    print(f'{name}: {score}')

#средняя оценка студентов
total_score = sum(sort_results.values())
average_score = total_score / len(sort_results)
print(f'Средняя оценка: {average_score:.2f}')

#Создание нового текстового файла
with open('sorted_results.txt', 'w', encoding='UTF-8') as file:
    file.write("Результаты студентов:\n")
    for name, score in sort_results.items():
        file.write(f'{name}: {score}\n')

















