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
            else:
                print("Недопустимое значение оценки. Оценка должна быть в пределах от 0 до 10.")
        else:
            print("Ошибка")

    def __str__(self):
        average_grade = round(self.average_grade(), 1)
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade}\n" \
               f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def average_grade(self):
        total_grades = sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values())
        return total_grades / len(self.grades)


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_taught = []

    def __str__(self):
        average_grade = round(self.average_grade(), 1)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def average_grade(self):
        total_grades = sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values())
        return total_grades / len(self.grades)


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
            else:
                print("Недопустимое значение оценки. Оценка должна быть в пределах от 0 до 10.")
        else:
            print("Ошибка")

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

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

# Завершенные курсы студенов
student1.finished_courses.append("Основы программирования")
student2.finished_courses.append("Основы программирования")

# Оценивание домашнего задания студента
reviewer1.rate_hw(student1, "Python", 8)
reviewer2.rate_hw(student1, "Git", 7)
reviewer1.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student2, "Git", 5)

# Оцениваем лектора студентом
student1.rate_lecturer(lecturer1, "Python", 9)
student1.rate_lecturer(lecturer2, "Git", 6)
student2.rate_lecturer(lecturer1, "Python", 10)
student2.rate_lecturer(lecturer2, "Git", 9)

print(f"Студенты\n{student1}\n\n{student2}\n")
print(f"Лекторы\n{lecturer1}\n\n{lecturer2}\n")
print(f"Ревьюеры\n{reviewer1}\n\n{reviewer2}\n")

# Сравнение студентов по средним оценкам
print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 = student2: {student1 == student2}")

# Сравнение лекторов по средним оценкам
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 = lecturer2: {lecturer1 == lecturer2}")