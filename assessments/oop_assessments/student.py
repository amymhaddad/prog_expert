class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("Invalid grade")
        self._grade = new_grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        return round(sum([student.grade for student in students]) / len(students))

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1
        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        best_student = None
        for student in cls.all_students:
            if best_student == None or student.grade > best_student.grade:
                best_student = student
        return best_student
