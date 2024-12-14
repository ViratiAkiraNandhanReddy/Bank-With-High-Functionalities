import os
#Knowing The Path Of The Package
Check_Location=os.getcwd()
if 'Main_File' not in Check_Location:
    Path = Check_Location + "\\Main_File"
else:
    Path = Check_Location
    
with open(fr'{Path}\Data_Of_User.txt') as Data:
    Accounts=eval(Data.readline())
    PinCodes=eval(Data.readline())




def Licence():
    pass

def Documentation()->str:
    pass