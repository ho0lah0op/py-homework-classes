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

    def enroll_to_course(self, course, lecturer):
        self.courses_in_progress.append(course)
        lecturer.courses_taught.append(course)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_taught:
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
                print(f"Оценка {grade} за курс {course} добавлена для лектора {lecturer.name} {lecturer.surname}")
            else:
                print("Недопустимое значение оценки. Оценка должна быть в пределах от 0 до 10.")
        else:
            print("Ошибка")


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_taught = []


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
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
                print("Недопустимое значение оценки. Оценка должна быть в пределах от 0 до 10.")
        else:
            print("Ошибка")

# Откомментируйте строки ниже, чтобы добавить тест-данные для проверки работоспособности кода:

# Создание студентов, лекторов и ревьюеров
student1 = Student('Aleksandr', 'Ivanov', 'male')
student2 = Student("Lidiya", "Petrova", "female")
lecturer1 = Lecturer('Elena', 'Smirnova')
lecturer2 = Lecturer("Renat", "Akhmetov")
reviewer1 = Reviewer('Kirill', 'Filippov')
reviewer2 = Reviewer("Larisa", "Gorina")

# Добавление курсов ревьюерам
reviewer1.courses_attached.append("Python")
reviewer2.courses_attached.append("Git")

# Запись студента на курс и связывание с лектором
student1.enroll_to_course("Python", lecturer1)
student1.enroll_to_course("Git", lecturer2)
student2.enroll_to_course("Python", lecturer1)
student2.enroll_to_course("Git", lecturer2)

# Оцениваем домашнее задание студента
reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student1, "Git", 7)
reviewer1.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student2, "Git", 5)

# Оцениваем лектора студентом
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer2, "Git", 6)
student2.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Git", 9)
