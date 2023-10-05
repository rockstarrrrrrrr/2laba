import string

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_top_three_largest_or_count_vowels(input_arg):
    if isinstance(input_arg, set):
        if len(input_arg) >= 3:
            sorted_values = sorted(input_arg, reverse=True)
            return sorted_values[:3]
        else:
            return list(input_arg)
    elif isinstance(input_arg, str):
        # Удаление знаков препинания
        input_arg = input_arg.translate(str.maketrans('', '', string.punctuation))
        vowels = "AEIOUaeiou"
        vowel_count = sum(1 for char in input_arg if char in vowels)
        return f"Количество гласных: {vowel_count}"
    elif isinstance(input_arg, (int, float)):
        if is_prime(int(input_arg)):
            return f"{int(input_arg)} - простое число"
        else:
            return f"{int(input_arg)} - не простое число"
    else:
        return "Аргумент не является множеством, строкой или числом"

while True:

    user_input = input("Введите множество элементов, строку или число: ")

    try:
        if ',' in user_input:
            input_arg = set(map(int, user_input.split(',')))
        elif '.' in user_input:
            input_arg = float(user_input)
        else:
            input_arg = int(user_input)
    except ValueError:

        input_arg = user_input

    result = find_top_three_largest_or_count_vowels(input_arg)
    print(result)
