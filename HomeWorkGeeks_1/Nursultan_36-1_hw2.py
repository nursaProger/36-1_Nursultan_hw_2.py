

while True:
    day = int(input("Введите ваш день рождения: "))
    month = input("Введите месяц рождения (цифрами): ")


    if month == '03':
        astro_sign = 'Рыбы' if (day < 21) else 'овен'
        print(f"вы по гороскопу: {astro_sign} ")

    elif month == '04':
        astro_sign = 'Овен' if (day < 21) else 'телец'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '05':
        astro_sign = 'Телец' if (day < 22) else 'близнецы'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '06':
        astro_sign = 'Близнецы' if (day < 22) else 'рак'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '07':
        astro_sign = 'Рак' if (day < 23) else 'лев'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '08':
        astro_sign = 'Лев' if (day < 22) else 'дева'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '09':
        astro_sign = 'Дева' if (day < 24) else 'весы'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '10':
        astro_sign = 'Весы' if (day < 24) else 'скорпион'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '11':
        astro_sign = 'Скорпион' if (day < 23) else 'стрелец'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '12':
        astro_sign = 'Стрелец' if (day < 23) else 'козерог'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '01':
        astro_sign = 'Козерог' if (day < 21) else 'водолей'
        print(f"вы по гороскопу: {astro_sign}")

    elif month == '02':
        astro_sign = 'Водолей' if (day < 21) else 'рыбы'
        print(f"вы по гороскопу: {astro_sign}")

    else:
        print("вы не правильно ввели день или месяц рождения :(")

    exit = input("если хотите выйти напишите 'stop' a если нет нажмите на любую клавишу: ")
    if exit == 'stop':
        print("exit..")
        break

    

















