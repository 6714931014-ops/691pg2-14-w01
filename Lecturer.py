class Lecturer:
    def __init__(self,lctrank,lctname,lctlastname,lctmajor):
        self.lctrank = lctrank
        self.lctname = lctname
        self.lctlastname = lctlastname
        self.lctmajor = lctmajor
    def __str__(self) -> str:
        return f"{self.lctrank} {self.lctname} {self.lctlastname} {self.lctmajor}"