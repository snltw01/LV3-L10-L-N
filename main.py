import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

class log_in(tk.Tk):
    def __init__(self):
        super().__init__()
       
        # image = Image.open('IMG/lll.png').resize((200,200))
        # self.tk_image = ImageTk.PhotoImage(image)
        self.geometry('500x500+100+200')
        self.title('Login')
        # self.ensure_files_exist()
        self.nation=['Việt Nam','Hàn Quốc','Nhật Bản','Mỹ',"Trung Quốc","Lào","Nga"]

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
        for widget in self.winfo_children():
            widget.destroy()

        # lb0=tk.Label(self.frame1,image=self.tk_image)
        # lb0.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        lb1=tk.Label(self.master,text='LOG IN',font=('Arial',20,"bold"))
        lb1.grid(row=1,column=0,columnspan=2,pady=15)

        lb2=tk.Label(self.master,text="Name",font=('Arial',13 ))
        lb2.grid(row=2,column=0,pady=10)

        self.en1=tk.Entry(self.master,font=('Arial',13))
        self.en1.grid(row=2,column=1,padx=14,pady=3)

        lb3=tk.Label(self.master,text='Password',font=('Arial',13))
        lb3.grid(row=3,column=0)

        self.en2=tk.Entry(self.master,show="*",font=("Arial",13))
        self.en2.grid(row=3,column=1,padx=14,pady=3)

        but1=tk.Button(self.master,text='Creat new accounts',font=('Arial',13),command=self.create_register_screen)
        but1.grid(row=4,column=0,pady=10)

        but2=tk.Button(self.master,text='Log in',font=('Arial',13),command=self.login_in)
        but2.grid(row=4,column=1,pady=10)

    def login_in(self):
        """Xử lý đăng nhập"""
        username = self.en1.get()
        password = self.en2.get()

        # Kiểm tra thông tin đăng nhập
        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Đọc file tài khoản
        with open(self.acc_file, 'r', encoding='utf-8') as f:
            accounts = [line.strip().split('|') for line in f]

        # Kiểm tra tài khoản
        for acc in accounts:
            if acc[0] == username and acc[1] == password:
                # Đăng nhập thành công
                messagebox.showinfo("Thành Công", "Đăng nhập thành công!")
                self.create_customer_screen()
                return
            
        # Đăng nhập thất bại
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác!")



    def create_register_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        


        lb1=tk.Label(self.master,text="ĐĂNG KÍ TÀI KHOẢN",fon=('Arial',30,'bold'))
        lb1.grid(row=0,column=1,padx=10,pady=10)

        lb2=tk.Label(self.master,text="Tên đăng kí")
        lb2.grid(row=1,column=0,columnspan=2)

        self.NAME=tk.Entry(self.master,font=('Arial',10))
        self.NAME.grid(row=2,column=0,columnspan=2)

        lb3=tk.Label(self.master,text='Mật khẩu')
        lb3.grid(row=3,column=0,columnspan=2)

        self.PASS=tk.Entry(self.master,font=('Arial',10))
        self.PASS.grid(row=4,column=0,columnspan=2)

        lb4=tk.Label(self.master,text='Xác nhận mật khẩu')
        lb4.grid(row=5,column=0,columnspan=2)

        self.PASSCOM=tk.Entry(self.master,font=('Arial',10))
        self.PASSCOM.grid(row=6,column=0,columnspan=2)

        but1=tk.Button(self.master,text='Quay lại',command=self.create_login_screen)
        but1.grid(row=7,column=1)

        but2=tk.Button(self.master,text="Đăng Ký", command=self.register)
        but2.grid(row=8,column=1)

    def register(self):
        """Xử lý đăng ký tài khoản"""
        username = self.NAME.get()
        password = self.PASS.get()
        confirm_password = self.PASSCOM.get()

        # Kiểm tra các điều kiện
        if not username or not password or not confirm_password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        if password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        # Kiểm tra tài khoản đã tồn tại chưa
        with open(self.acc_file, 'r', encoding='utf-8') as f:
            accounts = [line.strip().split('|')[0] for line in f]

        if username in accounts:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại!")
            return

        # Lưu tài khoản
        with open(self.acc_file, 'a', encoding='utf-8') as f:
            f.write(f"{username}|{password}\n")

        messagebox.showinfo("Thành Công", "Đăng ký tài khoản thành công!")
        self.create_login_screen()

    def create_customer_screen(self):
        # Xóa các widget cũ
        for widget in self.winfo_children():
            widget.destroy()



        # lb1=tk.Label(self.frame1, image=self.tk_image)
        # lb1.grid(row=0,column=1,columnspan=3,padx=80)
        lb2=tk.Label(self.master,text='THÔNG TIN KHÁCH HÀNG',font=('Arial',13,'bold'))
        lb2.grid(row=1,column=1,columnspan=3,pady=25)

        lb3=tk.Label(self.master,text="Họ và tên")
        lb3.grid(row=2,column=0)

        self.name=tk.Entry(self.master)
        self.name.grid(row=2,column=1,padx=30,pady=20)

        lb4=tk.Label(self.master,text='Địa chỉ')
        lb4.grid(row=2,column=2)

        self.address=tk.Entry(self.master)
        self.address.grid(row=2,column=3,padx=30,pady=20)

        lb5=tk.Label(self.master,text="Ngày sinh")
        lb5.grid(row=3,column=0)
        
        en3=tk.Entry(self.master)
        en3.grid(row=3,column=1,padx=30,pady=20)

        lb6=tk.Label(self.master,text="Email")
        lb6.grid(row=3,column=2)

        self.email=tk.Entry(self.master)
        self.email.grid(row=3,column=3,padx=30,pady=20) 

        lb7=tk.Label(self.master,text="Quốc tịch")
        lb7.grid(row=4,column=0)
        
        combobox=ttk.Combobox(self.master,values=self.nation, state='readonly')
        combobox.grid(row=4,column=1,padx=30,pady=20)

        lb8=tk.Label(self.master,text="Số Điện thoại")
        lb8.grid(row=4,column=2)

        self.phone=tk.Entry(self.master)
        self.phone.grid(row=4,column=3,padx=30,pady=20)

        but1=tk.Button(self.master,text='Register',command=self.login)
        but1.grid(row=5,column=1,columnspan=1)

        but2=tk.Button(self.master,text='Quit',command=quit)
        but2.grid(row=5,column=2,columnspan=1)


    def save_customer_info(self):
        """Lưu thông tin khách hàng ra file txt"""
        # Lấy thông tin từ các trường nhập
        name = self.name.get()
        phone = self.phone.get()
        email = self.email.get()
        address = self.address.get()

        # Kiểm tra thông tin
        if not all([name, phone, email, address]):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Lưu vào file
        with open(self.info_file, 'a', encoding='utf-8') as f:
            f.write(f"{name}|{phone}|{email}|{address}\n")

        messagebox.showinfo("Thành Công", "Lưu thông tin khách hàng thành công!")

        # Xóa các trường nhập
        self.name.delete(0, tk.END)
        self.phone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.address.delete(0, tk.END)







    # def __init__(self):
    #     super().__init__()
    #     # image = Image.open('IMG/lll.png').resize((200,200))
    #     # self.tk_image = ImageTk.PhotoImage(image)
    #     self.title('Form Đăng Kí')
    #     self.geometry('700x700+100+100')
    #     self.nation=['Việt Nam','Hàn Quốc','Nhật Bản','Mỹ',"Trung Quốc","Lào","Nga"]
    #     self.Creat_widget()

    #     self.current_bg_color='white'
    #     self.current_size=9
    #     self.current_style='Arial'
    #     self.current_fg_color='black'





    # def quit(self):
    #     self.destroy()

    # def login(self):
    #     messagebox.showinfo('Thông Báo','Đã đăng nhập')

    

    
    #     mainbar=tk.Menu(self)
    #     theme=tk.Menu(mainbar,tearoff=0)
    #     mainbar.add_cascade(label='theme',menu=theme)
    #     theme.add_command(label='Light',command=self.theme_white)
    #     theme.add_command(label='Dark',command=self.theme_dark)

    #     sizesetting=tk.Menu(mainbar,tearoff=0)
    #     mainbar.add_cascade(label='Size Setting',menu=sizesetting)
    #     sizesetting.add_command(label='size to 15',command=self.set_font_size_15)
    #     sizesetting.add_command(label='size to 17',command=self.set_font_size_17)
    #     sizesetting.add_command(label='size to 20',command=self.set_font_size_20)

    #     stylesetting=tk.Menu(mainbar,tearoff=0)
    #     mainbar.add_cascade(label='Style Setting',menu=stylesetting)
    #     stylesetting.add_command(label='Arial',command=self.set_font_arial)
    #     stylesetting.add_command(label='Times',command=self.set_font_times)
    #     stylesetting.add_command(label='Courier',command=self.set_font_crourier)
            
    #     self.config(menu=mainbar)


    # def theme_white(self):
    #     self.current_bg_color='white'
    #     self.current_fg_color='black'
    #     self.updateui()

    # def theme_dark(self):
    #     self.current_bg_color='black'
    #     self.current_fg_color='white'
    #     self.updateui()


    # def set_font_size_15(self):
    #     self.current_size = 15
    #     self.updateui()

    # def set_font_size_20(self):
    #     self.current_size = 20
    #     self.updateui()

    # def set_font_size_17(self):
    #     self.current_size = 17
    #     self.updateui()
    
    
    # def set_font_arial(self):
    #     self.current_style = 'Arial'
    #     self.updateui()

    # def set_font_times(self):
    #     self.current_style = 'Times New Roman'
    #     self.updateui()

    # def set_font_crourier(self):
    #     self.current_style = 'Courier'
    #     self.updateui()

    # def updateui(self):
    #     self.frame1.config(bg=self.current_bg_color)
    #     for widget in self.frame1.winfo_children():
    #         if isinstance(widget,tk.Label):
    #             widget.config(bg=self.current_bg_color,fg=self.current_fg_color,font=(self.current_style,self.current_size))
    #         elif isinstance(widget,tk.Entry):
    #             widget.config(font=(self.current_style,self.current_size))
    #         elif isinstance(widget,ttk.Combobox):
    #             widget.config(font=(self.current_style,self.current_size))

def main():
    # root = tk.Tk()
    app = log_in()
    app.mainloop()

if __name__ == "__main__":
    main()