import random
from classes.course import Course
from classes.student import Student


with open ("courses.txt", "r") as f:
    lines = f.readlines();


data = []
for a in lines:
    if not a.startswith('#'):
        data.append(a.strip())

courses=[]

for d in data:
    x = d.split(' | ')
    if "Course" in x[0]:
        courses.append(Course(x[1],x[2]))
    elif "Running" in x[0]:
        courses[-1].add_running(int(x[1]))

for a in courses:
    print a