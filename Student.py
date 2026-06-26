class Student:
    def __init__(self,stuid,stuname,stulastname,stumajor):
        self.stuid = stuid
        self.stuname = stuname
        self.stulastname = stulastname
        self.stumajor = stumajor
    def __str__(self) -> str:
        return f"{self.stuid} {self.stuname} {self.stulastname} {self.stumajor}"