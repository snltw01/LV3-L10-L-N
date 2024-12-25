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