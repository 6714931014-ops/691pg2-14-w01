import tkinter as tk
root = tk.Tk()
root.title ("Hello World")
root.geometry("400x300")

#tk.Label(root,text="9012071",font=("Arial",16)).pack(side="Bottom")

#tk.Label(root,text="Programing",font=("Arial",16)).pack(side="left")
#tk.Label(root,text="Computer",font=("Arial",16)).pack(side="riht")
#tk.Label(root,text="CSIT",font=("Arial",16)).pack(side="Bottom")

tk.Label(root,text="9012071",font=("Arial",16)).grid(row=0,column=0)
tk.Label(root,text="Programing",font=("Arial",16)).grid(row=0,column=1)
tk.Label(root,text="Computer Science Onformation Technology",font=("Arial",16)).grid(row=1,column=0)
tk.Label(root,text="CSIT",font=("Arial",16)).grid(row=1,column=1)
root.mainloop()
