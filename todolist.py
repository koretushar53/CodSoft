import tkinter as tk
from tkinter import *


root = Tk()
root.title("To_Do_List")
root.config(bg="cyan")
root.geometry('400x400+950+150')


frame = tk.Frame(root)
frame.pack(pady=10)


task_box = tk.Listbox(frame, width=58, height=15)
task_box.pack(side=tk.LEFT)


sb = tk.Scrollbar(frame)
sb.pack(side=tk.RIGHT, fill=tk.Y)


task_box.config(yscrollcommand=sb.set)
sb.config(command=task_box.yview)


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


def addtask():
    task = task_entry.get()
    if task == "":
        alert("Please try to give some task")
    else:
        task_box.insert(tk.END, task)
        task_entry.delete(0, END)


def delete_task():
    try:
        selected_task_index = task_box.curselection()[0]
        print(f"Selected task index: {selected_task_index}") 
        task_box.delete(selected_task_index)
    except IndexError:
        alert("Please select a task to delete")


def alert(message):
    alert_window = tk.Toplevel()
    alert_window.title("Warning")
    alert_window.geometry("300x150+600+300")

    message_label = tk.Label(alert_window, text=message, padx=20, pady=20)
    message_label.pack()

    ok_button = tk.Button(alert_window, text="OK", command=alert_window.destroy, padx=20, pady=5)
    ok_button.pack()

    ok_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)  

add_button = Button(root, text="Add Task", command=addtask)
add_button.pack(pady=5)


delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)


if __name__ == "__main__":
    print("Thank you for visiting")
    root.mainloop()
    print("I HOPE YOUR TASKS ARE EASILY ACCESSIBLE TO YOU")
