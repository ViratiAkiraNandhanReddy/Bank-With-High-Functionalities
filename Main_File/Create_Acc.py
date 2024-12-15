def New_Account():
    from __init__ import Accounts,PinCodes
    import tkinter as tk
    import Login_Screen
    import Invalid_Error
    
    def Stop():
            Window.destroy()
            Login_Screen.Login()
            global Command
            Command = False

    Command = True
    while Command:
        def Values():
            global Acc
            Acc=New.get()
        
        Window = tk.Tk()
        Window.title('New Account')
        Window.geometry('350x120')
        tk.Label(Window,text='Creating An New Account',fg='Red').grid(column=2)
        tk.Label(Window,text='New UserName').grid(row=2,pady=20)
        New = tk.Entry(Window)
        New.grid(row=2,column=2,ipadx=30)
        Continue = tk.Button(text='Continue',fg='Green',command=Values).grid(row=3,column=2)
        Cancel = tk.Button(text='Cancel',fg='Red',command=Stop).grid(row=3,column=3)

        Window.mainloop()

        try:
            if Acc == '':
                Invalid_Error.Blank_Error()
            elif Acc in Accounts:
                Invalid_Error.Exist_Error()
            elif Acc.isdigit()==True:
                Invalid_Error.Digit_Error()
            else:
                Accounts.append(Acc)

        except:
            pass
