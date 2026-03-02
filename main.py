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

    def rate_lecture(self, lecturer, course, grade):
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
        if not self.grades:
            return 0
        total = 0
        count = 0
        for course in self.grades.values():
            for grade in course:
                total += grade
                count += 1
        return total / count


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
        if not self.grades:
            return 0
        total = 0
        count = 0
        for course in self.grades.values():
            for grade in course:
                total += grade
                count += 1
        return total / count

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
