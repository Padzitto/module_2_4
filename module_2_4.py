numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создайте пустые списки primes и not_primes.
primes = []
not_primes = []

# Простое число — это натуральное число, которое делится без остатка только на единицу и на само себя!
# Соответственно, если число делится без остатка на какое-то еще другое число - оно Не простое!

for i in numbers:  # При помощи цикла for переберите список numbers.
    is_prime = True  # Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
    if i > 1:  # Учтите, что число 1 не является ни простым, ни составным числом (не учитываем число 1)
        # Проверка простоты числа (а точнее ищем Непростое)
        for j in range(2, i):  # Ищем делители числа в диапазоне от 2 до самого числа (не включительно)
            if i / j == i // j:  # Если i делится на j без остатка, то i / j и i // j дадут одинаковые значения
                # а если выполняется это условие, то число уже не простое!
                is_prime = False  # Меняем флаг на False, так как число не простое
                break  # Если при делении на первые числа выполняется условие, то перебирать другие числа j нет смысла,
                # т.к. число уже непростое, поэтому прерываем цикл.

        # Добавляем число в соответствующий список
        if is_prime:  # простое число (is_prime = Thrue)
            primes.append(i)  # Добавляем в список простых чисел
        else:  # не простое число (is_prime = False)
            not_primes.append(i)  # Добавляем в список не простых чисел

# Вывод результатов на экран
print("Primes:", primes)  # Выводим список простых чисел
print("Not Primes:", not_primes)  # Выводим список не простых чисел

# Примечание: Когда i = 2, диапазон range(2, 2) пустой, следовательно, цикл for не выполняется
# то есть цифры не перебираются в цикле и флаг Thrue остается на месте

# тест переноса в github
# тест для отправки из github  в pycharm
