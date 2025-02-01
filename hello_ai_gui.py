import tkinter as tk
from tkinter import simpledialog, messagebox

def greet_user():
    # 创建一个简单的输入对话框
    name = simpledialog.askstring("输入", "请输入你的名字:")
    if name:
        # 显示问候信息
        messagebox.showinfo("问候", f"你好，{name}！很高兴认识你！")

# 创建主窗口
root = tk.Tk()
root.title("AI 问候程序")

# 创建一个按钮，点击后调用greet_user函数
greet_button = tk.Button(root, text="开始问候", command=greet_user)
greet_button.pack(pady=20)

# 运行主循环
root.mainloop() 