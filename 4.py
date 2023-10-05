while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 / num2
        print("Результат деления:", result)

    except ZeroDivisionError:
        print("Ошибка: Деление на ноль!")
    except ValueError:
        print("Ошибка: Введите числовые значения!")
    finally:
        print("Завершение попытки.")

print("Программа завершена.")

