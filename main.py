import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

class log_in(tk.Tk):
    def __init__(self):
        image = Image.open('IMG/lll.png').resize((200,200))
        self.tk_image = ImageTk.PhotoImage(image)
        self.title('Login')
        self.geometry('500x500+100+200')
        self.creat_widget()

        self.acc_file = "acc.txt"
        self.info_file = "info.txt"
        
        self.ensure_files_exist()



    def creat_widget(self):
        self.frame1=tk.Frame(self)
        self.frame1.pack()

        lb0=tk.Label(self.frame1,image=self.tk_image)
        lb0.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
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

    def ensure_files_exist(self):
        """Tạo các file nếu chưa tồn tại"""
        for file in [self.acc_file, self.info_file]:
            if not os.path.exists(file):
                with open(file, 'w', encoding='utf-8') as f:
                    pass

    def create_register_screen(self):
        for widget in self.frame1.winfo_children():
           widget.destroy()
        
        
        self.frame2=tk.Frame(self)
        self.frame2.pack()

        lb1=tk.Label(self.frame2,text="ĐĂNG KÍ TÀI KHOẢN",fon=('Arial',30,'bold'))
        lb1.grid(row=0,column=1,padx=10,pady=10)



    





class Register(tk.Toplevel):
    def __init__(self):
        super().__init__()
        image = Image.open('IMG/lll.png').resize((200,200))
        self.tk_image = ImageTk.PhotoImage(image)
        self.title('Form Đăng Kí')
        self.geometry('700x700+100+100')
        self.nation=['Việt Nam','Hàn Quốc','Nhật Bản','Mỹ',"Trung Quốc","Lào","Nga"]
        self.Creat_widget()

        self.current_bg_color='white'
        self.current_size=9
        self.current_style='Arial'
        self.current_fg_color='black'



    def quit(self):
        self.destroy()

    def login(self):
        messagebox.showinfo('Thông Báo','Đã đăng nhập')

    

    def Creat_widget(self):
        self.frame1=tk.Frame(self)
        self.frame1.pack()

        lb1=tk.Label(self.frame1, image=self.tk_image)
        lb1.grid(row=0,column=1,columnspan=3,padx=80)
        lb2=tk.Label(self.frame1,text='Form Đăng Kí')
        lb2.grid(row=1,column=1,columnspan=3,pady=25)

        lb3=tk.Label(self.frame1,text="Họ và tên")
        lb3.grid(row=2,column=0)

        en1=tk.Entry(self.frame1)
        en1.grid(row=2,column=1,padx=30,pady=20)

        lb4=tk.Label(self.frame1,text='Địa chỉ')
        lb4.grid(row=2,column=2)

        en2=tk.Entry(self.frame1)
        en2.grid(row=2,column=3,padx=30,pady=20)

        lb5=tk.Label(self.frame1,text="Ngày sinh")
        lb5.grid(row=3,column=0)
        
        en3=tk.Entry(self.frame1)
        en3.grid(row=3,column=1,padx=30,pady=20)

        lb6=tk.Label(self.frame1,text="Email")
        lb6.grid(row=3,column=2)

        en4=tk.Entry(self.frame1)
        en4.grid(row=3,column=3,padx=30,pady=20) 

        lb7=tk.Label(self.frame1,text="Quốc tịch")
        lb7.grid(row=4,column=0)
        
        combobox=ttk.Combobox(self.frame1,values=self.nation, state='readonly')
        combobox.grid(row=4,column=1,padx=30,pady=20)

        lb8=tk.Label(self.frame1,text="Số Điện thoại")
        lb8.grid(row=4,column=2)

        en5=tk.Entry(self.frame1)
        en5.grid(row=4,column=3,padx=30,pady=20)

        but1=tk.Button(self.frame1,text='Register',command=self.login)
        but1.grid(row=5,column=1,columnspan=1)

        but2=tk.Button(self.frame1,text='Quit',command=quit)
        but2.grid(row=5,column=2,columnspan=1)

        mainbar=tk.Menu(self)
        theme=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='theme',menu=theme)
        theme.add_command(label='Light',command=self.theme_white)
        theme.add_command(label='Dark',command=self.theme_dark)

        sizesetting=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='Size Setting',menu=sizesetting)
        sizesetting.add_command(label='size to 15',command=self.set_font_size_15)
        sizesetting.add_command(label='size to 20',command=self.set_font_size_20)
        sizesetting.add_command(label='size to 30',command=self.set_font_size_30)

        stylesetting=tk.Menu(mainbar,tearoff=0)
        mainbar.add_cascade(label='Style Setting',menu=stylesetting)
        stylesetting.add_command(label='Arial',command=self.set_font_arial)
        stylesetting.add_command(label='Times',command=self.set_font_times)
        stylesetting.add_command(label='Courier',command=self.set_font_crourier)
            
        self.config(menu=mainbar)


    def theme_white(self):
        self.current_bg_color='white'
        self.current_fg_color='black'
        self.updateui()

    def theme_dark(self):
        self.current_bg_color='black'
        self.current_fg_color='white'
        self.updateui()


    def set_font_size_15(self):
        self.current_size = 15
        self.updateui()

    def set_font_size_20(self):
        self.current_size = 20
        self.updateui()

    def set_font_size_30(self):
        self.current_size = 30
        self.updateui()
    
    
    def set_font_arial(self):
        self.current_style = 'Arial'
        self.updateui()

    def set_font_times(self):
        self.current_style = 'Times New Roman'
        self.updateui()

    def set_font_crourier(self):
        self.current_style = 'Courier'
        self.updateui()

    def updateui(self):
        self.frame1.config(bg=self.current_bg_color)
        for widget in self.frame1.winfo_children():
            if isinstance(widget,tk.Label):
                widget.config(bg=self.current_bg_color,fg=self.current_fg_color,font=(self.current_style,self.current_size))
            elif isinstance(widget,tk.Entry):
                widget.config(font=(self.current_style,self.current_size))
            elif isinstance(widget,ttk.Combobox):
                widget.config(font=(self.current_style,self.current_size))

Form1=log_in()
Form1.mainloop()