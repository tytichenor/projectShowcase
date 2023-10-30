import random


#idk
def checkRow(row):
    row_list = row.rstrip().split(",")
    if len(row_list) > 1:
        if row_list[1] == "INFORMATION":
            return "USER"
        elif row_list[1] == "ACCOUNT":
            return "ACCOUNT"
        else:
            print('Database error')
            return False

# sets variables for password info
class User:
    def __init__(self, uname, pwd, fname, lname, account_list=[]):
        self.username = uname
        self.password = pwd
        self.first_name = fname
        self.last_name = lname
        self.account_list = account_list
    
    def add_account(self, account_object):
        self.account_list.append(account_object)

   


class Database:
    def __init__(self):
        self.update_database()

    #updates text file
    def update_database(self):
        with open("database.txt" , "r") as file:
            self.db = file.readlines()

    #writes to text file 
    def write_database(self):
        with open("database.txt" , "w") as file:
            file.writelines(self.db)
    
    #breaks down the text file to remove any commas or spaces
    def get_user_creds(self, row):
        row_list = row.rstrip().split(",")
        uname = row_list[0]
        pwd = row_list[2]

        #getting username and password from row list
        return uname, pwd


    def check_user(self, uname, pwd):
        #checks if password matches previous account user
        for line in self.db:
            if checkRow(line) == "USER":
                check_uname, check_pwd = self.get_user_creds(line)
                if uname == check_uname and pwd == check_pwd:
                    line_list = line.rstrip().split(",")
                    return User(line_list[0], line_list[2], line_list[3], line_list[4])
        
        return -1


    def add_row(self, text):
        with open("database.txt", "a") as file:
            file.write(text)
        return
    
    def add_user(self, uname, pwd, fname, lname):
        #text is assigned to every item in the row 
        self.add_row(text=uname+",INFORMATION,"+pwd+","+fname+","+lname+"\n")
        self.update_database()

    def add_account(self,uname,name,accountuname,pwd,category):
        self.add_row(f"{uname},ACCOUNT,{name},{accountuname},{pwd},{category}\n")
        self.update_database()


    # checks if category matches username, then prints account info 
    def viewaccounts(self,uname,category):
        for line in self.db:
            if checkRow(line) == "ACCOUNT":
                line_list = line.rstrip().split(",")
                if line_list[-1] == category and line_list[0] == uname:
                    print(f'Account name: {line_list[2]}')
                    print(f'User name: {line_list[3]}')
                    print(f'Password: {line_list[4]}\n')


    def edit_account(self,uname,name,accountuname,pwd,category):
        for i in range(len(self.db)):
            if checkRow(self.db[i]) == "ACCOUNT":
                line_list = self.db[i].rstrip().split(",")
                if line_list[2] == name and line_list[0] == uname:
                    self.db[i] = f"{uname},ACCOUNT,{name},{accountuname},{pwd},{category}\n"
                    self.write_database()
                    break
    
    #removes and writes accordinly 
    def remove_account(self,uname,name):
        for i in range(len(self.db)):
            if checkRow(self.db[i]) == "ACCOUNT":
                line_list = self.db[i].rstrip().split(",")
                if line_list[2] == name and line_list[0] == uname:
                    self.db.remove(self.db[i])
                    self.write_database()
                    break
                
#from previous assignment       
class password:
    @staticmethod
    def makepassword():
        capitalLetters = 1
        lowercaseLetters = 1
        numbers = 1
        specialCharacters = 1
        password =[]
        finalpass=""
        for i in range(capitalLetters):
            password.append(random.randint(65, 90))
        for i in range(lowercaseLetters):
            password.append(random.randint(97, 122))
        for i in range(numbers):
            password.append(random.randint(48, 57))
        special=[33,64,35,36,37,94,38,42,40,41]
        for i in range(specialCharacters):
            password.append(random.choice(special))
        decrypted = [chr(x) for x in password]
        randomized=random.shuffle(decrypted)

        for x in decrypted:
            finalpass += x
        
        return finalpass