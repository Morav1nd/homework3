"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
которое содержит либо только английские, либо только русские буквы. 
"""
dictionary = {"a": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1,"д": 2, "к": 2, "л": 2, "м": 2, "п": 2, "у": 2,"б": 3, "г": 3, "ё": 3, "ь": 3, "я": 3,"й": 4, "ы": 4,"ж": 5, "з": 5, "х": 5, "ц": 5, "ч": 5,"ш": 8, "э": 8, "ю": 8,"ф": 10, "щ": 10, "ъ": 10,}

a = input()
score = 0
for i in a:
    for kay, point in dictionary.items():
        if i in kay:
            score += point
print(f"Стоимость слова: {score}")