class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    def menu(self):
        user_input = input("""
        Hello , how would you like to proceed?
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exit()")
        else:
            print("Wrong Input")

    def create_pin(self):
        self.pin = input("Enter Your Pin")
        print("Pin Set Successfully!")

    def deposit(self):
        temp = input("Enter Your Pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit Successful!")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter Your Pin")
        if temp == self.pin:
            amount = int(input("Enter the amount to withdraw"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successful!")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Pin")


    def check_balance(self):
        temp = input("Enter Your Pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")


sbi = Atm()
# TODO make the code complete tomorrow
