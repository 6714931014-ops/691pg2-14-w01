import tkinter as tk
from Subject import Subject

window = tk.Tk()
window.title("ตารางเรียน")
window.geometry("1100x650")

custom_font = ("Arial", 12)



monday_subjects = [
    Subject("9043011-55", 1, "ระบบสารสนเทศภูมิศาสตร์ 2", "436", "#FFF176"),
    "",
    Subject("9043073-59", 1, "การประยุกต์ภูมิสารสนเทศด้านการสาธารณสุข", "436", "#FFF176")
]

tuesday_subjects = [
    Subject("9042032-59", 1, "ระบบดาวเทียมนำทางบนโลกขั้นสูง", "437", "#FFCC80"),
    ""
]

wednesday_subjects = [
    Subject("9043051-55", 1, "การเขียนโปรแกรมภาษาสมัยใหม่สำหรับภูมิสารสนเทศ", "433", "#A5D6A7"),
    ""
]

thursday_subjects = [
    "",
    "",
    "",
    "",
    Subject("9043091-55", 1, "สัมมนาทางภูมิสารสนเทศ 1", "426", "#CE93D8"),
]

friday_subjects = [
    Subject("9012071-54", 1, "การเขียนโปรแกรมคอมพิวเตอร์ 2", "434", "#80CBC4"),
    "",
    Subject("9043021-55", 1, "การรับรู้จากระยะไกล 2", "433", "#80CBC4")
]





monday_frame = tk.LabelFrame(window, text="วันจันทร์", font=custom_font)
monday_frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

tuesday_frame = tk.LabelFrame(window, text="วันอังคาร", font=custom_font)
tuesday_frame.grid(row=2, column=0, padx=10, pady=5, sticky="w")

wednesday_frame = tk.LabelFrame(window, text="วันพุธ", font=custom_font)
wednesday_frame.grid(row=3, column=0, padx=10, pady=5, sticky="w")

thursday_frame = tk.LabelFrame(window, text="วันพฤหัสบดี", font=custom_font)
thursday_frame.grid(row=4, column=0, padx=10, pady=5, sticky="w")

friday_frame = tk.LabelFrame(window, text="วันศุกร์", font=custom_font)
friday_frame.grid(row=5, column=0, padx=10, pady=5, sticky="w")



def create_subject_label(frame, subjects):
    column = 0
    for subject in subjects:
        if isinstance(subject, Subject):
            if subject.room:
                text = f"{subject.code}, {subject.section} \n{subject.name} \n{subject.room}"
            else:
                text = f"{subject.code}\n{subject.name}"
            label = tk.Label(frame, text=text, padx=20, pady=10, borderwidth=1, relief="solid", bg=subject.color, font=custom_font)
            label.grid(row=0, column=column)
            column += 2
        else:
            label = tk.Label(frame, text="", padx=0, pady=0, borderwidth=0, relief="solid")
            label.grid(row=0, column=column, padx=40, pady=5)
            column += 2

create_subject_label(monday_frame, monday_subjects)
create_subject_label(tuesday_frame, tuesday_subjects)
create_subject_label(wednesday_frame, wednesday_subjects)
create_subject_label(thursday_frame, thursday_subjects)
create_subject_label(friday_frame, friday_subjects)

window.mainloop()