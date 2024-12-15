from tkinter import messagebox
def Blank_Error():
    messagebox.showerror(title='Blank Error',message='Input Can\'t Be Blank!')
def Exist_Error():
     messagebox.showinfo(title='Exist Error',message='User Already Exists')
def Digit_Error():
    messagebox.showerror(title='Digit Error',message='UserName Can\'t Be Only Numbers')
def Pass_Error():
    messagebox.showerror(title='Wrong Password',text='Wrong PassWord Entered')