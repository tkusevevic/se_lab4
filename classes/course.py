class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code
        self.runnings = []
    def __str__(self):
        return "%s [%s], (active: %d)"%(self.name, self.course_code, len(self.runnings))
    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]

    @classmethod
    def get_courses_from_file(self,filename):
        #opening file and reading
        with open (filename, "r") as f:
            lines = f.readlines()


            data = []
            #removing # and triming strings
            for a in lines:
                if not a.startswith('#'):
                    data.append(a.strip())

            courses=[]
            #for every string if starts with Course createing Course object
            #if starts with Running create Running course
            for d in data:
                x = d.split(' | ')
                if "Course" in x[0]:
                    courses.append(Course(x[1],x[2]))
                elif "Running" in x[0]:
                    courses[-1].add_running(int(x[1]))
        return courses

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