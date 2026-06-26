class Room:
    def __init__(self,romid,romnameth):
        self.romid = romid
        self.romnameth = romnameth
    def __str__(self) -> str:
        return f"ห้อง{self.romid} อาคาร{self.romnameth} "

     