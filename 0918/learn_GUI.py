import tkinter as tk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        lstbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("输入错误", "请输入一个项目")

def delete_item():
    try:
        selected_index = lstbox.curselection()[0]
        lstbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("删除错误", "请选择要删除的项目")

# 创建窗口
root = tk.Tk()
root.title("高级GUI示例")

# 输入框
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

# 创建添加按钮
add_button = tk.Button(root, text="添加", command=add_item)
add_button.grid(row=0, column=1, padx=10, pady=10)

# 创建删除按钮
delete_button = tk.Button(root, text="删除", command=delete_item)
delete_button.grid(row=1, column=1, padx=10, pady=10)

# 创建列表框
lstbox = tk.Listbox(root, width=50, height=10)
lstbox.grid(row=1, column=0, padx=10, pady=10)

# 进入主循环
root.mainloop()
