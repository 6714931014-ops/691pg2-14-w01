class Building:
    def __init__(self,budid,budnameth):
        self.budid = budid
        self.budnameth = budnameth
    def __str__(self) -> str:
        return f"อาคาร{self.budid} ชื่ออาคาร{self.budnameth} "

     