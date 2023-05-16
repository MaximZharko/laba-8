from PIL import Image


holidays = {
    "1" : "new_year.jpeg",
    "2" : "easter.jpeg",
    "3" : "victory_day.jpeg"
}

print("1. Новый год")
print("2. Пасха")
print("3. День победы")
print("Введи номер нужной открытки:")

num = input()
if num in holidays:
    with Image.open(holidays[num]) as img:
        img.show()
