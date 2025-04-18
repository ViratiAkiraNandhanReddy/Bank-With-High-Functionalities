'''This Module Is Used To Activate The SoftWare/Product By Using The Product Keys
Which Provides The Additional Security For This Software

The Product Keys Will Be Provided By The Owner
GitHub: ViratiAkiraNandhanReddy'''

#Importing Required Packages/Modules
import tkinter as tk

#If The Product Is Not Activated
Activated = False

#Special Keys For Activation of Software
Product_keys = [

    '2030-GITH-UBGC-AKKI-DIST-FIRS-TPRJ-INDI-AUSA-2026',
    '2030-AKKI-FIRS-TPRJ-HAPP-YGIT-DIST-USAI-NDIA-2026',
    '2030-DEV0-FIRS-TPRJ-INDI-AUSA-AKKI-AT18-0022-2026',
    '2030-GITH-UBAT-AKKI-USAI-NDIA-FIRS-TPRJ-2008-2026',
    '2030-AKKI-ATUS-AGOO-GLEA-ISSE-100M-USAI-NDIA-2026',
    '2030-USAI-NDIA-GOOG-LEAI-WITH-AKKI-WITH-$10T-2026',
    '2030-ALLR-IGHT-SREC-IVED-WITH-AKKI-INDI-AUSA-2026',
    '2030-USAI-NDIA-2008-VSCO-DEPY-THON-AIAT-AKKI-2026',
    'USAI-NDIA-VIRA-TIAK-IRAN-ANDH-ANRE-DDY1-2008-2030',
    'LAST-PROD-UCTK-EYAT-AKKI-PROG-RAM1-USAI-NDIA-2030'

]

#Terms And Conditions For The User
Terms_Conditions = '''Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software with restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software but One Thing Should Be Remembered The Original
License File Should Not Be Modified

**Owner's Note And Guidelines**

SHOULD NOT MODIFY THE LICENSE FILE, MODIFYING THE OWNERSHIP DETAILS ARE STRICTLY FORBIDDEN!
DON'T TRY TO DELETE THE FILE [Data_Of_User.txt], ALL THE REQUIRED DETAILS ARE SAVED IN IT

Modifying Restricted Zone in License File is STRICTLY FORBIDDEN!

Contact Me:
Gmail: viratiaki29@gmail.com
GitHub: ViratiAkiraNandhanReddy
Instagram: Viratiaki53

*Owner Is Not Responsible For Any Kind Of Issue Regarding This Software

'''

#Activation Of SoftWare If The Product Key Match 
class Software_Activation:

    '''This Class Is Used For The Activation Of the SoftWare/Product\n
How Does This Class Works?\n
It will Ask The User To Accept The Terms And Guidelines If Accepted. Then Asks For The Product Key If That Product Key Matches The Exact Same As The 
Given Product Keys Then It Will Return As True. This Will Be Readed By The Main_Bank.py. Then It Will Call The Save_Info.py. After That The Main
Program Will Be Automatically Started On It Self\n
Then The Program Is Ready To Use\n
**Once The Program Is Activated It Never Asks To Activate Again
 '''
    
    #Main Function
    def Activate(self) -> bool:

        #New Window For Product Key
        def Product_Key():

            #Getting The Key
            def Key():
                if Entery_Key.get() in Product_keys:
                    Window_Activate.destroy()
                    global Activated
                    Activated = True

                else:
                    Invalid = tk.Label(Window_Activate,text='Invalid Product Key',fg='Yellow',bg='#4F55A8').place(x=200,y=200)
            
            #Removeing Text in Example
            def Temp(Key=None):
                Entery_Key.delete(0,'end')
                Entery_Key.config(fg='White')
            
            #Initial Setup Of Window
            Window.destroy()
            Window_Activate = tk.Tk()
            Window_Activate.title('Product Key')
            Window_Activate.geometry('640x320')
            Window_Activate.resizable(False,False)
            Window_Activate.configure(background='#4F55A8')
            
            #Instructions For The User
            tk.Label(Window_Activate,text='Enter a Product Key',bg='#4F55A8',fg='White',font=('Calibri 22'),justify='left',height=2).place(x=10,y=0)
            tk.Label(Window_Activate,text='The Product Keys For This Software Will Be Provided By The Owner, Also Provided In The \nWebsite That You Downloaded From (GitHub)',bg='#4F55A8',font=('Calibri 13')).place(x=10,y=80)
            tk.Label(Window_Activate,text='Product Key',bg='#4F55A8',font=('Calibri 14'),fg='White').place(x=10,y=140)
            
            #Product Key Entry
            Entery_Key = tk.Entry(Window_Activate,font=('Consolas',12),border=2,bg='#2F3263',relief='ridge',highlightbackground='White')
            Entery_Key.insert(0,string='XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX')
            Entery_Key.config(fg='#82829C')
            Entery_Key.place(x=10,y=168,relwidth=0.75,relheight=0.09)
            Entery_Key.bind('<FocusIn>',Temp)
            
            #Spepping Up
            tk.Button(Window_Activate,text='Authenticate',fg='White',command=Key,bg='#1E2040',activebackground='grey').place(x=485,y=250)
            tk.Button(Window_Activate,text='Cancel',fg='White',command=Window_Activate.destroy,bg='#1E2040',activebackground='grey').place(x=580,y=250)
            
            #Copyright Note 
            tk.Label(Window_Activate,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',fg='White',bg='#4F55A8',font=('Calibri 8')).place(x=418,y=300)
            Window_Activate.mainloop()
        
        #Making Forcefull Acceptance
        def Accepted():
            if OK.get() == True:
                Next.config(state='normal')
            elif OK.get() == False:
                Next.config(state='disabled')

        #Initial Setup Of Window
        Window = tk.Tk()
        Window.title('Activation Window')
        Window.geometry('750x500')
        Window.config(background='Light Blue')
        Window.resizable(False,False)
        # icon = tk.PhotoImage(file=r'Bank_Package\Visual Data\10108414.png')
        # Window.iconphoto(True,icon)

    
        

        
        OK = tk.BooleanVar()

        #Terms And Conditions
        Terms = tk.Frame(Window,background='White',height=380,width=700)
        Terms.place(x=25,y=25)
        tk.Label(Terms,text='Software Licence Agreement And Guidelines',fg='Black',bg='White',font=('Roboto 18 bold')).place(x=90,y=8)
        tk.Label(Terms,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',bg='White',font=('Roboto 12 bold')).place(x=165,y=43)
        tk.Label(Terms,text=Terms_Conditions,bg='White').place(x=22,y=70)
        
        #Acceptance Check
        Check = tk.Checkbutton(Window,text='Accept All Terms And Conditions',underline=0,variable=OK,onvalue=True,\
                            offvalue=False,command=Accepted,bg='Light Blue',activebackground='Light Blue').place(x=25,y=410)
        Next = tk.Button(Window,text='Next',state='disabled',command=Product_Key,font=('Roboto 10'),activebackground='#316E7A',bg='#68ABC9',relief='ridge')
        tk.Button(Window,text='Cancel',fg='Red',command=Window.destroy,font=('Roboto 10'),activebackground='#316E7A',bg='#68ABC9',relief='ridge').place(x=662,y=435)
        Next.place(x=580,y=435,width=60)

        #Copyright Note 
        tk.Label(Window,text='Copyright (c) 2026 Virati Akira Nandhan Reddy',\
                fg='Black',bg='Light Blue',font=('Calibri 8')).place(x=528,y=480)
        
        Window.mainloop()

        return Activated

#Satisfied Code Completion:98%     
'''                                                            End Of Program                                                                 '''