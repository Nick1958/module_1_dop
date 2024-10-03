# Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]   # оценки учеников
grades[0]
count_1 = sum(grades[0])
average_1 = count_1/len(grades[0])
count_2 = sum(grades[1])
average_2 = count_2/len(grades[1])
grades[2]
count_3 = sum(grades[2])
average_3 = count_3/len(grades[2])
grades[3]
count_4 = sum(grades[3])
average_4 = count_4/len(grades[3])
grades[4]
count_5 = sum(grades[4])
average_5 = count_5/len(grades[4])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()          # так как оценки учеников в алфавитном порядке, множество преобразовал в список и отсортировал по алфавиту
print(students)          # вывел в консоль для облегчения создания словаря: ввод ключа (имя ученика) по алфавиту
average_score={'Aaron':average_1, 'Bilbo': average_2, 'Johnny':average_3, 'Khendrik':average_4, 'Steve':average_5}
print(average_score)

