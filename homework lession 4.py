

#1. Створити програму, яка буде очікувати введення тексту від користувача і повідомляти — чи є введений текст “числом” чи “словом” (використати функцію cтрічки .isdigit() або .isalpha())

month = input("What month is today?")
if month.isdigit():
    print(f" {month} is not a word!You need to input a word!")
print(f" Today is {month.title()}")
day = input("What day is today?")
if day.isalpha():
    print(f" {day} is not a number!You need to input a number!")

#2. Якщо введений текст “число”, програма має також вказати чи є воно парним чи непарним.

a = int(day)
if a % 2 == 0:
    print(" Day is even number")
else:
    print(" Day is not even number")

#3. Якщо це “слово”, програма має вказати його довжину.

b = len(month)
print(f" In {month} is {b} letters")

#4. (необов'язкове виконання) Створити програму, яка буде очікувати введення тексту від користувача і повідомляти якого типу введені дані. Використати match, case і вбудовані функції Python

c = month
match c:
    case "March":
        print(f"Yes you are right it is {c}")
    case "November":
        print(f"No, it isnt {c}")
    case "September":
        print(f"No, it isnt {c}")
    case "May":
        print(f"No, it isnt {c}")
