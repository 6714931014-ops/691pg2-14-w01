from Building import Building
from Room import Room

class Course:
    def __init__(self, subject, section, room: Room):
        self.__subject = subject
        self.__section = section
        self.__room = room

    def __str__(self) -> str:
        return f"วิชา: {self.subject}  เซกชัน: {self.section}  {self.room}"
    
    @property
    def subject(self):
        return self.__subject
    
    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def section(self):
        return self.__section
    
    @section.setter
    def section(self, value):
        self.__section = value

    @property
    def room(self):
        return self.__room
    
    @room.setter
    def room(self, value):
        self.__room = value