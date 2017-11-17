import random
from classes.course import Course
from classes.student import Student

def get_courses_from_file(filename):
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

if __name__ == "__main__":
        courses = get_courses_from_file("courses.txt")
        for a in courses:
            print a