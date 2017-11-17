import random
from classes.course import Course
from classes.student import Student


pi = Course("Programsko inzenjerstvo", "SARS503")
pi2017 = pi.add_running(2017)
pi2016 = pi.add_running(2016)
print pi
mat = Course("Matematika 1", "SER101")
mat.add_running(2017)
mat.add_running(2016)
print mat


