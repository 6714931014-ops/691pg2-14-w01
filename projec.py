"""
โปรแกรมเรียงลำดับข้อมูลสมาร์ทโฟน (Merge Sort) พร้อมหน้าจอ GUI (Tkinter)

1) คลาสต้นแบบ Smartphone มี 9 คุณสมบัติ
2) สร้างรายการวัตถุ 24 วัตถุ
3) ใช้อัลกอริธึม Merge Sort (เขียนเอง) เรียงลำดับและแสดงผล
4) GUI ด้วย Tkinter: เลือกคุณสมบัติ + เรียงน้อยไปมาก/มากไปน้อย
"""

# ---------------------------------------------------------------
# 1) คลาสต้นแบบ
# ---------------------------------------------------------------
class Smartphone:
    def __init__(self, code, brand, model, price, ram, storage,
                 battery, screen, rating):
        self.code = code          # 1 รหัสสินค้า
        self.brand = brand        # 2 ยี่ห้อ
        self.model = model        # 3 รุ่น
        self.price = price        # 4 ราคา (บาท)
        self.ram = ram            # 5 แรม (GB)
        self.storage = storage    # 6 หน่วยความจำ (GB)
        self.battery = battery    # 7 แบตเตอรี่ (mAh)
        self.screen = screen      # 8 ขนาดจอ (นิ้ว)
        self.rating = rating      # 9 คะแนนรีวิว (เต็ม 5)

    def as_tuple(self):
        return (self.code, self.brand, self.model, self.price, self.ram,
                self.storage, self.battery, self.screen, self.rating)


# ชื่อคอลัมน์ (ภาษาไทย) -> ชื่อคุณสมบัติ
FIELDS = {
    "รหัส": "code",
    "ยี่ห้อ": "brand",
    "รุ่น": "model",
    "ราคา (บาท)": "price",
    "RAM (GB)": "ram",
    "ความจุ (GB)": "storage",
    "แบตเตอรี่ (mAh)": "battery",
    "ขนาดจอ (นิ้ว)": "screen",
    "คะแนนรีวิว": "rating",
}

# ---------------------------------------------------------------
# 2) รายการวัตถุ 24 รายการ
# ---------------------------------------------------------------
def create_phones():
    return [
        Smartphone("P001", "Samsung", "Galaxy S24",      27900, 8,  256, 4000, 6.2, 4.6),
        Smartphone("P002", "Samsung", "Galaxy A55",      15900, 8,  256, 5000, 6.6, 4.4),
        Smartphone("P003", "Samsung", "Galaxy A15",       6490, 6,  128, 5000, 6.5, 4.1),
        Smartphone("P004", "Apple",   "iPhone 15",       32900, 6,  128, 3349, 6.1, 4.7),
        Smartphone("P005", "Apple",   "iPhone 15 Pro",   42900, 8,  256, 3274, 6.1, 4.8),
        Smartphone("P006", "Apple",   "iPhone SE",       16900, 4,   64, 2018, 4.7, 4.2),
        Smartphone("P007", "Xiaomi",  "Redmi Note 13",    7990, 8,  256, 5000, 6.67, 4.3),
        Smartphone("P008", "Xiaomi",  "Xiaomi 14",       28990, 12, 256, 4610, 6.36, 4.6),
        Smartphone("P009", "Xiaomi",  "Poco X6",         10990, 8,  256, 5100, 6.67, 4.4),
        Smartphone("P010", "OPPO",    "Reno 11",         14990, 8,  256, 5000, 6.7, 4.3),
        Smartphone("P011", "OPPO",    "A78",              7499, 8,  128, 5000, 6.43, 4.0),
        Smartphone("P012", "OPPO",    "Find X7",         35990, 16, 512, 5000, 6.78, 4.5),
        Smartphone("P013", "vivo",    "V30",             16999, 12, 256, 5000, 6.78, 4.4),
        Smartphone("P014", "vivo",    "Y100",             7999, 8,  256, 5000, 6.67, 4.1),
        Smartphone("P015", "vivo",    "X100",            29999, 12, 256, 5000, 6.78, 4.6),
        Smartphone("P016", "realme",  "12 Pro",          12999, 8,  256, 5000, 6.7, 4.3),
        Smartphone("P017", "realme",  "C67",              5499, 6,  128, 5000, 6.72, 3.9),
        Smartphone("P018", "realme",  "GT 5",            19999, 12, 256, 5240, 6.74, 4.5),
        Smartphone("P019", "HUAWEI",  "nova 12",         13990, 8,  256, 4600, 6.7, 4.2),
        Smartphone("P020", "HUAWEI",  "Pura 70",         32990, 12, 256, 5050, 6.6, 4.6),
        Smartphone("P021", "Google",  "Pixel 8",         24900, 8,  128, 4575, 6.2, 4.5),
        Smartphone("P022", "Google",  "Pixel 8a",        17900, 8,  128, 4492, 6.1, 4.4),
        Smartphone("P023", "Nothing", "Phone (2a)",      12990, 8,  128, 5000, 6.7, 4.3),
        Smartphone("P024", "Infinix", "Note 40",          6299, 8,  256, 5000, 6.78, 4.0),
    ]


# ---------------------------------------------------------------
# 3) อัลกอริธึมการเรียง: Merge Sort
# ---------------------------------------------------------------
def merge_sort(items, key, reverse=False):
    """เรียงลำดับด้วย Merge Sort (คืนลิสต์ใหม่ ไม่แก้ลิสต์เดิม)"""
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2
    left = merge_sort(items[:mid], key, reverse)
    right = merge_sort(items[mid:], key, reverse)
    return _merge(left, right, key, reverse)


def _merge(left, right, key, reverse):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        a, b = key(left[i]), key(right[j])
        # ใช้ <= / >= เพื่อให้การเรียงเสถียร (stable)
        take_left = (a >= b) if reverse else (a <= b)
        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort_phones(phones, attr, reverse=False):
    def key(p):
        v = getattr(p, attr)
        return v.lower() if isinstance(v, str) else v
    return merge_sort(phones, key, reverse)


# ---------------------------------------------------------------
# แสดงผลทางหน้าจอ Console
# ---------------------------------------------------------------
def print_table(phones, title=""):
    if title:
        print("\n" + title)
    header = f"{'รหัส':<6}{'ยี่ห้อ':<9}{'รุ่น':<15}{'ราคา':>8}{'RAM':>5}" \
             f"{'ความจุ':>8}{'แบต':>7}{'จอ':>6}{'รีวิว':>7}"
    print(header)
    print("-" * len(header))
    for p in phones:
        print(f"{p.code:<6}{p.brand:<9}{p.model:<15}{p.price:>8,}{p.ram:>5}"
              f"{p.storage:>8}{p.battery:>7}{p.screen:>6}{p.rating:>7}")


# ---------------------------------------------------------------
# 4) GUI (Tkinter)
# ---------------------------------------------------------------
def run_gui(phones):
    import tkinter as tk
    from tkinter import ttk

    root = tk.Tk()
    root.title("เรียงลำดับข้อมูลสมาร์ทโฟนด้วย Merge Sort")
    root.geometry("900x560")

    state = {"data": phones[:]}

    # ---- แถบควบคุม ----
    top = ttk.Frame(root, padding=10)
    top.pack(fill="x")

    ttk.Label(top, text="เรียงตาม:").pack(side="left")
    field_var = tk.StringVar(value="ราคา (บาท)")
    ttk.Combobox(top, textvariable=field_var, values=list(FIELDS),
                 state="readonly", width=16).pack(side="left", padx=6)

    order_var = tk.StringVar(value="asc")
    ttk.Radiobutton(top, text="น้อย → มาก", variable=order_var,
                    value="asc").pack(side="left", padx=4)
    ttk.Radiobutton(top, text="มาก → น้อย", variable=order_var,
                    value="desc").pack(side="left", padx=4)

    # ---- ตาราง ----
    cols = list(FIELDS)
    tree = ttk.Treeview(root, columns=cols, show="headings", height=22)
    for c in cols:
        tree.heading(c, text=c, command=lambda c=c: sort_by(c))
        tree.column(c, width=90, anchor="center")
    tree.column("รุ่น", width=130)
    tree.pack(fill="both", expand=True, padx=10, pady=(0, 6))

    status = tk.StringVar(value=f"จำนวนข้อมูล {len(phones)} รายการ (ยังไม่ได้เรียง)")
    ttk.Label(root, textvariable=status, padding=(10, 0, 10, 8)).pack(anchor="w")

    def refresh(data):
        tree.delete(*tree.get_children())
        for i, p in enumerate(data):
            tree.insert("", "end", values=p.as_tuple(),
                        tags=("odd" if i % 2 else "even",))
        tree.tag_configure("odd", background="#f2f6fb")

    def do_sort():
        label = field_var.get()
        desc = order_var.get() == "desc"
        state["data"] = sort_phones(state["data"], FIELDS[label], desc)
        refresh(state["data"])
        status.set(f"เรียงตาม '{label}' แบบ "
                   f"{'มากไปน้อย' if desc else 'น้อยไปมาก'} ด้วย Merge Sort")

    def sort_by(col):
        # คลิกหัวคอลัมน์: เลือกคอลัมน์นั้น และสลับทิศทางถ้าคลิกซ้ำ
        if field_var.get() == col:
            order_var.set("desc" if order_var.get() == "asc" else "asc")
        field_var.set(col)
        do_sort()

    def reset():
        state["data"] = phones[:]
        refresh(state["data"])
        status.set("แสดงข้อมูลตามลำดับเดิม")

    ttk.Button(top, text="เรียงลำดับ", command=do_sort).pack(side="left", padx=8)
    ttk.Button(top, text="รีเซ็ต", command=reset).pack(side="left")

    refresh(state["data"])
    root.mainloop()


# ---------------------------------------------------------------
if __name__ == "__main__":
    phones = create_phones()

    # แสดงผลทาง Console ก่อน (ตัวอย่าง: เรียงตามราคา น้อย -> มาก)
    print_table(phones, "ข้อมูลก่อนเรียง")
    print_table(sort_phones(phones, "price"), "หลังเรียงตามราคา (น้อย -> มาก) ด้วย Merge Sort")

    # เปิดหน้าจอ GUI
    try:
        run_gui(phones)
    except Exception as e:
        print("\nไม่สามารถเปิด GUI ได้:", e)