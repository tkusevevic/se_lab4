import random
from classes.course import Course
from classes.student import Student


if __name__ == "__main__":
        courses = Course.get_courses_from_file("courses.txt")
        for a in courses:
            print a
        print("Hello")