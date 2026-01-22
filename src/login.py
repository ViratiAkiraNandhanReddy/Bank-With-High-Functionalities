from . import *
from PIL import Image
from random import randint
from .signup import signup_interface
from .dashboard import dashboard

icon__account_circle = Image.open(fr'{DIR_PATH}\assets\icons\material icons\account_circle.png')
icon__password = Image.open(fr'{DIR_PATH}\assets\icons\material icons\password.png')
icon__security = Image.open(fr'{DIR_PATH}\assets\icons\material icons\security.png')

class login_interface:

    '''
    Docstring for login_interface
    '''

    def __init__(self) -> None:
        pass

    class login:

        '''
        Docstring for login
        '''
      
        def __init__(self) -> None: # Initialize The Login Interface

            # --- Background Image Configuration --- #

            self.background__login = Image.open(fr'{DIR_PATH}\assets\images\login_backgrounds\{randint(0, 30)}.jpg')

            # --- X-Axis Configuration For Animation --- #

            self.x_axis_rtl = +960 # login screen frame starts from right to left (initially outside the window) -- rtl
            self.x_axis_ltr = -410 # reset password screen frame starts from left to right (initially outside the window) -- ltr

            # --- Main Window Configuration --- #

            self.window = customtkinter.CTk()
            self.window.title('Login')
            self.window.geometry('950x600+100+40')
            self.window.resizable(False, False)
            self.window.protocol('WM_DELETE_WINDOW', )
            customtkinter.CTkLabel(self.window, text = '', image = customtkinter.CTkImage(light_image = self.background__login, dark_image = self.background__login, size = (950,600))).place(x = 0, y = 0)
            self.window.after(600, self.show_login_rtl)

            # --- Login Screen Configuration --- # 

            self.frame__login = customtkinter.CTkFrame(self.window,corner_radius=0)
            self.frame__login.configure(width = 400, height = 560)
            self.frame__login.place(x = self.x_axis_rtl, y = 20)
            self.__heading_login = customtkinter.CTkLabel(self.frame__login, text = 'Login', font = ('Freestyle Script', 42, 'bold'), width = 5)#.place(x=175,y=2)
            self.__greet_login = customtkinter.CTkLabel(self.frame__login, text='Welcome Back!',font=('Roboto',30,'bold'),text_color='#57D956')#.place(x=30,y=65)
            self.__subheading_login = customtkinter.CTkLabel(self.frame__login, text='Sign in to Your Account', height = 0,font=('Roboto',12))#.place(x=33,y=100)
            
            # --- Username Entry --- #

            self.__user_icon_label_login = customtkinter.CTkLabel(self.frame__login,text='Username',font=('Roboto',24,'bold'),image=customtkinter.CTkImage(light_image = icon__account_circle, dark_image = icon__account_circle, size = (40, 40)),compound='top')#.place(x=140,y=140)
            self.__username = customtkinter.CTkEntry(self.frame__login,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=340,corner_radius=5,
                                    font=('Roboto',16))#;Username.place(x=30,y=204)
            
            # --- Password Entry And Reset Password --- #

            self.__password_icon_label_login = customtkinter.CTkLabel(self.frame__login,text='Password',font=('Roboto',24,'bold'),image=customtkinter.CTkImage(light_image = icon__password, dark_image = icon__password, size = (40, 40)), compound = 'top')#.place(x=140,y=260)
            self.__forgot_password_button_login = customtkinter.CTkButton(self.frame__login,text='Forgot Password',height=0,width=0,fg_color='transparent',hover=False,font=('Roboto',10),text_color='#218CFF', command = self.hide_login_frame__show_reset_password_frame)#.place(x=288,y=359)
            self.__password = customtkinter.CTkEntry(self.frame__login,placeholder_text='Example: Viratiaki@Akki#2008',height=40,width=340,corner_radius=5,
                                    font=('Roboto',16))#;Password.place(x=30,y=324)

            # --- Login And Sign Up Buttons --- #

            self.__login_button_login = customtkinter.CTkButton(self.frame__login,text='Login', width = 120, border_width = 1, text_color = 'Green', fg_color = 'transparent', font = ('Roboto', 16, 'bold'),
                        command = self.validate_and_redirect_to_dashboard)#.place(x=142,y=400)
            self.__sign_up_message_login = customtkinter.CTkLabel(self.frame__login,text='Don\'t You Have An Account? ',font=('Roboto',10,'italic'),width=0,height=0)#.place()
            self.__sign_up_button_login = customtkinter.CTkButton(self.frame__login,text='Sign Up',width=0,height=0,text_color='#00A2E8',fg_color='transparent', font=('Roboto',10,'italic'), hover = False,
                                        command = self.redirect_to_signup)#.place(x=2,y=538)
            

            # --- Reset Password Screen Configuration --- #

            self.frame__reset_password = customtkinter.CTkFrame(self.window, corner_radius = 0)
            self.frame__reset_password.configure(width = 400, height = 560)
            self.frame__reset_password.place(x = self.x_axis_ltr, y = 20)
            self.__heading_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text='Forgot Password',font=('Freestyle Script',42,'bold'),width=5)#.place(x=105,y=2)
            self.__greet_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text='Get Your Account Back!',font=('Roboto',20,'bold'),text_color='#57D956')#.place(x=30,y=65)
            self.__subheading_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text='Enter Required Credentials',font=('Roboto',12),height=0)#.place(x=33,y=90)
            
            # --- Username Entry At Reset Password Screen --- #

            self.__user_icon_label_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text='Username',font=('Roboto',24,'bold'),image=customtkinter.CTkImage(light_image=icon__account_circle,dark_image=icon__account_circle,size=(40,40)),compound='top')#.place(x=140,y=140)
            self.__username_at_reset_password = customtkinter.CTkEntry(self.frame__reset_password,placeholder_text='Example: Virati Akira Nandhan Reddy',height=40,width=340,corner_radius=5,
                                    font=('Roboto',16))#.place(x=30,y=204)
            
            # --- Security Code Entry At Reset Password Screen --- #

            self.__security_icon_label_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text='Security Code',font=('Roboto',24,'bold'),image=customtkinter.CTkImage(light_image = icon__security, dark_image = icon__security,size=(40,40)),compound='top',height=0)#.place(x=120,y=250)
            self.__forgot_security_code_button_reset_password = customtkinter.CTkButton(self.frame__reset_password,text = 'Forgot Security Code', height = 0, width = 0, fg_color = 'transparent', hover = False, font = ('Roboto', 10), text_color = '#218CFF', command = self.forgot_security_code)#.place(x=270,y=359)
            self.__security_code_at_reset_password = customtkinter.CTkEntry(self.frame__reset_password, placeholder_text = 'Example: Viratiaki@Akki', height = 40, width = 340, corner_radius = 5, font = ('Roboto', 16))#.place(x=30,y=324)
            
            # --- Request And Cancel Buttons At Reset Password Screen --- #

            self.__request_reset_password = customtkinter.CTkButton(self.frame__reset_password, text = 'Request', width = 120, border_width = 1, text_color = '#3264FF',
                                                fg_color = 'transparent', font = ('Roboto', 16, 'bold'), hover_color = 'Light Blue', command = self.request_for_password_reset)#.place(x=142,y=400)
            self.__cancel_reset_password = customtkinter.CTkButton(self.frame__reset_password, text = 'Cancel', fg_color = 'transparent', height = 15, border_width = 1, hover_color = '#A1FB8E', width = 45, command = self.hide_reset_password_frame__show_login_frame)#.place(x=2,y=538)
            

            self.window.after(1500, self.show_contents_login)

            # --- Copyright Notices --- #

            self.__copyright_notice_login = customtkinter.CTkButton(self.frame__login, text = 'Copyright (c) 2026 Bank-With-High-Functionalities', font = ('Calibri', 8), command = License_Developer_Documentation, hover = False, width = 0,
                        height = 0,fg_color = 'transparent', text_color = '#218CFF')#.place(x=243,y=547)
            self.__copyright_notice_reset_password = customtkinter.CTkLabel(self.frame__reset_password,text = 'Copyright (c) 2026 Bank-With-High-Functionalities', font = ('Calibri', 8))#.place(x=247,y=540)
            
            self.window.mainloop()
        
        def show_login_rtl(self): # show login frame -- MOVE: right to left
            '''
            ## Shows the login frame moving from right to left
            '''
            
            self.x_axis_rtl -= 10

            if self.x_axis_rtl >= 530:
                
                self.frame__login.place(x = self.x_axis_rtl, y = 20)
                self.window.after(10,self.show_login_rtl)
            
            if self.x_axis_rtl < 530:
                
                return
            
        def hide_login_rtl(self): # hide login frame -- MOVE: left to right
            '''
            ## Hides the login frame moving from left to right
            '''

            self.x_axis_rtl += 10

            if self.x_axis_rtl <= 960:
            
                self.frame__login.place(x = self.x_axis_rtl, y = 20)
                self.window.after(10, self.hide_login_rtl)
            
            if self.x_axis_rtl > 960:
            
                return
        
        def show_reset_password_ltr(self): # show reset password frame -- MOVE: left to right
            '''
            ## Shows the reset password frame moving from left to right
            '''

            self.x_axis_ltr += 10
            
            if self.x_axis_ltr <= 20:
            
                self.frame__reset_password.place(x = self.x_axis_ltr, y = 20)
                self.window.after(10, self.show_reset_password_ltr)
            
            if self.x_axis_ltr >= 20:
            
                return 
        
        def hide_reset_password_ltr(self): # hide reset password frame -- MOVE: right to left
            '''
            ## Hides the reset password frame moving from right to left
            '''

            self.x_axis_ltr -= 10
            
            if self.x_axis_ltr >= -410:
            
                self.frame__reset_password.place(x = self.x_axis_ltr, y = 20)
                self.window.after(10, self.hide_reset_password_ltr)
            
            if self.x_axis_ltr < -410:
            
                return
            
        def hide_reset_password_frame__show_login_frame(self): # Hides The Reset Password Screen Then Shows The Login Screen in The Window

            self.hide_contents_reset_password()
            self.hide_reset_password_ltr()
            self.show_login_rtl()

        def hide_login_frame__show_reset_password_frame(self): # Hides The Login Screen Then Shows The Reset Password Screen in The Window

            self.hide_contents_login()
            self.hide_login_rtl()
            self.show_reset_password_ltr()

        def show_contents_login(self): # Shows The Contents Of The Login Screen

            self.__heading_login.place(x=175,y=2)
            self.__greet_login.place(x=30,y=65)
            self.__subheading_login.place(x=33,y=100)
            self.__user_icon_label_login.place(x=140,y=140)
            self.__username.place(x=30,y=204)
            self.__password_icon_label_login.place(x=140,y=260)
            self.__forgot_password_button_login.place(x=288,y=359)
            self.__password.place(x=30,y=324)
            self.__login_button_login.place(x=142,y=400)
            self.__sign_up_message_login.place(x=117,y=480)
            self.__sign_up_button_login.place(x=247,y=477)
            self.__copyright_notice_login.place(x=243,y=547)

        def hide_contents_login(self): # Hides The Contents Of The Login Screen

            for widget in [

                self.__password,
                self.__username,
                self.__greet_login,
                self.__heading_login,
                self.__subheading_login,
                self.__login_button_login,
                self.__sign_up_button_login,
                self.__sign_up_message_login,
                self.__user_icon_label_login,
                self.__copyright_notice_login,
                self.__password_icon_label_login,
                self.__forgot_password_button_login
                
                ]:

                widget.place_forget()

            else:
                
                self.window.after(900, self.show_contents_reset_password)

        def show_contents_reset_password(self): # Shows The Contents Of The Reset Password Screen

            self.__heading_reset_password.place(x=105,y=2)
            self.__greet_reset_password.place(x=30,y=65)
            self.__subheading_reset_password.place(x=33,y=90)
            self.__user_icon_label_reset_password.place(x=140,y=140)
            self.__username_at_reset_password.place(x=30,y=204)
            self.__security_icon_label_reset_password.place(x=120,y=250)
            self.__forgot_security_code_button_reset_password.place(x=270,y=359)
            self.__security_code_at_reset_password.place(x=30,y=324)
            self.__request_reset_password.place(x=142,y=400)
            self.__cancel_reset_password.place(x=2,y=538)
            self.__copyright_notice_reset_password.place(x=247,y=541)

        def hide_contents_reset_password(self): # Hides The Contents Of The Reset Password Screen

            for widget in [
                
                self.__greet_reset_password,
                self.__cancel_reset_password,
                self.__heading_reset_password,
                self.__request_reset_password,
                self.__subheading_reset_password, 
                self.__username_at_reset_password,
                self.__user_icon_label_reset_password,
                self.__security_code_at_reset_password,
                self.__copyright_notice_reset_password,
                self.__security_icon_label_reset_password,
                self.__forgot_security_code_button_reset_password
                
                ]:
                
                widget.place_forget()

            else:
                
                self.window.after(900, self.show_contents_login)

        def redirect_to_signup(self): # Redirects To The Signup Module

            self.window.destroy() # Closing The Login Window

            try:

                signup_interface.signup() # Opening The Signup Window

                login_interface.login() # Re-Opening The Login Window After Signing Up

            except:

                login_interface.login() # Re-Opening The Login Window If Any Error Occurs

        def validate_and_redirect_to_dashboard(self): # Validates The User Credentials And Redirects To The Dashboard

            username = self.__username.get()
            password = self.__password.get()

            def redirect_to_dashboard(): # Redirects To The Dashboard

                try:

                    #Destroy The Login Window And Opens Up The User Actions Module And Then Goes To The Login Window (if They Logout)
                    try:

                        if self.UserData.get('FileNotFoundError') or self.UserData.get('JSONDecodeError'):
                            pass

                        else:
                            self.window.destroy()
                            dashboard(username)
                            login_interface.login()

                    except KeyError:
                        print('Hello From KeyError')
                except:
                    pass

            #If the Username Is Not Entered But Password Is Entered 
            if (not username) and password:
                Username_Error = customtkinter.CTkLabel(self.frame__login,text='Username is Incomplete',text_color='Orange');Username_Error.place(x=133,y=442)
                Username_Error.after(2000,Username_Error.destroy)
            
            #If The Given Username Is Does Not Exists In The Data Base and Password is Entered
            elif (username and not SERVER.traversal().is_user_exists(username)) and password:
                Username_Not_Exists_Error = customtkinter.CTkLabel(self.frame__login,text=f'The Given Username Does Not Exists',text_color='Orange');Username_Not_Exists_Error.place(x=98,y=442)
                Username_Not_Exists_Error.after(2000,Username_Not_Exists_Error.destroy)
            
            #If Both Username And Password Is not Entered
            elif (not username) and (not password):
                Username_password_Error = customtkinter.CTkLabel(self.frame__login,text='Username and Password is Incomplete',text_color='Orange');Username_password_Error.place(x=96,y=442)
                Username_password_Error.after(2000,Username_password_Error.destroy)

            #If Password Is Not Entered But Username Is Entered
            elif (not password) and username:
                Password_Error = customtkinter.CTkLabel(self.frame__login,text='Password is Incomplete',text_color='Orange');Password_Error.place(x=133,y=442)
                Password_Error.after(2000,Password_Error.destroy)
            
            #If The Username is Entered And The Password Is Wrong
            elif username and (password != self.UserData.get('Password', None)):
                Password_Rule_Error = customtkinter.CTkLabel(self.frame__login,text='The Password is incorrect. Try Again!',text_color='Orange');Password_Rule_Error.place(x=100,y=442)
                Password_Rule_Error.after(2000,Password_Rule_Error.destroy)

            #Successfully Passed All The Criteria
            else:
                Processing = customtkinter.CTkLabel(self.frame__login,text='Processing...',text_color='Orange');Processing.place(x=166,y=442)
                Processing.after(2000, redirect_to_dashboard)


        '''                                                      Special Features                                                             '''


        #Shows The License, Developer, Documentation Options
        def License_Developer_Documentation(self):
            '''Used To Show The License, Developer, Documentation Options To The User ; So The User Can Able To View The License,
            Developer, Documentation'''

            #Shows The License Window
            def Show_License_Window():
                Dev_Doc.destroy()
                License(Detailed_Licence).Show_License()

            #Shows The Documentation Window
            def Show_Documentation_Window():
                Dev_Doc.destroy()
                Documentation().Show_Documentation()

            #Shows The Developer Window
            def Show_Developer_Window():
                Dev_Doc.destroy()
                Developer().Developer_Autentication()

            #Main Window For The License, Developer, Documentation
            Dev_Doc = customtkinter.CTk()
            Dev_Doc.geometry('220x182')
            Dev_Doc.resizable(False,False)
            Dev_Doc.title('Bank\'s Backend Options')

            #self.frame__login For The License, Developer, Documentation
            Dev_Doc_Frame = customtkinter.CTkFrame(Dev_Doc)
            Dev_Doc_Frame.configure(width=200,height=162)
            Dev_Doc_Frame.place(x=10,y=10)

            #Buttons For The License, Developer, Documentation
            customtkinter.CTkButton(Dev_Doc_Frame,text='Developer',font=('Roboto',16,'bold'),fg_color='Orange',hover_color='Yellow',text_color='Black',width=180,height=38,command=Show_Developer_Window).place(x=10,y=12)
            customtkinter.CTkButton(Dev_Doc_Frame,text='Documentation',font=('Roboto',16,'bold'),width=180,height=38,fg_color='#E63B60',hover_color='#067FD0',command=Show_Documentation_Window).place(x=10,y=62)
            customtkinter.CTkButton(Dev_Doc_Frame,text='License',font=('Roboto',16,'bold'),width=180,height=38,fg_color='#797EF6',hover_color='#4ADEDE',command=Show_License_Window).place(x=10,y=112)
            Dev_Doc.mainloop()

        def forgot_security_code(self): # Handles The Forgot Security Code Action

            for widget in [

                self.__heading_reset_password,
                self.__greet_reset_password,
                self.__subheading_reset_password,
                self.__user_icon_label_reset_password,
                self.__username_at_reset_password,
                self.__security_icon_label_reset_password,
                self.__forgot_security_code_button_reset_password,
                self.__security_code_at_reset_password,
                self.__request_reset_password
                
                ]:

                widget.place_forget()

        def request_for_password_reset(self): # Handles The Request To Reset The Password

            username_at_reset_password = self.__username_at_reset_password.get()
            user_security_code_at_reset_password = self.__security_code_at_reset_password.get()

            def security_code_accepted(): # If The Security Code is Accepted Then Change The Password

                for widget in [

                    self.__greet_reset_password,
                    self.__cancel_reset_password,
                    self.__request_reset_password,
                    self.__heading_reset_password,
                    self.__subheading_reset_password,
                    self.__username_at_reset_password,
                    self.__user_icon_label_reset_password,
                    self.__security_code_at_reset_password,
                    self.__security_icon_label_reset_password,
                    self.__forgot_security_code_button_reset_password

                    ]:

                    widget.place_forget()

                self.__username_at_reset_password.delete(0,'end') ; self.__security_code_at_reset_password.delete(0,'end')

                #Hideing All The Items on The Change Password
                def Clear_Change_Password():

                    #Hideing All The Items in The Change Password Window 
                    Accepted_Greet.place_forget();Accepted_Heading.place_forget();Accepted_Subeading.place_forget();Note.place_forget()
                    New_Password_Label.place_forget();New_Password_Reset.place_forget();Confirm_Password_Label.place_forget()
                    Confirm_Password_Reset.place_forget();Change_Password_Button.place_forget();Cancel_Reset_New.place_forget()

                    self.__username_at_reset_password.delete(0,'end');self.__security_code_at_reset_password.delete(0,'end')
                    
                    self.hide_reset_password_frame__show_login_frame()
                
                #Changing The Password
                def Change_Password():

                    #Getting The Passwords
                    New_Password = New_Password_Reset.get()
                    Confirm_Password = Confirm_Password_Reset.get()
                    
                    #if The New Password is Not Entered But The Confirm Password is Entered
                    if (not New_Password) and Confirm_Password:
                        New_Password_Error = customtkinter.CTkLabel(self.frame__reset_password,text='New Password is Incomplete',text_color='Orange');New_Password_Error.place(x=117,y=442)
                        New_Password_Error.after(2000,New_Password_Error.destroy)
                    
                    #if The Cofirm Password is Not Entered But The New Password is Entered
                    elif New_Password and (not Confirm_Password):
                        Confirm_Password_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Confirm Password is Incomplete',text_color='Orange');Confirm_Password_Error.place(x=110,y=442)
                        Confirm_Password_Error.after(2000,Confirm_Password_Error.destroy)
                    
                    #if The Confirm Password is Different From The New Password
                    elif New_Password != Confirm_Password:
                        Pass_differ_Error = customtkinter.CTkLabel(self.frame__reset_password,text='New Password And Confirm Password is Different',text_color='Orange');Pass_differ_Error.place(x=58,y=442)
                        Pass_differ_Error.after(2000,Pass_differ_Error.destroy)

                    #if The Cofirm Password And New Password is Not Entered
                    elif (not New_Password) and (not Confirm_Password):
                        New_Confirm_Password_Error = customtkinter.CTkLabel(self.frame__reset_password,text='New Password And Confirm Password Are Incomplete',text_color='Orange');New_Confirm_Password_Error.place(x=48,y=442)
                        New_Confirm_Password_Error.after(2000,New_Confirm_Password_Error.destroy)

                    #if The New Password Length is less Than 6 Characters
                    elif ((len(New_Password)<6) and (not len(New_Password) == 0)):
                        Password_Rule_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Password Must Contain At least 6 Characters',text_color='Orange');Password_Rule_Error.place(x=70,y=442)
                        Password_Rule_Error.after(2000,Password_Rule_Error.destroy)
                    
                    #Successfully Passed All The Criteria
                    else:

                        try:

                            #Changing The Password
                            self.UserData['Password'] = New_Password

                            #Saying That The Password is Changed
                            Change_Successful = customtkinter.CTkLabel(self.frame__reset_password,text='Password Changed Successfully!\nRedirecting To Login Screen',text_color='Orange');Change_Successful.place(x=105,y=442)
                            Change_Successful.after(5000,Change_Successful.destroy)
                            self.frame__reset_password.after(5000,Clear_Change_Password)

                        except:

                            #if Any Error Occurs
                            Change_Pass_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Some Error Occurred ; Please Try Again Later!',text_color='Orange');Change_Pass_Error.place(x=77,y=442)
                            Change_Pass_Error.after(5000,Change_Pass_Error.destroy)
                            self.frame__reset_password.after(5000,Clear_Change_Password)
                            
                #Main Headings
                Accepted_Greet = customtkinter.CTkLabel(self.frame__reset_password,text='Request Accepted',font=('Roboto',28,'bold'),text_color='#57D956');Accepted_Greet.place(x=75,y=10)
                Accepted_Heading = customtkinter.CTkLabel(self.frame__reset_password,text='You Are One Step Away',font=('Roboto',20,'bold'),text_color='#57D956');Accepted_Heading.place(x=30,y=75)
                Accepted_Subeading = customtkinter.CTkLabel(self.frame__reset_password,text='Enter Required Credentials To Log into Your Account',font=('Roboto',9),height=0);Accepted_Subeading.place(x=33,y=99)
                Note = customtkinter.CTkLabel(self.frame__reset_password,text='*Changes Occurs On The Given Username',font=('Roboto',16,'bold'));Note.place(x=30,y=150)

                #New Password Entry Box
                New_Password_Label = customtkinter.CTkLabel(self.frame__reset_password,text='New Password',font=('Roboto',18,'bold'));New_Password_Label.place(x=30,y=208)
                New_Password_Reset = customtkinter.CTkEntry(self.frame__reset_password,placeholder_text='Example: Viratiaki#2008@Google$10T',height=40,width=340,corner_radius=5,font=('Roboto',16));New_Password_Reset.place(x=30,y=230)

                #Confirm Password Entry Box
                Confirm_Password_Label = customtkinter.CTkLabel(self.frame__reset_password,text='Confirm Password',font=('Roboto',18,'bold'));Confirm_Password_Label.place(x=30,y=288)
                Confirm_Password_Reset = customtkinter.CTkEntry(self.frame__reset_password,placeholder_text='Example: Viratiaki#2008@Google$10T',height=40,width=340,corner_radius=5,font=('Roboto',16));Confirm_Password_Reset.place(x=30,y=310)

                #Change Password Button
                Change_Password_Button = customtkinter.CTkButton(self.frame__reset_password,text='Change Password',width=140,border_width=1,text_color='#3264FF',fg_color='transparent',
                                                       font=('Roboto',16,'bold'),hover_color='Light Blue',command=Change_Password);Change_Password_Button.place(x=122,y=400)
                
                Cancel_Reset_New = customtkinter.CTkButton(self.frame__reset_password,text='Cancel',fg_color='transparent',height=15,border_width=1,hover_color='#A1FB8E',width=45,command=Clear_Change_Password);Cancel_Reset_New.place(x=2,y=538)
            
            #If the Username Is Not Entered But Security Code Is Entered 
            if (not username_at_reset_password) and user_security_code_at_reset_password:
                Username_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Username is Incomplete',text_color='Orange');Username_Error.place(x=133,y=442)
                Username_Error.after(2000,Username_Error.destroy)
            
            #If The Given Username Is Does Not Exists In The Data Base and Password is Entered
            elif (username_at_reset_password and not SERVER.traversal().is_user_exists(username_at_reset_password)) and user_security_code_at_reset_password:
                Username_Exists_Error = customtkinter.CTkLabel(self.frame__reset_password,text=f'The Given Username Does Not Exists',text_color='Orange');Username_Exists_Error.place(x=98,y=442)
                Username_Exists_Error.after(2000,Username_Exists_Error.destroy)
            
            #If Both Username And Security Code Is not Entered
            elif (not username_at_reset_password) and (not user_security_code_at_reset_password):
                Username_password_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Username and Security Code is Incomplete',text_color='Orange');Username_password_Error.place(x=85,y=442)
                Username_password_Error.after(2000,Username_password_Error.destroy)

            #If Security Code Is Not Entered But Username Is Entered
            elif (not user_security_code_at_reset_password) and username_at_reset_password:
                Password_Error = customtkinter.CTkLabel(self.frame__reset_password,text='Security Code is Incomplete',text_color='Orange');Password_Error.place(x=126,y=442)
                Password_Error.after(2000,Password_Error.destroy)
            
            #If The Username is Entered And The Security Code Is Incorect
            elif username_at_reset_password and (user_security_code_at_reset_password != self.UserData.get('Security Code')):
                Password_Rule_Error = customtkinter.CTkLabel(self.frame__reset_password,text='The Security Code is incorrect. Try Again!',text_color='Orange');Password_Rule_Error.place(x=87,y=442)
                Password_Rule_Error.after(2000,Password_Rule_Error.destroy)

            #Successfully Passed All The Criteria
            else:
                Processing = customtkinter.CTkLabel(self.frame__reset_password,text='Requesting...',text_color='Orange');Processing.place(x=166,y=442)
                Processing.after(2000,Processing.place_forget)
                Processing.after(2000,security_code_accepted)

