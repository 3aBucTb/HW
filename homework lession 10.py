def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n - 1)


try:
    num = int(input("Введіть число: "))
    print_numbers(num)
except ValueError:
    print("Будь ласка, введіть ціле число.")


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


try:
    num = int(input("Введіть номер числа в послідовності Фібоначчі: "))
    fib_result = fibonacci(num)
    print(f"Число Фібоначчі з номером {num}: {fib_result}")
except ValueError:
    print("Будь ласка, введіть ціле число.")


    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    try:
        num = int(input("Введіть число для обчислення факторіалу: "))
        factorial_result = factorial(num)
        print(f"Факторіал числа {num}: {factorial_result}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")