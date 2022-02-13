 

class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name 
        #Want to prevent people from setting invalid grades; i want to make this attr private so use undersscore so this attr can't be modified outside of class
        self._grade = grade
        Student.all_students.append(self)
        
    @property
    def grade(self):
        return self._grade 

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("Invalid grade")
        #Set the private attr IF new_grade is w/in boundaries
        self.grade = new_grade 

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
        return int(total_grade / len(cls.all_students))


    @classmethod
    def get_best_student(cls):
        best_student = None

        for student in cls.all_students:
            if best_student == None or student.grade > best_student.grade:
                best_student = student
        return best_student
      
student1 = Student("ANtoine", 75)
student2 = Student("Tim", 81)
average = Student.get_average_grade()
best_student = Student.get_best_student()
print(average, best_student.name)
    
