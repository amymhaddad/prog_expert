from functools import total_ordering
import imp


class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name 
        if grade < 0 or grade > 100:
            raise ValueError("Invalid grade")
        else:
            import pdb; pdb.set_trace()
            self.grade = grade 
        Student.all_students.append(self)

    @property
    def grade(self):
        return self.grade 

    # @grade.setter
    # def grade(self):
    #    # import pdb; pdb.set_trace()
    #     if self.grade < 0 or self.grade > 100:
    #         raise ValueError("Invalid grade")
    #     else:
    #         self.grade = self.grade 

    def calculate_average_grade(students):
        if len(students) == 0:
            return -1 

        total_grades = 0
        for student in students:
            total_grades += student.grade 
        return total_grades / len(students)

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1 
        total_grade = 0 
        for student in cls.all_students:
            total_grade += student.grade 
        return total_grade / len(cls.all_students)


    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None 
        
        best_grade = 0 
        best_student = ""
        for student in cls.all_students:
            if student.grade > best_grade:
                best_grade = student.grade 
                best_student = student.name 
        return best_student
        

student1 = Student("Antoine", 75)
#average = Student.get_average_grade()
#best_student = Student.get_best_student()
print(student1)

    