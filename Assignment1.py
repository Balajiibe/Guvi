import re
import json

lst=[]
UserInput=input('Register/Login: ')

if UserInput.title()=='Register':
  UserId=input('UserId: ')
  Password=input('Password: ')
  UserId=re.match('^[a-zA-Z]+[a-zA_Z0-9_\-\.]+@[a-zA-Z]{4,9}.[a-zA-Z]',UserId)
  MatchPass="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%&*?])[A-Za-z\d@$!#%*?&]{5,16}$"
  Pw=re.compile(MatchPass)
  Pass=re.match(Pw,Password)
  print(UserId.string)
  print(Pass.string)
  f = open("demofile.json", "a")
  # f.write(dict{'UserId':UserId,'Password':Pass})
  f.close()
if UserInput.title()=='Login':
  print('login')
