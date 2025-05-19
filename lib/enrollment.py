from datetime import datetime

class Course:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []  # list of Enrollment instances
        self._grades = {}       # dictionary {Enrollment: grade}

    def course_count(self):
        return len(self._enrollments)

    def aggregate_average_grade(self):
        total_grades = sum(self._grades.values())
        num_courses = len(self._grades)
        return total_grades / num_courses if num_courses > 0 else 0

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

    def add_grade(self, enrollment, grade):
        self._grades[enrollment] = grade


class Enrollment:
    all = []

    def __init__(self, student, course, enrollment_date=None):
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date or datetime.now()
        Enrollment.all.append(self)
        # Link enrollment to student
        self.student.add_enrollment(self)

    def get_enrollment_date(self):
        return self.enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count