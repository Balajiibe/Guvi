import re as re
class ProjectLogin:

    def Purpose(self):
        self.Flow=input('Please Select Register / Login: ')
        if self.Flow.title()=='Register':
            self.Register()
        elif self.Flow.title()=='Login':
            self.Login()
        else :
            print('Please select Valid input')
    def Register(self):
        self.GetUserId()
    def GetUserId(self):
        self.UserId=input('Enter UserId: ')
        self.UserId=self.UserId.lower()
        ValidUserName = re.match('^[a-zA-Z]+[a-zA_Z0-9_\-\.]*@[a-zA-Z]{4,9}.[a-zA-Z]', self.UserId)
        if ValidUserName and self.Flow.title()=='Register''':
            print('U Id Valid')
            self.CheckUserId()
        elif ValidUserName and self.Flow.title()=='Login':
            self.CheckUserId()
        else:
            print('UserId Not Valid')
            self.GetUserId()
    def CheckUserId(self):
        DataBase = open("DataBase.txt", 'r')
        # print(DataBase.read())
        U = []
        P = []
        for i in DataBase:
            a, b = i.split(', ')
            b = b.strip()
            U.append(a)
            P.append(b)
        self.datas = {'UserId': [], 'Password': []}
        self.datas.update({'UserId': U, 'Password': P})
        # print(self.datas['UserId'])
        if self.UserId in self.datas['UserId'] and self.Flow.title()=='Register' :
            print('UserId Already Exists Please Login, Try Login')
            self.Flow='Login'
            self.Login()
        elif self.UserId in self.datas['UserId'] and self.Flow.title()=='Login' :
            print('u id in db')
            self.GetPassword()
        elif self.UserId not in self.datas['UserId'] and self.Flow.title()=='Login' :
            print('u id not in db, Try Register')
            self.Flow='Register'
            self.Register()
        elif self.UserId not in self.datas['UserId'] and self.Flow.title() == 'Register':
            self.GetPassword()

    def GetPassword(self):
        self.Password = input('Enter Password: ')
        ValidPassword = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%&*?])[A-Za-z\d@$!#%*?&]{5,16}$"
        Pw = re.compile(ValidPassword)
        self.MatchPass = re.match(Pw, self.Password)
        if self.Flow.title() == 'Register' and self.MatchPass:
            self.InsertNewId()
        elif self.Flow.title() == 'Register':
            print('Enter Strong Password')
            self.GetPassword()
        elif self.Flow.title()=='Login':
            self.IdIndex = self.datas['UserId'].index(self.UserId)
            if self.UserId == self.datas['UserId'][self.IdIndex]:
                if self.Password == self.datas['Password'][self.IdIndex]:
                    print('Hi ' + self.UserId + ' Welcome back')
                else:
                    i = 1
                    while i <= 3:
                        print('Wrong Password Try Again ' + 'no of attempts ' + str(i))
                        i = i + 1
                        if self.Password == self.datas['Password'][self.IdIndex]:
                            print('Hi ' + self.UserId + ' Welcome back')
                            break
                        elif i>3:
                            print('Entered wrong password many times')
                            print('Please update new Password')
                            self.Login()
                            # self.ForgetPassword()
                            break
                        else:
                            self.Password=input('Re-Enter Password: ')



    def InsertNewId(self):
        db = open("DataBase.txt", 'a')
        db.write(self.UserId.lower() + ', ' + self.Password + '\n')
        db.close()
        print('User Created Successfully')

    def Login(self):
        self.GetUserId()
 
 
a=ProjectLogin()
a.Purpose()
