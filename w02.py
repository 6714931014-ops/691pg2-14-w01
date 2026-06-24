class TouristAttraction:
    def __init__(self, name, province, description):
        self.name = name
        self.province = province
        self.description = description

    def show_info(self):
        print("ชื่อสถานที่:", self.name)
        print("จังหวัด:", self.province)
        print("รายละเอียด:", self.description)

place1 = TouristAttraction(
    "อุทยานแห่งชาติเขาคิชฌกูฏ",
    "จันทบุรี",
    "อุทยานแห่งชาติด้านการท่องเที่ยวเชิงธรรมชาติ"
)

place1.show_info()