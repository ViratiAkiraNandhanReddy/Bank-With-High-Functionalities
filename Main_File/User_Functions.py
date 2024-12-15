def loop():
    import tkinter as tk
    from Login_Screen import Login
    Command = True
    while Command:
        def log():
            Window.destroy()
            Login()
            global Command
            Command = False

        Window = tk.Tk()
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
        