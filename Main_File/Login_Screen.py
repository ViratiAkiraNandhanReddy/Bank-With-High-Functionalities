def Login():
    from __init__ import Accounts
    import tkinter as tk
    import PassCodes
    import Create_Acc

    #Variable To Stop The Loop 
    Command = True

    #Running In a loop
    while Command:

        #Getting All The Values
        def Values():
            global UserName,PinCode
            UserName = User.get()
            PinCode = Pin.get()
            Window.destroy()
        
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
                PassCodes.Code(PinCode)
                Command = False
            else:
                try:

                    #If Yes Goes to The Module
                    def Yes():
                        if Yes_Bt.configure():
                            Verify.destroy()
                            Create_Acc.New_Account()
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
