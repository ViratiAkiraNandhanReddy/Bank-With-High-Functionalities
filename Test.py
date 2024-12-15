import tkinter as tk
from Main_File import Invalid_Error
from Main_File.__init__ import Accounts,PinCodes,User_func


def New_Account():

    def Stop():
            Window.destroy()
            Login()
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


def User_Functions():

    Command = True
    while Command:
        def log():
            Window.destroy()
            Login()
            global Command
            Command = False

        Window = tk.Tk(sync=True)
        Window.geometry('300x500')
        B = tk.Button(Window,text='Balance',fg='Green')
        B.place(x=130,y=10)
        D = tk.Button(Window,text='Deposit',fg='Blue')
        D.place(x=90,y=50)
        W = tk.Button(Window,text='Withdrawal',fg='Red')
        W.place(x=150,y=50)
        C = tk.Button(Window,text='Log Out',command=log,fg='Purple')
        C.place(x=130,y=400)
        Window.mainloop()








def Login():
    
    #Variable To Stop The Loop 
    Command = True

    #Running In a loop
    while Command:

        #Getting All The Values
        def Values():
            global UserName,PinCode
            UserName = User.get()
            PinCode = Pin.get()
            User_Functions()
        
        #Creating The Main Login screen
        Window = tk.Tk()
        Window.geometry('250x150')
        Window.title('Login')
        tk.Label(Window,text='UserName').grid(row=2,column=2)
        tk.Label(Window,text='PinCode').grid(row=4,column=2)
        User = tk.Entry(Window)
        Pin = tk.Entry(Window)
        Pin.grid(row=4,column=3,pady=20)
        User.grid(row=2,column=3,padx=20)
        Continue = tk.Button(Window,text='Continue',command=Values,fg='Green').grid(row=6,column=3)

        Window.mainloop()

        #Using The Info Of Users
        try:
            if UserName in Accounts:
                if PinCodes[User_func(UserName)] == PinCode:
                    User_Functions()
                else:
                    Invalid_Error.Pass_Error()
                Command = False
            else:
                try:

                    #If Yes Goes to The Module
                    def Yes():
                        if Yes_Bt.configure():
                            Verify.destroy()
                            New_Account()
                            global Command
                            Command = False

                    #If No Loop Runs Again
                    def No():
                        Verify.destroy()
                        
                    Verify = tk.Tk()
                    Verify.title('Account Not Available')
                    Verify.geometry('300x180')
                    tk.Label(Verify,text='Oops! Account Not Available In The DataBase',fg='Red').pack()
                    tk.Label(Verify,text='Do You Want To Create An Account',fg='Blue').pack(pady=20)
                    Yes_Bt = tk.Button(Verify,text='Create An Account',fg='Green',command=Yes)
                    Yes_Bt.pack()
                    No_Bt = tk.Button(Verify,text='No Thanks!',fg='Red',command=No)
                    No_Bt.pack(pady=20)
            
                    Verify.mainloop()
                except:
                    pass
        except:
            Window.mainloop()

Login()