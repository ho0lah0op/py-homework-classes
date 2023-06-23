class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Student(Person):
    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
            print(f"Оценка {grade} за домашнее задание по курсу {course} добавлена для студента {student.name} {student.surname}")
        else:
            print("Ошибка")

# Откомментируйте строки ниже, чтобы добавить тест-данные для проверки работоспособности кода:

# Создание студента, лектора и ревьюера
student1 = Student('Aleksandr', 'Ivanov', 'male')
student1.courses_in_progress.append('Python')

lecturer1 = Lecturer('Elena', 'Smirnova')
lecturer1.courses_attached.append('Python')

reviewer1 = Reviewer('Kirill', 'Filippov')
reviewer1.courses_attached.append('Python')

# Выставление оценок ревьюером
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 10)

# Проверка оценок студента
print(f"Оценки студента {student1.name} {student1.surname} по курсу Python: {student1.grades['Python']}")
