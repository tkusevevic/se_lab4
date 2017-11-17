class Student:
    def __init__(self,name,lastname,student_number):
        self.name = name
        self.lastname = lastname
        self.student_number = student_number
        self.classes = []
    def __str__(self):
        return "%s %s (%s)" %(self.name, self.lastname, 
                              self.student_number)
    def enrol(self, course):
        self.classes.append(course)
        course.students.append(self)