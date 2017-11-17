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