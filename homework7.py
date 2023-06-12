# Задача 1:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, 
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во 
# фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг 
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с 
# клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в 
# порядке и “Пам парам”, если с ритмом все не в порядке

# text = input("Введите текст стихотворения: ")
# vowels = 'ауоыэяюёие'
# previous_count = None
# separation = text.split()
# is_rhythm = True
# for word in separation:
#     count = 0
#     for char in word.lower():
#         if char in vowels:
#             count += 1

#     if previous_count is None:
#         previous_count = count
#     elif previous_count != count:
#         is_rhythm = False
#         break
#     else:
#         previous_count = count
        
# if is_rhythm:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

# Задача 2: Напишите функцию print_operation_table(operation, 
# num_rows=6, num_columns=6), которая принимает в качестве аргумента 
# функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов 
# таблицы, которые должны быть распечатаны. Нумерация строк и столбцов 
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной 
# операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for row in range(1, num_rows+1):
#         for column in range(1, num_columns+1):
#             res = operation(row, column)
#             print(res, end=" ")
#         print()

# print_operation_table(lambda x, y: x * y)
