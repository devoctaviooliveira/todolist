import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

#making window
window = tk.Tk()
window.title("My To do list")
window.configure(bg="#F0F0F0")
window.geometry("500x600")

frame_in_edition = None

def clear_entry(event, entry):
    if entry.get() == "Write your task here":
        entry.delete(0, tk.END)

def add_task():
  global frame_in_edition

  task = entry_task.get().strip()
  if task and task != "Write your task here":
    if frame_in_edition is not None:
      update_task(task)
      frame_in_edition = None
    else:
      add_new_task(task)
      entry_task.delete(0, tk.END)
  else:
    messagebox.showwarning("Invalid entry","Please, write a task")

def add_new_task(task):
  task_frame = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)
  task_frame.pack(fill=tk.X, padx=5, pady=5)

  task_label = tk.Label(task_frame, text=task, font=("Garamond", 16), bg="white", width=26, height=2, anchor="w")
  task_label.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

  edit_button = tk.Button(task_frame, image=edit_icon, command=lambda f=task_frame, l=task_label: prepare_edit(f, l), bg="white", relief=tk.FLAT)
  edit_button.pack(side=tk.RIGHT, padx=5)

  delete_button = tk.Button(task_frame, image=delete_icon, command=lambda f=task_frame: delete_task(f), bg="white", relief=tk.FLAT)
  delete_button.pack(side=tk.RIGHT, padx=5)

  checkButton = tk.Checkbutton(task_frame, command=lambda label=task_label: alternate_underlined(label))
  checkButton.pack(side=tk.RIGHT, padx=5)

  canvas_interior.update_idletasks()
  canvas.config(scrollregion=canvas.bbox("all"))

def prepare_edit(task_frame, task_label):
  global frame_in_edition
  frame_in_edition = task_frame
  entry_task.delete(0, tk.END)
  entry_task.insert(0, task_label.cget("text"))

def update_task(add_new_task):
  global frame_in_edition
  for widget in frame_in_edition.winfo_children():
    if isinstance(widget, tk.Label):
      widget.config(text=add_new_task)

def delete_task(task_frame):
  task_frame.destroy()
  canvas_interior.update_idletasks()
  canvas.config(scrollregion=canvas.bbox("all"))

def alternate_underlined(label):
    current_font = font.Font(font=label.cget("font"))
    if 'overstrike' in current_font.actual():
        new_font = current_font.copy()
        new_font['overstrike'] = not new_font['overstrike']
        label.config(font=new_font)

edit_icon = PhotoImage(file="edit.png").subsample(3, 3)
delete_icon = PhotoImage(file="delete.png").subsample(3, 3)

font_h1 = font.Font(family="Garamond", size="24", weight="bold")
h1 = tk.Label(window, text="My To Do List", font=font_h1, bg="#F0F0F0", fg="#333").pack(pady=20)

frame = tk.Frame(window, bg="#F0F0F0")
frame.pack(pady=10)

entry_task = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="grey", width=30)
entry_task.insert(0, "Write your task here")
entry_task.pack(side=tk.LEFT, padx=10)
entry_task.bind("<FocusIn>", lambda event: clear_entry(event, entry_task))

add_button = tk.Button(frame, command=add_task, text="Add task", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
add_button.pack(side=tk.LEFT, padx=10)

#making a frame for my to do list with scrollbar
frame_task_list = tk.Frame(window, bg="white")
frame_task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_task_list, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_task_list, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

window.mainloop()