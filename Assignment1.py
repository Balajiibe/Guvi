import re
import pandas as pd

 
def Register():

  db=open("database.csv",'a')
  UserName = input('Create User: ')
  Password = input('Create Password: ')
  ValidUserName=re.match('^[a-zA-Z]+[a-zA_Z0-9_\-\.]*@[a-zA-Z]{4,9}.[a-zA-Z]',UserName)
  ValidPassword="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%&*?])[A-Za-z\d@$!#%*?&]{5,16}$"
  Pw=re.compile(ValidPassword)
  MatchPass = re.match(Pw,Password)
  db.close()
  Users=[]   
  try:
    db=pd.read_csv("/content/database.csv")
    df=pd.DataFrame(db)
  # print(df['UserName'])

    for i in df['UserName']:
      Users.append(i.lower())
  # print(Users)
  except:
    pass  
  if UserName in Users:
    print('User Already Exists, Try Log in')
    Login()

  else :
    if ValidUserName:
      
      if MatchPass:
        # db.close()
        db=open('database.csv','a')
        db.write(UserName+ ', '+ Password +'\n')
        db.close()
        print('User created Successfully')
      else :
        print('Weak Password, Please Try again' )
        Register()
    else :
      print('User Id not valid, Please try again')
      Register()


def Login():
  Users=[]
  try:
    db=open("database.csv",'a')
    db.close()
    db=pd.read_csv("/content/database.csv")
    df=pd.DataFrame(db)
    for i in df['UserName']:
      Users.append(i.lower())
    if UserName in Users:
      pass

  except :
    print('User not Exists')
  

# Register()  
# Login()
ip=input('Please choose Register/ Login or forget Password:')
if ip.title()=='Register':
  Register()
elif ip.title()=='Login':
  Login()
elif ip.lower()=='forget password':
  pass 
