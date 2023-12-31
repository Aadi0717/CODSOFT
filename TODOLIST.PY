import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []
        self.task_entry = ttk.Entry(root, font=('Arial', 12), width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=('Arial', 12), width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.mark_complete_button = ttk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.mark_complete_button.grid(row=2, column=0, padx=10, pady=10)
        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)
        self.load_tasks()
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = f"{task_text} ({timestamp})"
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks[task_index]
            if "(Completed)" not in task:
                self.tasks[task_index] = f"{task} (Completed)"
                self.update_task_listbox()
                self.save_tasks()
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()
            self.save_tasks()
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task}\n")
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
                self.update_task_listbox()
        except FileNotFoundError:
            pass
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
