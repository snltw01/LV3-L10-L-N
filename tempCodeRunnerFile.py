import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

class log_in(tk.Tk):
    def __init__(self):
        self.geometry('500x500+100+200')
        self.title('Login')
        
        self.ensure_files_exist()

        self.create_login_screen()

        self.acc_file = "acc.txt"
        self.info_file = "info.txt"
        
        
    def ensure_files_exist(self):
        """Tạo các file nếu chưa tồn tại"""
        for file in [self.acc_file, self.info_file]:
            if not os.path.exists(file):
                with open(file, 'w', encoding='utf-8') as f:
                    pass


    def create_login_screen(self):
        """Tạo giao diện đăng nhập"""
        # Xóa các widget cũ
        for widget in self.frame1.winfo_children():
            widget.destroy()

        self.frame1=tk.Frame(self)
        self.frame1.pack()

        # lb0=tk.Label(self.frame1,image=self.tk_image)
        # lb0.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        lb1=tk.Label(self.frame1,text='LOG IN',font=('Arial',20,"bold"))
        lb1.grid(row=1,column=0,columnspan=2,pady=15)

        lb2=tk.Label(self.frame1,text="Name",font=('Arial',13 ))
        lb2.grid(row=2,column=0,pady=10)

        en1=tk.Entry(self.frame1,font=('Arial',13))
        en1.grid(row=2,column=1,padx=14,pady=3)

        lb3=tk.Label(self.frame1,text='Password',font=('Arial',13))
        lb3.grid(row=3,column=0)

        en2=tk.Entry(self.frame1,show="*",font=("Arial",13))
        en2.grid(row=3,column=1,padx=14,pady=3)

        but1=tk.Button(self.frame1,text='Creat new accounts',font=('Arial',13),command=self.create_register_screen)
        but1.grid(row=4,column=0,pady=10)

        but2=tk.Button(self.frame1,text='Log in',font=('Arial',13))
        but2.grid(row=4,column=1,pady=10)


Form1=log_in()
Form1.mainloop()