from Building import Building
from Room import Room
from Student import Student
from Coures import Course       
from Enroilment import Enroilment  
from Subject import Subject
from Program import Program  


it_program = Program("IT", "เทคโนโลยีสารสนเทศ", "Information Technology")


Std001 = Student("013", "Jaason", "Borne", it_program)
b4 = Building("4", "คณะวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ")
r434 = Room("434", "ปฏิบัติการคอมพิวเตอร์ 2", b4)
r435 = Room("435", "ปฏิบัติการคอมพิวเตอร์ 3", b4) 

sj9023051 = Subject("9012071", "การเขียนโปรแกรมคอมพิวเตอร์ 2", "Computer Programming 2", 3, 2, 2)
sj9043011 = Subject("9043011", "ระบบสารสนเทศภูมิศาสตร์ 2", "Geographic Information Systems 2", 3, 2, 2)
sj9043073 = Subject("9043073", "การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข", "Application of Geoinformatics in Public Health", 3, 2, 2)
sj9042032 = Subject("9042032", "ระบบดาวเทียมนำทางบนโลกขั้นสูง", "Advanced Global Navigation Satellite System", 3, 2, 2)
sj9043051 = Subject("9043051", "การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ", "Modern Programming Language for Geoinformatics", 3, 2, 2)
sj9043021 = Subject("9043021", "การรับรู้จากระยะไกล 2", "Remote Sensing 2", 3, 2, 2)
sj9043091 = Subject("9043091", "สัมมนาทางภูมิสารสนเทศ 1", "Seminar in Geoinformatics 1", 1, 0, 2)


Course01 = Course(sj9023051, 1, r434)
Course02 = Course(sj9043011, 1, r435)
Course03 = Course(sj9043073, 1, r435)
Course04 = Course(sj9042032, 1, r434)
Course05 = Course(sj9043051, 1, r434)


em01 = Enroilment(2569, 1, Std001)
em01.add_course(Course01)
em01.add_course(Course02)
em01.add_course(Course03)
em01.add_course(Course04)
em01.add_course(Course05)


print(em01)
em01.listCourse ()