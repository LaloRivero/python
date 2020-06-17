list_of_numbers = list(range(100))

pares = [number for number in list_of_numbers if number % 2 == 0]

student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']

students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
