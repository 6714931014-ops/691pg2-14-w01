from Student import Student
from Coures import Course  

class Enroilment:
    def __init__(self, year, semester, student):
        self.__year = year
        self.__semester = semester
        self.__student = student
        self.__course_list = []  

    def __str__(self) -> str:
        return f"ปีการศึกษา: {self.year}  เทอม: {self.semester}  นักศึกษา: {self.student}  วิชาที่ลงเรียน: {len(self.course_list)} วิชา"
    
    def add_course(self, course: Course):
        self.__course_list.append(course)
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, value):
        self.__year = value
    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, value):
        self.__semester = value
    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, value):
        self.__student = value
    @property
    def course_list(self):
        return self.__course_list 
 
    @property
    def course_list(self):
        return self.__course_list
    def listCourse(self):
        for course in self.__course_list:
            print(course)