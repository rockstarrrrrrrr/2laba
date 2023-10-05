def sum_of_even_digits(n):
    even_digit_sum = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_digit_sum += digit
        n = n // 10
    return even_digit_sum


while True:
    try:
        num = int(input("Введите натуральное число (или 0 для выхода): "))

        if num < 0:
            print("Число должно быть натуральным.")
        elif num == 0:
            print("Программа завершена.")
            break
        else:
            result = sum_of_even_digits(num)
            print("Сумма четных цифр в числе:", result)
    except ValueError:
        print("Введите корректное число.")
