import math

def cosh_maclaurin(x, n_terms):
    """
    Вычисляет значение cosh(x) с использованием ряда Маклорена.

    :param x: Значение аргумента.
    :param n_terms: Количество членов ряда для вычисления.
    :return: Значение cosh(x).
    """
    result = 1
    for n in range(1, n_terms + 1):
        term = (x ** (2 * n)) / math.factorial(2 * n)
        result += term
    return result

def ln_maclaurin(x, n_terms):
    """
    Вычисляет значение ln(1+x) с использованием ряда Маклорена.

    :param x: Значение аргумента.
    :param n_terms: Количество членов ряда для вычисления.
    :return: Значение ln(1+x).
    """
    if x <= -1 or x == 0:
        raise ValueError("Значение x должно быть в диапазоне (-1, 1] и не равно 0.")

    result = 0
    for n in range(1, n_terms + 1):
        term = (-1) ** (n + 1) * (x ** n) / n
        result += term
    return result


def main():
    while True:
        print("\nМеню:")
        print("1. Вычислить cosh(x)")
        print("2. Вычислить ln(1+x)")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            x = float(input("Введите значение x: "))
            n_terms = 10
            result = cosh_maclaurin(x, n_terms)
            print(f"cosh({x}) = {result}")
        elif choice == '2':
            x = float(input("Введите значение x: "))
            n_terms = 10
            try:
                result = ln_maclaurin(x, n_terms)
                print(f"ln(1+{x}) = {result}")
            except ValueError as e:
                print(e)
        elif choice == '3':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()
