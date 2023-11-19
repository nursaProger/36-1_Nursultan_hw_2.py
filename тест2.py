from тест import Person
import тест
from termcolor import cprint
import emoji
from decouple import config



friend = Person("Amir", 16)
print(friend)

print(тест.calculator(45, 45))
cprint("Hello", "green", "on_red")
print(emoji.emojize('Nursultan :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.emojize("Python is fun :red_heart:"))
print(config('DATABASE_URL'))

