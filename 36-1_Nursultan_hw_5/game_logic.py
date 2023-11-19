from decouple import config
import random

def play_game():
    my_money = int(config("MY_MONEY", default=1000))
    slots = list(range(1, 31))

    while True:
        print(f"Текущий баланс: ${my_money}")
        bet = int(input("Введите сумму ставки: "))

        winning_slot = random.choice(slots)
        selected_slot = int(input("Введите число от 1 до 30: "))

        print(f"Выпавшее число: {winning_slot}")

        if selected_slot == winning_slot:
            my_money += 2 * bet
            print(f"Поздравляем! Вы выиграли. Новый баланс: ${my_money}")
        else:
            my_money -= bet
            print(f"Увы, вы проиграли. Новый баланс: ${my_money}")

        if my_money <= 0:
            print("Игра окончена. Ваш баланс опустился до нуля.")
            break

        play_again = input("Хотите ли вы сыграть еще? (да/нет): ").lower()
        if play_again != "да":
            print(f"Игра окончена. Ваш баланс: {my_money}")
            break