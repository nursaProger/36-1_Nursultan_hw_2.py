while True:
    word = input("Введите любое слово на латинице или кириллице: ").lower()
    letters_1 = 'euioa'
    letters_2 = 'qwrtypasdfghjklzxcvbnm'
    rus_letters1 = 'йуеыаоэяию'
    rus_letters2 = 'цкнгшщзхъфвпрлджчсмтьб'
    gls = 0
    sgl = 0

    for letter in word:
        if letter in letters_1:
            gls = gls + 1
        elif letter in letters_2:
            sgl = sgl + 1
        elif letter in rus_letters1:
            gls = gls + 1
        elif letter in rus_letters2:
            sgl = sgl + 1

        percent = round(gls * 100 / len(word), 1)
        percent2 = round(sgl * 100 / len(word), 1)

    len_word = len(word)
    if word == 'stop':
        print("пока...")
        break


    print(f"Слово: {word}")
    print(f"Количество букв: {len_word}")
    print(f"Гласных букв: {gls}")
    print(f"Согласных букв: {sgl}")
    print(f"Cогласные/Гласные: {percent}% / {percent2}% ")

