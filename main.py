class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finishedCourses = []
        self.coursesInProgress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.averageGrade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.coursesInProgress)}'
                f'\nЗавершенные курсы: {", ".join(self.finishedCourses)}')

    def rateLecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.coursesAttached and course in self.coursesInProgress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.averageGrade() == other.averageGrade()

    def averageGrade(self):    # Расчет средней оценки конкретного студента по всем курсам
        return averageGradeAllCourse(self.grades)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coursesAttached = []

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}')

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.averageGrade()}')

    def averageGrade(self):    # Расчет средней оценки конкретного лектора по всем курсам
        return averageGradeAllCourse(self.grades)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.averageGrade() == other.averageGrade()

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rateReviewer(self, student, course, grade):
        if isinstance(student, Student) and course in self.coursesAttached and course in student.coursesInProgress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def averageGradeAllCourse(gradesDict):    # Расчет средней оценки конкретного студента/лектора по всем курсам
    if not gradesDict:
        return 0
    total = 0
    count = 0
    for course in gradesDict.values():
        for grade in course:
            total += grade
            count += 1
    return total / count

def averageGradeStudentForCourse(students, course):     # Расчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count else 0

def averageGradeLecturerForCourse(lecturers, course):   # Расчет средней оценки за лекции всех лекторов в рамках конкретного курса
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count else 0

# Создание экземпляров классов и добавление тестовых данных
student1 = Student('Иван', 'Иванов', 'мужчина')
student2 = Student('Мария', 'Иванова', 'женщина')

lecturer1 = Lecturer('Евгений', 'Фролов')
lecturer2 = Lecturer('Дмитрий', 'Шипулин')

reviewer1 = Reviewer('Станислав', 'Попов')
reviewer2 = Reviewer('Антон', 'Иванов')

student1.coursesInProgress = ['Python', 'Java']
student1.finishedCourses = ['Git']
student2.coursesInProgress = ['Python', 'SQL']
student2.finishedCourses = ['Java']

lecturer1.coursesAttached = ['Python', 'Java']
lecturer2.coursesAttached = ['Python', 'SQL']

reviewer1.coursesAttached = ['Python', 'Java']
reviewer2.coursesAttached = ['Python', 'SQL']

# Вызов методов rateReviewer и rateLecture
reviewer1.rateReviewer(student1, 'Python', 9)
reviewer1.rateReviewer(student1, 'Java', 8)
reviewer2.rateReviewer(student2, 'Python', 10)
reviewer2.rateReviewer(student2, 'SQL', 9)

student1.rateLecture(lecturer1, 'Python', 4)
student1.rateLecture(lecturer1, 'Java', 8)
student2.rateLecture(lecturer2, 'Python', 10)
student2.rateLecture(lecturer2, 'SQL', 9)

# Вывод информации о студентах и менторах (лекторы, ревьюверы)
print('\nИнформация о студентах:')
print(f'{student1}')
print(f'\n{student2}')

print('\nИнформация о лекторах:')
print(f'{lecturer1}')
print(f'\n{lecturer2}')

print('\nИнформация о ревьюерах:')
print(f'{reviewer1}')
print(f'\n{reviewer2}')

# Сравнение студентов и лекторов при помощи магического метода
print('\nСравнение студентов (средние оценки):')
print(f'student1 == student2: {student1 == student2}')
print(f'student1 != student2: {student1 != student2}')

print('\nСравнение лекторов (средние оценки):')
print(f'lecturer1 == lecturer2: {lecturer1 == lecturer2}')
print(f'lecturer1 != lecturer2: {lecturer1 != lecturer2}')

# Вызов функций для подсчета средних оценок по курсу для студентов и лекторов
studentsList = [student1, student2]
lecturersList = [lecturer1, lecturer2]

courseName = 'Python'
averageStudent = averageGradeStudentForCourse(studentsList, courseName)
averagelecturer = averageGradeLecturerForCourse(lecturersList, courseName)

print(f'\nСредняя оценка за ДЗ по курсу {courseName}: {averageStudent}')
print(f'Средняя оценка за лекции по курсу {courseName}: {averagelecturer}')