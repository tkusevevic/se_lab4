import random
class StudentGenerator:
    NAMES=["Pero", "Djuro", "Marko", "Miki", "Ana", "Ivana"]
    LNAMES=["Peric", "Duric", "Markic", "Mikic", "Anic", "Ivic"]
    def __init__(self):
        pass
    def get_n(self, n):
        """returns n students in list"""
        students = []
        for i in range(n):
            name = random.choice(self.NAMES)
            lname = random.choice(self.LNAMES)
            number = random.randint(1000,10000)
            students.append(Student(name, lname, number))
        return students

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
        
        
class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.runnings = []
    def __str__(self):
        return "%s [%s]"%(self.name, self.course_code)
    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]

class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []
    def __str__(self):
        return "%s, %d (%d studenata)"%(
            self.course.name,
            self.year,
            len(self.students) )
    def print_students(self):
        """Ispisuje na ekran imena studenata upisanih u course"""
        pass
        
    
generator = StudentGenerator() 
students = generator.get_n(10)
for student in students:
    print student

pi = Course("Programsko inzenjerstvo", "SARS503")
pi2017 = pi.add_running(2017)
pi2016 = pi.add_running(2016)
mat = Course("Matematika 1", "SER101")
mat.add_running(2017)
mat.add_running(2016)

for student in students:
    student.enrol(pi2017)
    student.enrol(pi2016)
print pi2017
print pi2016
