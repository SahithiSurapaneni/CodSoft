import tkinter as tk

def add_task():
    task = entry.get()
    if task.strip():
        tasks.append(task)
        update_listbox()

def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = tasks[index]
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Task")

        edit_entry = tk.Entry(edit_window, font=("Calibri", 14), bd=5)
        edit_entry.pack(padx=10, pady=10)
        edit_entry.insert(0, task)

        def save_changes():
            new_task = edit_entry.get()
            if new_task.strip():
                tasks[index] = new_task
                update_listbox()
                edit_window.destroy()

        save_button = tk.Button(edit_window, text="Save",bg="grey",fg="black", font=("Calibri", 12), command=save_changes)
        save_button.pack(padx=10, pady=5)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks[index]
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

tasks = []

root = tk.Tk()
root.title("To-Do List")

heading_label = tk.Label(root, text="Todo List",bg="grey", fg="black", font=("Comic Sans MS", 24), padx=180, pady=10)
heading_label.grid(row=0, column=0, columnspan=3)

heading_label = tk.Label(root, text="Add Items", font=("Calibri", 20, "bold"), padx=50, pady=5)
heading_label.grid(row=1, column=0, columnspan=1)

entry = tk.Entry(root, font=("calibri", 14), bd=5)
entry.grid(row=2, column=0, padx=10, pady=5)

add_button = tk.Button(root, text="Submit", bg="green",fg="black",font=("calibri", 12), width=12, command=add_task)
add_button.grid(row=2, column=1, padx=10, pady=5)

listbox = tk.Listbox(root, font=("Calibri", 14), bd=5)
listbox.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

edit_button = tk.Button(root, text="Edit",bg="grey",fg="black", font=("Calibri", 12), width=10, command=edit_task)
edit_button.grid(row=3, column=1, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete", bg="red",fg="black",font=("Calibri", 12), width=10, command=delete_task)
delete_button.grid(row=3, column=2, padx=5, pady=5)

update_listbox()

root.mainloop()
