import datetime as dt
import os


class bank:
    def __init__(self,username,password,intial_balance=1000.00):
        self.username=username
        self.password=password
        self.balance=intial_balance

        if os.path.exists(f"{self.username}_transaction"):
            with open(f"{self.username}_transaction","r") as f:
                lines=f.readlines()
                if lines:
                    last_line=lines[-1].strip().split("|")
                    self.balance=float(last_line[-1].split("Rs.")[1])
        

    def record_transactions(self,transaction):
        date=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S")
        data=open(f"{self.username}_transaction","a")
        data.write(f"{date}-{transaction}\n")
   
          

    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount Deposited Successfully-Rs.{amount}")
        self.record_transactions(f"Amount Deposited Rs.{amount} | Current balance Rs.{self.balance}")

        check=input("Do you want see your balance(Yes or No):")
        if check=="yes" or check=="Yes" or check=="YES":
            print(f"Current balance:Rs.{self.balance}\n")
        elif check=="no" or check=="No" or check=="NO":
            print(f"Thank You!\n")
        else:
            print("Invalid\n")


    def withdraw(self,amount):
        if self.balance<=0:
            print("Insifficent balance....\n")
        else:
            if self.balance<amount:
                print("Insifficent balance....\n")
            else:
                self.balance-=amount
                print(f"Rs.{amount} withdraw")
                self.record_transactions(f"Amount Withdrawl Rs.{amount} | Current balance Rs.{self.balance}")

                check=input("Do you want see your balance(Yes or No):")
                if check=="yes" or check=="Yes" or check=="YES":
                    print(f"Current balance:Rs.{self.balance}\n")
                elif check=="no" or check=="No" or check=="NO":
                    print(f"Thank You!\n")
                else:
                    print("Invalid\n")

    def save_records(self):
        file=open("customer_details","a")
        file.write(f"{self.username},{self.password}\n")

    def get_records(self):
        file=open(f"{self.username}_transaction","r")
        print(file.read())




print("Welcome to net banking app!\n\t----Mainmenu----")


while True:
    try:
        print("1.Register\n2.Login\n3.Exit")
        signin=int(input("Choose your option(1-3):"))
        if signin==1:
            user=input("Enter your username:").title()
            flag=False

            if os.path.exists("customer_details"):
                with open("customer_details","r") as file:
                    for line in file:
                        u,p=line.strip().split(",")
                        if user==u:
                            flag=True
                            break
                    
            if flag:
                print("User already exists.Try to login\n")
            else:
                print("Character must be 8 or more and contain at least one digit and one uppercase letter")
                pas=input("Enter your password:")
                digit=False
                word=False
                for i in pas:
                    if i.isdigit():
                        digit=True
                    if i.isupper():
                        word=True

                if digit==True and word==True and len(pas)>=8:
                    print("Strong password")
                    banks=bank(user,pas)
                    banks.save_records()
                    print("Registered Successfully\n")
                elif len(pas)<8:
                    print("Must be minimum 8 characters,Try again!....\n")
                else:
                    print("Invalid Password!,Try again!.....\n")
                
        elif signin==2:
            user=input("Enter your username:")
            pas=input("Enter your password:")

            login_in=False
            if os.path.exists("customer_details"):
                with open("customer_details","r") as file:
                    for line in file:
                        u,p=line.strip().split(",")
                        if user==u and pas==p:
                            login_in=True
                            break
            
            if login_in:
                print("Login Successfully\n")
                net_bank=bank(user,pas)
                while True:
                    print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Transaction History\n5.Logout")
                    try:
                        user=int(input("Enter your choice(1-5):"))
                        if user==1:
                            amount=float(input("Enter the amount:"))
                            net_bank.deposit(amount)
                        elif user==2:
                            amount=float(input("Enter the amount:"))
                            net_bank.withdraw(amount)
                        elif user==3:
                            print(f"Your current balance Rs.{net_bank.balance}\n")
                        elif user==4:
                            net_bank.get_records()
                        elif user==5:
                            print("Logged out Successfully\n")
                            break
                        else:
                            print("Invalid input.Try again!\n")
                    except:
                        print("Invaild Input.Try Again!\n") 
            else:
                print("Invalid username or password.Try again!\n")

        elif signin==3:
            print("Thank you for using net banking")
            break
        else:
            print("Invalid input.Try again!\n")

    except:
        print("Invalid input.Try again!\n")    
    


