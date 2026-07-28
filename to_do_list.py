import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="light yellow")

#-------------Functions----------------
def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Enter The Task !!!")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def del_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Select the task !!!")

def clear_all():
        if messagebox.askyesno("Clear","Are you sure you want to Clear the Listbox ??"):
            listbox.delete(0,tk.END)

def mark_done():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
         
        if not task.startswith("✓"):
            listbox.delete(index)
            listbox.insert(index,"✓" + task)
    except:
        messagebox.showwarning("Warning", "Select the task !!!")



def Exit_app():
    if messagebox.askyesno("Exit","Are you sure you want to exit the application ??"):
        root.destroy()

#-------------Frames----------------
main_frame=tk.Frame(root,bg="white",width=700,height=600,bd=2,relief="solid").pack(pady=100)

#-------------Labels----------------
tk.Label(root, text="My To-Do List",bg="light yellow", fg="black",font=('Times New Roman', 24, "bold")).place(x=320, y=20)
tk.Label(main_frame, text="Add Tasks :",bg="white", fg="black",font=('Times New Roman', 14, "bold")).place(x=100, y=140)

#-------------Entries----------------
entry = tk.Entry(main_frame, bg="white", fg="black", bd=1,relief="solid", font=('Times New Roman', 14))
entry.place(x=230, y=140)

#-------------Listbox----------------
listbox = tk.Listbox(main_frame, bg="white", fg="black",font=('Times New Roman', 14),height=12, width=40)
listbox.place(x=100, y=200)

#-------------Buttons----------------
tk.Button(main_frame, text="Add Task", command=add_task,bg="white", fg="green",font=('Times New Roman', 14), width=12).place(x=530, y=240)
tk.Button(main_frame, text="Delete Task", command=del_task,bg="white", fg="red",font=('Times New Roman', 14), width=12).place(x=530, y=300)
tk.Button(main_frame, text="Clear Tasks",command=clear_all,bg="white", fg="black",font=('Times New Roman', 14), width=12).place(x=530, y=420)
tk.Button(main_frame, text="Mark Done",command=mark_done,bg="white", fg="blue",font=('Times New Roman', 14), width=12).place(x=530, y=360)
tk.Button(root, text="Exit",command=Exit_app,bg="white", fg="black",font=('Times New Roman', 14), width=12).place(x=350, y=530)

root.mainloop()