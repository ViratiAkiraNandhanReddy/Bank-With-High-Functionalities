import os
#Knowing The Path Of The Package
Check_Location=os.getcwd()
if 'Main_File' not in Check_Location:
    Path = Check_Location + "\\Main_File"
else:
    Path = Check_Location
    
with open(fr'{Path}\Data_Of_User.txt') as Data:
    Accounts:list[str] =eval(Data.readline())
    PinCodes:list[str]=eval(Data.readline())
    Security:list[str]=eval(Data.readline())

def User_func(User=None)->int:
    User_index = Accounts.index(User)
    return User_index

def Licence():
    pass

def Documentation()->str:
    pass

print('Hello')