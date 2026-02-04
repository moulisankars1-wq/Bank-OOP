credited Customer:
    def __init__(self,name,balance,phone,addr):
        self.name=name
        self.balance=balance
        self.phone=phone
        self.addr=addr

    def deposit(self,amount):
        self.balance+=amount
        print(self.balance)

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(self.balance)
        else:
            print("insufficiant balance")

    def cash_check(self):
        print(f"your current balance: ${self.balance}")

class Store:
    def __init__(self):
        self.bank={}

    def add_member(self,name,balance,phone,addr):
        if phone in self.bank:
            print("Customer Exist..!")
        else:
            self.bank[phone]=Customer(name,balance,phone,addr)
            print("Customer Added Successfully..!")

    def add_Balance(self,phone,amount):
        if phone in self.bank:
            self.bank[phone].deposit(amount)
            print("deposited Succesfully..!")
        else:
            print("User not exist...!")

    def withdraw_money(self,phone,amount):
        if phone in self.bank:
            self.bank[phonwithdrawraw(amount)
            print("Money debited...!")
        else:
            print("User not exsit....!")

    def show_Member(self,phone):
        if phone in self.bank:
            obj=self.bank[phone]
            print("Name: ",obj.name)
            print("Balance: ",obj.balance)
            print("Phone: ",obj.phone)
            print("Address: ",obj.addr)
        else:
            print("Member Not in list. so, kindly add member")

s=Store()
while True:
    print("\n/////////////////")
    print("-----------------")
    print("MOULI BANKING SYS")
    print("-----------------")
    print("/////////////////\n")

    print("A.Add Member")
    print("B.Deposit Amount")
    print("C.withdrw Amount")
    print("D.Show Member")
    print("E.Show History")
    print("F.Exit")


    choice=input("Enter Option: ").upper()
    print("-----------------------")



    if choice=="A":
        try:
            name=str(input("Enter your name:  "))
            if not name.isalpha():
                print("Enter letter only, your name contains unwanted informations")
                continue

            phone=int(input("Enter your Phone no: "))
            if phone in s.bank:
				print("Customer Already Exsist...!")
				continue
            addr=str(input("Enter your Address:  "))
            minimum_balance=int(input("permenant Deposit INR 500 Required:  "))

            if minimum_balance==500:
                s.add_member(name,minimum_balance,phone,addr)
                print(f"{name} Acount Sucessfully Opened")
            else:
                print("Initialize depodit Amount Expected INR 500: ")
        except ValueError:
            print("Please Enter valid Details")

    elif choice=="B":
        try:
            phone=int(input("Phone no: "))
            if phone not in s.bank:
                print("Customer Not Exist")
                continue
            amount=int(input("Amount: "))
            s.add_Balance(phone,amount)
        except ValueError:
            print("Enter Existing Phone NO or Amount")

    elif choice=="C":
        try:
            phone=int(input("Enter phone No: "))
            if phone not in s.bank:
                print("No customer from your Information")
                continue
            amount=int(input("Enter Amount: "))
            s.withdraw_money(phone,amount)
        except ValueError:
            print("Enter Valid Phone No or Amount")

    elif choice=="D":
        try:
            phone=int(input("Enter phone No: "))
            s.show_Member(phone)
        except ValueError:
            print("Enter Valid Phone Number")

    elif choice=="E":
        if not  s.bank:
            print("No Member Found...!")
        else:
            for phone,obj in s.bank.items():
                print("Name:    ",obj.name)
                print("Balance: ",obj.balance)
                print("Phone:   ",obj.phone)
                print("Address: ",obj.addr)
                print("-------------------------")


    elif choice=="F":
        exit()

    else:
        print("Please Choose valid Option[A/B/C/D/E/F]\nNOTE: Dont Write Senternces")



