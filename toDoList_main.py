#To-Do List

from tkinter import *

obj = Tk()
obj.title("To-Do List")
obj.geometry("500x600+400+100")
obj.configure(bg="#fff3e0")
obj.resizable(False, False)

#img = PhotoImage(file=r"C:\Users\NIDHI HARISH K\PycharmProjects\pythonProject\toDoList\image\to_do_bg.jpg")
#Label(obj, image=img).pack()

task_list = []

def addTask():
    task = entry.get()
    entry.delete(0, END)
    if task:
        with open(r"C:\Users\NIDHI HARISH K\OneDrive\Desktop\tasklist.txt.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open(r"C:\Users\NIDHI HARISH K\OneDrive\Desktop\tasklist.txt.txt", 'w') as tasky:
            for task in task_list:
                tasky.write(task+"\n")
        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_list
        with open(r"C:\Users\NIDHI HARISH K\OneDrive\Desktop\tasklist.txt.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open(r"C:\Users\NIDHI HARISH K\OneDrive\Desktop\tasklist.txt.txt", "w")
        file.close()


Label(obj, text="To-Do List", font="Cambria 30 italic", fg="#ff9800", bg="#fff3e0").place(x=170, y=30)
Label(obj, text="All tasks", font="Cambria 20 italic", fg="black", bg="#fff3e0").place(x=210, y=100)

frame = Frame(obj, width=500, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
entry = Entry(frame, width=18, font="arial 15", bd=0)
entry.place(x=10, y=7)
entry.focus()

button = Button(frame, text="ADD", font="arial 15 bold", width=5, bg="#e65100", fg="#fff", bd=3, command=addTask)
button.place(x=429, y=0)

frame1 = Frame(obj, bd=3, width=100, height=280, bg="white")
frame1.pack(pady=(230, 100))

listbox = Listbox(frame1, font=('arial', 12), width=52, height=16, bg="white", fg="#000000", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete_icon = PhotoImage(file=r"C:\Users\NIDHI HARISH K\OneDrive\Desktop\delete_icon.png")
#delete_icon.configure(height=50, width=50)
delete_button = Button(obj, text="DELETE", font="arial 10 bold", width=10, bg="#ff1744", fg="#fff", bd=3, command=deleteTask)
delete_button.place(x=210, y=520)
#Button(obj, image=delete_icon, bd=0).pack(side=BOTTOM, pady=13)

obj.mainloop()
