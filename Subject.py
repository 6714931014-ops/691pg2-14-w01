class Subject:
    def __init__(self,subid,subnameth,subnameen,subunit,sublect,sublab):
        self.subid = subid
        self.subnameth = subnameth
        self.subnameen = subnameen
        self.subunit = subunit
        self.sublect = sublect
        self.sublab = sublab
    def __str__(self) -> str:
        return f"{self.subid} {self.subnameth} {self.subunit} ({self.sublect})-({self.sublab})"

     