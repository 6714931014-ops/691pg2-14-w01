from Subject import Subject
from Student import Student
from Room    import Room
from Lecturer import Lecturer
from Building import Building
s9012071 = Subject("9012071","การเขียนโปรแกรมคอมพิวเตอร์","computer",3,2,2)
s9043011 = Subject("9043011","ระบบสารสนเทศภูมิศาสตร์ 2","Geographic",3,2,2)
s9043073 = Subject("9043073","การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข","Application",3,2,2)
s9042032 = Subject("9042032","ระบบดาวเทียมนำทางบนโลกขั้นสูง","Advanced Global Navigation Satellite System",3,2,2)
s9043051 = Subject("9043051","การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ","Modern Programming Language for Geoinformatics",3,2,2)
s9043091 = Subject("9043091","สัมมนาทางภูมิสารสนเทศ 1","Seminar in Geoinformatics 1",1,0,2)
s9043021 = Subject("9043021","การรับรู้จากระยะไกล 2","Remote Sensing 2",3,2,2)

s6714931014 = Student("6714931014", "ธนกร", "เรียมชัยสงค์", "ภูมิสารสนเทศ")

ro1 = Room("426","4")
ro2 = Room("433","4")
ro3 = Room("434","4")
ro4 = Room("436","4")
ro5 = Room("437","4")

lc1 = Lecturer("ผู้ช่วยศาสตราจารย์","วิระ","ศรีมาลา","ภูมิสารสนเทศ")
lc2 = Lecturer("ผู้ช่วยศาสตราจารย์","คัมภีร์","ธีระเวช","ภูมิสารสนเทศ")
lc3 = Lecturer("อาจารย์","นิทัศน์","นิลฉวี","ภูมิสารสนเทศ")
lc4 = Lecturer("ผู้ช่วยศาสตราจารย์","ทบทอง","ชั้นเจริญ","ภูมิสารสนเทศ")
lc5 = Lecturer("อาจารย์","ภูมิพัฒน์","อุ่นบ้าน","ภูมิสารสนเทศ")

b4 = Building("4","คณะวิทยาการคอมพิวเตอร์และเทคโนโลยีสารสนเทศ")

print(s9012071)
print(s9043011)
print(s9043073)
print(s9042032)
print(s9043051)
print(s9043091)
print(s9043021)

print(s6714931014)

print(ro1)
print(ro2)
print(ro3)
print(ro4)
print(ro5)

print(lc1)
print(lc2)
print(lc3)
print(lc4)
print(lc5)

print(b4)