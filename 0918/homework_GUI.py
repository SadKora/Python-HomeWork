# 一个联系人管理系统
import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contact = f"Name: {name}, Phone: {phone}, Email: {email}"
        listbox.insert(tk.END, contact)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("输入错误", "请填写所有字段")

def delete_contact():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("删除错误", "请选择要删除的联系人")

# 创建主窗口
root = tk.Tk()
root.title("联系人管理系统")

# 创建标签和输入框
name_label = tk.Label(root, text="姓名:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="电话:")
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="邮箱:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# 创建添加和删除按钮
add_button = tk.Button(root, text="添加联系人", command=add_contact)
add_button.grid(row=3, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="删除联系人", command=delete_contact)
delete_button.grid(row=3, column=1, padx=10, pady=10)

# 创建列表框
listbox = tk.Listbox(root, width=60, height=10)
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# 进入主循环
root.mainloop()
