import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class register:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.master.geometry("300x400")

        # Tạo thư mục lưu trữ nếu chưa tồn tại
        self.acc_file = "acc.txt"
        self.info_file = "info.txt"
        
        # Kiểm tra và tạo file nếu chưa tồn tại
        self.ensure_files_exist()

        # Tạo giao diện đăng nhập
        self.create_login_screen()

    def ensure_files_exist(self):
        """Tạo các file nếu chưa tồn tại"""
        for file in [self.acc_file, self.info_file]:
            if not os.path.exists(file):
                with open(file, 'w', encoding='utf-8') as f:
                    pass

    def create_login_screen(self):
        """Tạo giao diện đăng nhập"""
        # Xóa các widget cũ
        for widget in self.master.winfo_children():
            widget.destroy()

        # Tiêu đề
        lb1=tk.Label(self.master, text="ĐĂNG NHẬP", font=("Arial", 30, "bold"))
        lb1.pack(pady=20)

        # Tên đăng nhập
        lb2=tk.Label(self.master, text="Name:")
        lb2.pack()
        
        
        self.username_entry = tk.Entry(self.master, width=30)
        self.username_entry.pack(pady=5)

        # Mật khẩu
        lb3=tk.Label(self.master, text="Password:")
        lb3.pack()
        
        
        self.password_entry = tk.Entry(self.master, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Nút đăng nhập
        but1=tk.Button(self.master, text="Đăng Nhập", command=self.login)
        but1.pack(pady=10)

        # Nút đăng ký
        but2=tk.Button(self.master, text="Đăng Ký Tài Khoản Mới", command=self.create_register_screen)
        but2.pack(pady=5)

    def login(self):
        """Xử lý đăng nhập"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Kiểm tra thông tin đăng nhập
        if not username or not password:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Đọc file tài khoản
        with open(self.acc_file, 'r', encoding='utf-8') as f:
            acc = [line.strip().split('|') for line in f]

        # Kiểm tra tài khoản
        for accounts in acc:
            if accounts[0] == username and accounts[1] == password:
                # Đăng nhập thành công
                messagebox.showinfo("Thành Công", "Đăng nhập thành công!")
                self.create_customer_screen()
                return

        # Đăng nhập thất bại
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không chính xác!")

    def create_register_screen(self):
        """Tạo giao diện đăng ký"""
        # Xóa các widget cũ
        for widget in self.master.winfo_children():
            widget.destroy()

        # Tiêu đề
        lb1=tk.Label(self.master, text="ĐĂNG KÝ TÀI KHOẢN MỚI", font=("Arial", 30, "bold"))
        lb1.pack(pady=20)

        # Tên đăng nhập
        lb2=tk.Label(self.master, text="Tên đăng kí:")
        lb2.pack()
        
        
        self.reg_username_entry = tk.Entry(self.master, width=30)
        self.reg_username_entry.pack(pady=5)

        # Mật khẩu
        lb3=tk.Label(self.master, text="Mật khẩu:")
        lb3.pack()
        self.reg_password_entry = tk.Entry(self.master, show="*", width=30)
        self.reg_password_entry.pack(pady=5)

        # Xác nhận mật khẩu
        lb4=tk.Label(self.master, text="Nhập Lại Mật Khẩu:")
        lb4.pack()
        self.reg_confirm_password_entry = tk.Entry(self.master, show="*but2", width=30)
        self.reg_confirm_password_entry.pack(pady=5)

        # Nút đăng ký
        but1=tk.Button(self.master, text="Đăng Ký", command=self.register)
        but1.pack(pady=10)

        # Nút quay lại
        but2=tk.Button(self.master, text="Quay Lại", command=self.create_login_screen)
        but2.pack(pady=5)

    def register(self):
        """Xử lý đăng ký tài khoản"""
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.reg_confirm_password_entry.get()

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
        """Tạo giao diện quản lý thông tin khách hàng"""
        # Xóa các widget cũ
        for widget in self.master.winfo_children():
            widget.destroy()

        # Tiêu đề
        lb1=tk.Label(self.master, text="CUSTOMER'S INFORMATION", font=("Arial", 30, "bold"))
        lb1.pack(pady=20)

        # Họ tên
        lb2=tk.Label(self.master, text="Họ và Tên")
        lb2.pack()
        self.name_entry = tk.Entry(self.master, width=30)
        self.name_entry.pack(pady=5)

        # Số điện thoại
        lb3=tk.Label(self.master, text="Số Điện Thoại:")
        lb3.pack()
        self.phone_entry = tk.Entry(self.master, width=30)
        self.phone_entry.pack(pady=5)

        # Email
        lb4=tk.Label(self.master, text="Email:")
        lb4.pack()
        self.email_entry = tk.Entry(self.master, width=30)
        self.email_entry.pack(pady=5)

        # Địa chỉ
        lb5=tk.Label(self.master, text="Địa Chỉ:")
        lb5.pack()
        self.address_entry = tk.Entry(self.master, width=30)
        self.address_entry.pack(pady=5)

        # Nút lưu thông tin
        but1=tk.Button(self.master, text="Duyệt và lưu thông tin", command=self.save_customer_info)
        but1.pack(pady=10)

        # Nút xem danh sách khách hàng
        but2=tk.Button(self.master, text="Xem Danh Sách Khách Hàng", command=self.view_customers)
        but2.pack(pady=5)

        # Nút đăng xuất
        but3=tk.Button(self.master, text="Đăng Xuất", command=self.create_login_screen)
        but3.pack(pady=5)

    def save_customer_info(self):
        """Lưu thông tin khách hàng ra file txt"""
        # Lấy thông tin từ các trường nhập
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        # Kiểm tra thông tin
        if not all([name, phone, email, address]):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        # Lưu vào file
        with open(self.info_file, 'a', encoding='utf-8') as f:
            f.write(f"{name}|{phone}|{email}|{address}\n")

        messagebox.showinfo("Thành Công", "Lưu thông tin khách hàng thành công!")

        # Xóa các trường nhập
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_customers(self):
        """Hiển thị danh sách khách hàng"""
        # Đọc file khách hàng
        with open(self.info_file, 'r', encoding='utf-8') as f:
            customers = f.readlines()

        # Tạo cửa sổ mới để hiển thị
        view_window = tk.Toplevel(self.master)
        view_window.title("Danh Sách Khách Hàng")
        view_window.geometry("500x400")

        # Tạo text widget để hiển thị
        text_widget = tk.Text(view_window, wrap=tk.WORD)
        text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Hiển thị danh sách
        for customer in customers:
            text_widget.insert(tk.END, customer)

        # Thêm nút đóng
        but1=tk.Button(view_window, text="Đóng", command=view_window.destroy)
        but1.pack(pady=10)

def main():
    root = tk.Tk()
    app = register(root)
    root.mainloop()

if __name__ == "__main__":
    main()