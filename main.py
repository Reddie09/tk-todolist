import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-do-List")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30)

task_label = tk.Label(root, text="Tarefa:")
task_listbox = tk.Listbox(root, width=50, height=15)

scrollbar = tk.Scrollbar(root)



def add_task():
    task = task_entry.get()
    if task!="":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Tarefa Vazia!")

def delete_task():
    try:
        selected_task_index =  task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning","Você deve selecionar uma tarefa")
    

def clear_tasks():
    task_listbox.delete(0, tk.END)

add_btn = tk.Button(root, text="+", command=add_task)
delete_btn = tk.Button(root, text="X", command=delete_task)
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)

task_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.W)
task_entry.grid(row=0, column=1, padx=5, pady=10, sticky=tk.W)
add_btn.grid(row=0, column=2, padx=5, pady=10, sticky=tk.W)
delete_btn.grid(row=1, column=0, padx=5, pady=10)
clear_button.grid(row=1, column=1, padx=5, pady=10)
task_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
scrollbar.grid(row=2, column=3, sticky=tk.N+tk.S+tk.W)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

root.mainloop()
