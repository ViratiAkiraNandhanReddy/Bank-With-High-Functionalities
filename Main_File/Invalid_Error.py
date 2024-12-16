from tkinter import messagebox

def Blank_Error():
    messagebox.showerror(title='Blank Error',message='Input Can\'t Be Blank!')

def Exist_Error():
     messagebox.showinfo(title='Exist Error',message='User Already Exists')

def Digit_Error():
    messagebox.showerror(title='Digit Error',message='Username Can\'t Be Only Numbers')

def Pass_Error():
    messagebox.showerror(title='Wrong Password',message='Wrong PassWord Entered')

def User_blank_Error():
    messagebox.showerror(title='Blank Error',message='Username Can\'t Be Blank!')

def Pin_blank_Error():
    messagebox.showerror(title='Blank Error',message='PinCode Can\'t Be Blank!')

def Pin_Char_Error():
    messagebox.showerror(title='Against PinCode Rule',message='Must Contain 4 or More Characters')

def xyz():
    pass