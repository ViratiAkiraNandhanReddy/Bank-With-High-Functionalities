'''Hello I'm Virati Akira Nandhan Reddy This Is My First Biggest Project At My age(16) at Class 11
Project 001 Title: Project Bank
**Special Tool**
1.Developer
                                                                       Start Date:9.Nov.2024 
                                                                       Time:5:33 PM

                                                                       End Date:4.Dec.2024
                                                                       Time:8:42 PM
Time Spent For This Project:76hrs
With No Source Used(Total Own)
Special Thanks To My             Teacher:Smita Tiple Mam (PGT Computer Science)
                                        
From PM Shri Kendriya Vidyalaya Warangal
Python Version Used:3.13.0
Code Editer Used:Visual Studio Code
program Consisting 900 lines(including Comments)

What this Program Can Do:
1.Login Screen
2.Show Balance
3.Deposit Amount
4.WithDraw Amount
5.Change PassCode
6.Create Account
7.Delete Account
8.Developer Mode

**Next Target**
Use Tkinter

***This Program Is Still In Developing Stage***'''
from time import sleep
from json import dumps
from os import getcwd
from datetime import datetime

#Making As A Module to Reuse
def Bank()->None:
    #An Infinite Loop
    while True:

        #Getting The Current Working Directory
        location=getcwd()

        #Checking Does File Exists
        try:
            x=open(f'{location}\\User_Data.txt','r')
        
        #Plan for if File Not Exist
        except FileNotFoundError:
            x=open(f'{location}\\User_Data.txt','a')

            #ReWriting Whole Requirements in New File
            x.write("['Developer','AKI','Akki']")
            x.write('\n[0,1000,100]')
            x.write('\n[4321,1000,1001]')
            x.write('\n10E6')
            x.write('\n[]')
            x.write('\n[]')
            x.write('\n[]')
            x.write('\n[0,10E5,10E5]')
            x.write('\n[0,0,0]')
            x.write('\n[0,0,0]')
            x.write('\n[0,0,0]')
            x.write('\n[]')
            x.write("\n{'AKI':10}")
            #x.write("\n[{'None':None},{'Date:29/10/2024 Time:07:45:22 AM':'Account Created'}]")
            x.close()
            10E3

        #Atlast Opening File
        finally:
            x=open(f'{location}\\User_Data.txt','r')

            #Initial Values
            accounts:list[str]=eval(x.readline())
            balance:list[int|float]=eval(x.readline())
            pincode:list[int]=eval(x.readline())

            #Bank Records
            Acc_of_Bank=eval(x.readline())

            #Record For Closed Accounts 
            acclose=eval(x.readline())
            acclosepass=eval(x.readline())
            acclobal=eval(x.readline()) 

            #Details For Loan Lenders
            loanavail:list[float]=eval(x.readline())
            loantk:list[int|float]=eval(x.readline())
            interest:list[float]=eval(x.readline())
            rate_of_int:list[float]=eval(x.readline())
            dev_inter:list[int|float]=eval(x.readline())   
            profit_fr_user:dict[str|float]=eval(x.readline())
            x.close()

        #Details For Transaction History
            tran_hist_user={}
            
        #Stater Key Function **Very Important**
        def userid()->int:
            global user
            user=accounts.index(username)
            return user
        
        #passCode To Acess The Accounts
        def PassCode()->None:
            #inside function to Fix a Bug 
            def inside():
                try :
                    pin=int(input('Enter 4-Digit PassCode:'))
                    if len(str(pin))== 4:
                        #Checking For PassCode Is Correct Go Inside 
                        if pincode[(userid())] == pin:
                            #Special Access To Developer
                            if username == 'Developer':
                                Developer()
                                login()
                            loop()
                        else:
                            print('Wrong PassCode')
                            login()
                    else:
                        print('Invalid PassCode')
                        login()

                except ValueError:
                    print('Kindly Enter PassCode!!')
                    login()
                    
            inside()
                    
        #To Show Balance
        def Balance()->None:
            print(f'Your Balance is ${balance[accounts.index(username)]:.2f}')

            #Only Executes If Loan Taken
            if loanavail[user] != 10E5 and interest[user] !=0 :
                print(f'Credit Taken From Bank:${loantk[user]} And Interest Of ${interest[user]:.0f}')

        #To Deposit Amount
        def Deposit()->int:
            #Human errors
            try:
                deposit=float(input('Enter Amount To Be Added:'))

                #Checking Does The Amount Entered Is less Than Zero
                if deposit<=0:
                    print('Amount Can\'t be <=0')
                else:     
                    balance[accounts.index(username)]+=deposit
            except ValueError:
                print('Kindly Enter Valid Amount')
                
        #To WithDraw Amount
        def WithDraw()->int:
            try:
                witdraw=float(input('Enter Amount To Be WithDrawn:'))

                #Checking Does The Amount is Grater Than The Users Balance
                if witdraw>(balance[accounts.index(username)]):
                    print('Insufficient Balance')
                else:
                    balance[accounts.index(username)]-=witdraw
            except ValueError:
                print('Kindly Enter Valid Amount')
        
        #Making Things Shorter
        Acpin_rules='''                                                             ****Rules For PassCode****
                                                            1.Must Contain 4-Digit Only
                                                             2.Should Not Start With 0
                                                     3.Symbols and Alphabet Not Allowed For Pin'''
        
        #To Create An Account
        def Account()->None:
            create=input("Enter UserName To Be Added(Case Senstive):")
            if create == '':
                print('Symbols Are Allowed;But Not empty Space')
                Account()
            elif create.isdigit()==True:
                print('Only Numbers Are Not Allowed')
                Account()

            #Checking Existence Of Account
            elif create in accounts:
                print('Account Already Exist')
                Account()
            else:
                #For pin Generation
                def appin()->None:
                    print(Acpin_rules)
                    try:
                        appenpin=int(input('Enter PassCode For Your New Account:'))
                        if len(str(appenpin))==4:
                            #For Main Accounts
                            pincode.append(appenpin)
                            accounts.append(create)
                            balance.append(0)

                            #For Loan Lenders
                            loanavail.append(10E5)
                            loantk.append(0)
                            interest.append(0)
                            rate_of_int.append(0)

                            print()
                            print('Account Created!!'.center(130))
                            print()
                        else:
                            print()
                            print('Account Creation UnSuccessful!!'.center(130))
                            print()
                    except ValueError:
                        print('Please Enter A Valid PassCode')
                appin()
                    
                #Redirect to Login Screen    
                login()

        #To Close An Account
        def Close()->None:
            clo=input("Are you Sure:")
            if clo in ['Yes','yes','yeah','y','yep','oh yeah']:

                #Removeing All the Details of User From The Accounts
                name=accounts.pop(user)
                bal=balance.pop(user)
                pindil=pincode.pop(user)
                print(f'Account:{name} With PassCode:{pindil};Balance Available:{bal:.2f} (**Has Been Disabled/Deleted!!**)')

                #For Developer importance
                acclose.append(name)
                acclosepass.append(pindil)
                acclobal.append(bal)
            else:
                print('Invalid Entry')
                
        #Changing The PassCode
        def ChangePassCode()->None:
            print(Acpin_rules)
            try:
                newpass=int(input('Enter New PassCode:'))
                if len(str(newpass))==4:
                    pincode[user]=newpass
                    print('Changing In'.center(130))
                    sleep(1)
                    print('3'.center(130))
                    sleep(1)
                    print('2'.center(130))
                    sleep(1)
                    print('1'.center(130))
                    print(f'user:{username} With Balance:{balance[accounts.index(username)]:.2f}!!**PassCode Changed:{newpass}**')
                    print()
            except ValueError:
                print('Invalid PassCode Entered (Nothing Changed!)')

        #Sending Amount To Other Accounts
        def send_oth()->None:
            Receiver=input('Enter Receiver UserName:')

            #Searching The User in DataBase
            if Receiver in accounts and Receiver != username:
                print('User Found'.center(130))
                temp=accounts.index(Receiver)
                try:
                    amt=float(input('Enter Amount For Sending:'))
                    if amt <= balance[user]:
                        try:
                            lenpin=int(input('Enter 4-Digit PassCode For Confirmation:'))
                            if len(str(lenpin)) == 4:
                            #Checking For PassCode if Correct then Go Inside 
                                if pincode[(userid())] == lenpin:
                                    balance[temp]+=amt
                                    balance[user]-=amt
                                    print(f'Amount of {amt:.2f} Sent To UserName: {Receiver} ')
                                    print()
                                    print('Transaction Successful!!'.center(130))
                                    print()      
                                else:
                                    print('Wrong PassCode')
                                    print()
                                    print('Transaction Failed!!'.center(130))   
                                    print()       
                            else:
                                print('Invalid PassCode')
                                print()
                                print('Transaction Failed!!'.center(130))
                                print()
                        except ValueError:
                            print('Kindly Enter Valid PassCode!!')
                            print()
                            print('Transaction Failed!!'.center(130))
                            print()
                    else:
                        print('Insufficient Balance')
                
                except ValueError:
                    print()
                    print('Invalid Input Were Given!!'.center(130))
                    print('Transaction Failed!!'.center(130))
                    print()

            else:
                if Receiver not in accounts:
                    print(f'UserName:{Receiver} Wasn\'t Found In Bank\'s DataBase'.center(130))
                elif Receiver == username:
                    print('Self Transfer Is Not Possible'.center(130))
        
        #Saving all The Info of Users in .txt file
        def savtxt()->None:
            '''Saving All The Details of the Users In A Txt File To Avoid removing The User Data That Includes:
            1.Username
            2.Passcode
            3.Balance
            4.Developer requirments
            etc..'''
            c=open(f'{location}\\User_Data.txt','w')
            c.write(f'{str(accounts)}')
            c.write(f'\n{str(balance)}')  
            c.write(f'\n{str(pincode)}')
            c.write(f'\n{str(Acc_of_Bank)}')
            c.write(f'\n{str(acclose)}')
            c.write(f'\n{str(acclosepass)}')
            c.write(f'\n{str(acclobal)}')
            c.write(f'\n{str(loanavail)}')
            c.write(f'\n{str(loantk)}')
            c.write(f'\n{str(interest)}')
            c.write(f'\n{str(rate_of_int)}')
            c.write(f'\n{str(dev_inter)}')
            c.write(f'\n{str(profit_fr_user)}')
            #c.write(f'\n{str()}')
            #c.write(f'\n{str()}')
            #c.write(f'\n{str()}')
            #c.write(f'\n{str()}')
            c.close()

        #For Developer console
        def Developer()->None:
            while True:
                print('<For Help:opts>')
                dev=input("<Console>")

                #Help Developer
                if dev == 'opts':
                    print('savacc:Save All Info Of Users In Servers')
                    print('totbal:Total Balance in Bank')
                    print('inpdbk:Total *Interest* Paid To Bank Form Users(Loan)')
                    print('pruser:Total Amount Extra Paid By User At Loan Repay (Profit)')
                    print('totap:Total Accounts Available(excludes Developer)')
                    print('delacc:Accounts That Closed In Bank')
                    print('totacc:Accounts Available in Server')
                    print('exitdev:Exit Developer Mode')
                    print('forcequit:quit all The Program And Deletes All The Accounts')
                
                #Save All Info In .txt File
                elif dev == 'savacc':
                    savtxt()
                    print()
                    print('All Accounts Information Saved Successfully!!'.center(130))
                    print()

                #Exit From Developer Mode  
                elif dev == 'exitdev':
                    break

                #Review the Accounts Closed in Program
                elif dev == 'delacc':
                    a=0
                    b=0
                    f=1
                    print('***Accounts Deleted***'.center(130))
                    for i in acclose:
                        print(f'{f}.User:{i} : PassCode:{acclosepass[a]} : Balance:${acclobal[b]:.2f}'.center(130))
                        f+=1
                        b+=1
                        a+=1
                
                #Review the Accounts Present in Program
                elif dev == 'totacc':
                    a=0
                    b=0
                    f=1
                    print('***Accounts Available***'.center(130))
                    for i in accounts:
                        print(f'{f}.User:{i} : PassCode:{pincode[a]} : Balance:${balance[b]:.2f}'.center(130))
                        f+=1
                        b+=1
                        a+=1
                                
                #Total Balance Available in Bank
                elif dev == 'totbal':
                    balav=sum(balance)
                    print(f'Total Balance Available in Bank ${balav}'.center(130))

                #Total Accounts Available
                elif dev == 'totap':
                    totap=(len(accounts)-1)#To Exclude Developer Account
                    print(f'Total Accounts Available(excludes Developer) Are:{totap}'.center(130))
                
                #Forceful Quit the Whole Program
                elif dev == 'forcequit':
                    savtxt()
                    print('<This Might Crash The Whole Program And Save The Details of The Users>')
                    devs=input('<Are You Sure(YES/NO)>')
                    if devs == 'YES':
                        print('Quiting In'.center(130))
                        sleep(1)
                        print('3'.center(130))
                        sleep(1)
                        print('2'.center(130))
                        sleep(1)
                        print('1'.center(130))
                        sleep(1)
                        print('Successful Quit'.center(130))
                        print("Created By Virati AKira Nandhan Reddy".center(130))
                        raise Exception('All Accounts Saved SuccessFuly!!')
                    elif devs == "NO":
                        print("<Great!!>")
                    else:
                        print('<Error>')
                
                #Interest Paid To Bank
                elif dev == 'inpdbk':
                    print(f'Total *Interest* Paid To Bank Form Users(Loan):${sum(dev_inter)}'.center(130) if sum(dev_inter)>0 else \
                          'None Of The User Taken Credit From The Bank'.center(130))
                
                #Extra Paid By The Users
                elif dev == 'pruser':
                    print(dumps(profit_fr_user,indent=90))
                    print(f'Total Amount Extra Paid By User At Loan Repay (Profit):${sum(profit_fr_user.values())}'.center(130))
                    
                #If Other Input Given
                else:
                    print('<invalid>')
        
        #To Contact With Developer
        def contact_dev()->None:

            #This Function is Under Developement
            print()
            print('Under Developement ; Not Accessible!!'.center(130))
            print()
            loop()
            while True:
                print()
                print('''Available Chat Options:
    Plan:Conversation Fee
    1.Basic:Free
    2.Diamond:$50
    3.Premium:$80
    4.Premium plus:$120
    5.Help:Explain All The Plans
    6.Exit Contact Developer''')
                
                #For Lowest Features
                def Basic():
                    '''1.'''
                    pass

                #For  Medium Features
                def Diamond():
                    choice=0

                #For High Features
                def Premium():
                    choice=input('Enter Your Choice (1-)')

                #For Maximum Features
                def Premium_Plus():
                    pass    

                #To Explain All The Plans
                def Help():
                    pass   
                
                chat=input('Enter Your Choice (1-6):')
                match chat: #Choice selection 
                    case '1':
                        Basic()
                    case '2':
                        Diamond()
                    case '3':
                        Premium()
                    case '4':
                        Premium_Plus()
                    case '5':
                        Help()
                    case '6':
                        print()
                        print('Thank You For Your Time!!'.center(130))
                        print()
                        break
                    case _:
                        print('Sorry! To Say That\'s Invalid Input')

        #loop for each User
        def loop()->None:
            while True:

                #Options For User
                print('1.Check Balance'.center(130))
                print('2.Deposit Amount'.center(130))
                print('3.Withdraw Amount'.center(130))
                print('4.Send Amount To Other Accounts'.center(130))
                print('5.Transaction History'.center(130))
                print('6.Create An New Account'.center(130))
                print('7.Loan From Bank'.center(130))
                print('8.Close This Account'.center(130))
                print('9.Change PassCode'.center(130))
                print('10.Contact Developer'.center(130))
                print('11.Exit'.center(130))

                #Only Excutes If They Taken Loan
                if loanavail[user] != 10E5:
                    print('12.Repay The Loan Amount'.center(130))
                    print('13.Loan Portfolio'.center(130))

                #For The Other Inputs text
                def invid():
                    print()
                    print('****Invalid Choice****'.center(130))
                    print()
                
                #Choice Selection
                Choice=input('Enter Your Choice (1-11):' if loanavail[user]==10E5 else 'Enter Your Choice (1-13):')

                match Choice: #Works Like If Else Statements
                    case "1": #Check Balance
                        Balance()
                    case "2": #Deposit Amount
                        Deposit()
                    case "3": #Withdraw Amount
                        WithDraw()
                    case "4": #Send Money Others
                        send_oth()
                    case "5": #Transaction History 
                        tran_hist()
                    case "6": #Create Account
                        Account()
                    case "7": #Loan From Bank
                        loan_bank()
                    case "8": #Close Account
                        Close()
                        login()
                    case "9": #Change PassCode
                        change=input('Are You Sure(Yes/No):')
                        if change == 'Yes':
                            ChangePassCode()
                        else:
                            print()
                            print('PassCode Not Changed'.center(130))
                            print()
                    case "10": #Contact Developer
                        contact_dev()
                    case "11": #Exit Loop
                        login()
                        break
                    case "12": #Repay Loan
                        if loanavail[user] != 10E5:
                            repay_loan()
                        else:
                            invid()
                    case "13": #Loan Portfolio
                        if loanavail[user] != 10E5:
                            loan_port()
                        else:
                            invid()       
                    case _: #Errors
                        invid()

        #Transaction History Of Users
        def tran_hist():
            print()
            print('Under Developement ; Not Accessible!!'.center(130))
            print()
            loop()
            '''datetime.now().strftime('Date:%d/%m/%Y Time:%I:%M:%S %p') and print(datetime.now().strftime('%I:%M:%S %p'))'''
            '''try:
                c=open(f'{location}\\Transaction History\\{username}_Tran_Hist')
            except FileNotFoundError:
                pass'''

        #Credit From Bank (Loan)
        def loan_bank()->None:
            try:
                print(f'Loan Amount Available For You ${loanavail[user]:.2f}'.center(130))
                lenam=float(input(f'Enter Amount Required (1 - {loanavail[user]}):'))
                if lenam>0 and lenam<=loanavail[user]:
                    print()
                    print(f'For The Amount ${lenam} Rate Of Interest Might be {rate_int(lenam)}%'.center(130))
                    print()
                    verify=input('Is That OK For You (Yes/No):')
                    if verify in ['Yes','yes','yeah','y','yep','oh yeah','Y']:
                        try:
                            lenpin=int(input('Enter 4-Digit PassCode For Confirmation:'))
                            if len(str(lenpin))== 4:

                            #Checking For PassCode if Correct then Go Inside 
                                if pincode[(userid())] == lenpin:
                                    balance[user]+=lenam
                                    loantk[user]+=lenam
                                    loanavail[user]-=lenam
                                    rate_of_int[user]=rate_int(lenam)
                                    interest[user]=round(((rate_of_int[user]/100)*loantk[user]),2)
                                    dev_inter.append(interest[user])
                                    print(f'Amount of {lenam:.2f} Credited To UserName: {username} ')             
                                else:
                                    print('Wrong PassCode')     
                            else:
                                print('Invalid PassCode')
                        except ValueError:
                            print('Kindly Enter Valid PassCode!!')                    
                    else:
                        print()
                        print('Have A Great Day!'.center(130))
                        print()
                else:
                    if lenam <=0:
                        print('Amount Can\'t be Negative or Zero')
                    elif lenam>loanavail[user]:
                        print('Insufficient Lend Amount Available!')           
            except ValueError:
                print()
                print('***Invaid Input Recevied***'.center(130))
                print()

        #Repaying The Loan
        def repay_loan()->None:
            try:
                repay=float(input('Enter Amount To Repay:$'))
                temp_int=round(repay-loantk[user],2)

                #For Less Paying Users
                def less_pay()->None:
                    if interest[user] != 0:
                        if repay < interest[user]:
                            interest[user]-=repay
                        else:
                            loan_tk=repay-interest[user]
                            interest[user]-=interest[user]
                            balance[user]-=loan_tk
                            loanavail[user]+=loan_tk
                            loantk[user]-=loan_tk
                    elif interest[user] == 0:
                        balance[user]-=repay
                        loanavail[user]+=repay
                        loantk[user]-=repay

                #For Correct Paying Users
                def corr_pay()->None:
                    #Collecting The Amount Same as The Lend+Interest
                    loanavail[user]+=(repay-interest[user]) 
                    loantk[user]-=(repay-interest[user])
                    interest[user]-=temp_int
                    balance[user]-=repay

                #Saying Thanks And Portfolio After Repaying The Loan
                def good()->None:
                    if (loanavail[user] == 10E5 and loantk[user] == 0) and interest[user] == 0:
                        rate_of_int[user]=0
                        print()
                        print('**Thank You For Repaying The Loan Completely**'.center(130))
                        print()
                        verify=input('Do You Want To See The Loan Portfolio After Repay (For Verification Purpose):')
                        if verify in ['Yes','yes','yeah','y','yep','oh yeah','Y']:
                            loan_port()
                        else:
                            print()
                            print('Great Day Then; Bye!!'.center(130))
                            print()
                      
                #For Extra Paying Users To Bank(Donates)
                def hi_pay_tip()->None:
                    profits=repay-(loantk[user]+interest[user])

                    #Records For The Developer If They Want Their Money Back
                    if username in profit_fr_user: #existing Users
                        profit_fr_user[username]+=profits
                    else: #New Users
                        profit_fr_user[username]=profits

                    loanavail[user]=10E5
                    loantk[user]=0
                    interest[user]=0
                    balance[user]-=repay
                    print()
                    print(f'Thanks For The Extra Pay Of ${profits};This Might Help The Bank'.center(130))
                    print('**If You Want The Extra Money Back To Your Account : Please Contact Developer**'.center(130))
                    print()
        
                if repay<=balance[user]:
                    if repay<(loantk[user]+interest[user]): #For The Users Who Pays Less
                        less_pay()
                    elif repay == (loantk[user]+interest[user]): #For The Users Who Pays Exactly
                        corr_pay()
                    elif repay>(loantk[user]+interest[user]): #For The Users Who Pays High Rich People
                        hi_pay_tip()
                else: #Intelligent User
                    print('Insufficient Balance Available In Your Account To Pay The Loan')

                good()
                
            #For Invalid Entry Users
            except ValueError:
                print()
                print('Invalid Amount Entered!!'.center(130))
                print()
    
        #Detalis About Loan
        def loan_port()->None:
            #Gives the details of the loan
            print()
            print(('-'*120).center(130))
            print(f'Loan Available For You ${loanavail[user]:.2f}'.center(130))
            print(f'Total Amount Credited From Bank ${loantk[user]}'.center(130))
            print(f'The Rate Of Interest For This Loan:{rate_of_int[user]}%'.center(130))
            print(f'Amount To Be Paid To Bank ${loantk[user]} + interest: ${interest[user]}'.center(130))
            print(f'Total Amount To Be Paid:{loantk[user]+interest[user]}'.center(130))
            print(('-'*120).center(130))
            print()

        #Rate Of Interest
        def rate_int(lenam)->float | str:

            #This Func Will Decide the Rate of Interest
            if lenam >0 and lenam<=100000:
                return 7.83
            elif lenam >100000 and lenam<=300000:
                return 5.91
            elif lenam >300000 and lenam<=600000:
                return 4.69
            elif lenam >600000 and lenam<=800000:
                return 3.45
            elif lenam >800000 and lenam<=1000000:
                return 1.91
            else:
                return '**Maximum Amount Exceded**'

        #login Screen For User
        def login()->None:
            global username
            username=input('Enter User Name (Case Senstive):') 
            if username in accounts:
                PassCode()
            else:
                print()
                print('''***Oops! Account Not Available***'''.center(130))
                print()
                create=input('Do You Want To Create An Account:')
                if create in ['Yes','yes','yeah','y','yep','oh yeah','Y']:
                    Account()
                else:
                    print()
                    print('Have A Great Day!!'.center(130))
                    print()
                    login()
        login()

#For Documentation 
def Documentation()->str:
    return '''                
------------------------------------------------------------------------------------------------------------------------
                                       Hey!! There This Is The Documentation Of This Bank.



I'm Going To Explain How Does The Bank Works?
There Is A Special Tool Called Developer Tools; Which Can Be Accessed By Login Screen, Using The Username Developer.


Time Spent With This Project Is About 76 Hours. 
With None Of The Source Used Every Single Line Of Code Is Hand Written; Not Seen In Any Source.

------------------------------------------------------------------------------------------------------------------------
I'm From PM Shri Kendriya Vidyalaya Warangal
Python Version Used: 3.13.0
Code Editor Used: Visual Studio Code
This Programme Consisting Of 900 Lines(Including Comments).
------------------------------------------------------------------------------------------------------------------------

What's Special About This Project? I Just Mean To Say That The Functionalities Of These Project.
1.Login Screen.
2.Showing The Balance Of User
3.Depositing Amount.
4.Withdrawal Of Amount.
5.We Can Change The Passcode As We Want.
6.Create A Account.
7.We Can Also Delete The Account.
8.We Can Take The Loan Of $1 Million.
9.We Can Also Send Money To Other Accounts.


**The Highly Useful Feature Is:
        In This Project, The Accounts Data Which Is Provided To The Bank Will Be Saved In A Textual Format In A Txt File.
        Which Is A Good For The Backup. So The All Accounts Which Are Saved In That Txt File Will Be Remained Unremoved/Undeleted
        Which Is A Good Sign For This Project.

        Also, When We Stop The Bank Forcefully, The Data Will Be Again Stored In The Txt File, Overriding The Previous File.
        Without Disturbing Any Data And Details Of The User. Which Is Highly Secure.


**User Balance Is Encrypted Using The PassCode Functionality 


-----------------------------------------------------------------------------------------------------------------------------
There Is A Developer Mode, Which Has A Very Useful Features For The Developer. That Includes:
1.Saving All The Accounts Details In The Txt File
2.Displaying The Deleted Accounts
3.Total Balance In Whole: Sum Of The All Users Money/Amount.
4.Total User Present In This Bank At The Present A Time.
5.Total Account Present In The Bank (Number Of Accounts), Excluding The Developer Account.
6.Force Quitting The Whole Programme. And Saving The Account Details In That Same Particular Txt File.
7.Some Of The People In Them Might Be Rich. They Might Pay Higher Amount Than They Need To Pay At Loan Repay. 
  That Will Be Recorded And It Can Be Accessed By The Developer, Including The Username And Amount They Paid Extra.
-----------------------------------------------------------------------------------------------------------------------------


***There Is An Also A Good Feature That Is Contact Developer,Transaction History,etc.. 
Which Is Under Development So That Won't Works Right Now.


----------------------------------------------------------------------
There Is The Three Options To Repay The Loan
1.Less Pay Those Users Who Pay Lesser Amount Than The Repay Amount
2.Pay Exactly Correct. Which Takes The Exactly Amount From The User Which Is Lended By The Bank
3.Those Users Pay Higher Amount Than They Lend Amount.
-----------------------------------------------------------------------


There Is An Also Another Functionality Which Says The Portfolio Of The Loan
1.The Interest Of Taken Amount
2.The Loan Available For The User 
3.Total Amount Credited From The Bank
4.The Rate Of Interest
5.Total Amount To Be Paid Again To The Bank.

There Is An Functionality Which Decide. Which Decides The Interest According To The Lend The Amount Which Is Required To The User


******************************************************** Highly Important *****************************************************

                               ********* Last But Not Least *********

When You Want To Close The Program You Must Need To Stop It By The Developer Option forcequit
>>>Otherwise The User Data Will Be Crashed And Deleted This Might Be Dangerous To The Users Money

                                 ⚠  So This Is The Big Warning Be Careful  ⚠


---------------------------------------------------------------------------------------------------------------------------------

This Project Is Created By The Virati Akira Nandhan Reddy 
A Student Of Smita Tiple (PGT Computer Science)
From PM Shri Kendriya Vidyalaya Warangal
At The Creation Of this Project My Age Was About 16 Years
I'm From Class 11 Science

                                       **** For Better Experience/View Use This Bank In Full Screen Mode ****


                                                    Thank You For Using Of This Project

---------------------------------------------------------------------------------------------------------------------------------'''

#For Modules 
if __name__=='__main__':
    def start():
        #Introducing MySelf
        print()
        print('Hey! There I\'m Virati Akira Nandhan Reddy Creator Of This Project Bank'.center(130))
        print()
        print('Starting The Bank In'.center(130))
        sleep(1)
        print('3'.center(130))
        sleep(1)
        print('2'.center(130))
        sleep(1)
        print('1'.center(130))
        print('Successfully Started'.center(130))
        print()
        
        #Starting Main Module
        Bank()
    
    #Asking The Reader for Documentation
    verify=input('Do You Want To Read Documentation:')
    if verify in ['Yes','yes','yeah','y','yep','oh yeah','Y']:
        print()
        print('The Bank Will Start Automatically After 2 Minutes'.center(130))
        print()
        print(Documentation())
        print()
        sleep(120)
        start()
    else:
        start()
    

'''                                                          End Of Program                                                        '''
