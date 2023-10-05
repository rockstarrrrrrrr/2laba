while True:
    try:
        n = int(input("Введите количество строк (n): "))
        m = int(input("Введите количество столбцов (m): "))

        if n < 0 or m < 0:
            print("Ошибка: Введите положительные значения для n и m.")
        else:
            break
    except ValueError:
        print("Ошибка: Введите целые числа для n и m.")


chessboard = []


for i in range(n):
    row = []
    for j in range(m):
        if (i + j) % 2 == 0:
            row.append(".")
        else:
            row.append("*")
    chessboard.append(row)


for row in chessboard:
    print(" ".join(row))
