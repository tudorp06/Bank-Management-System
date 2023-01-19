import sys

import bankHolder
from bankHolder import Bankholder
import random

class UI:

    def __init__(self, bankh: Bankholder):
        self.bankh = Bankholder("", "", "")

    def exit(self):
        sys.exit("Exiting program...")

    def go_back(self):
        comm = input("Press anything to continue: ")
        self.menu()

    def menu(self):
        print("Welcome to Tudor's bank account management system! Please choose one of the options below:")
        print("1) Register user")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Check balance")
        print("5) Check account details")
        print("6) Show all bank accounts")
        print("0) Exit")

    def register(self):
        num = random.randint(1000,9999)
        name = input("Enter account name: ")
        balance = int(input("Enter starting balance: "))
        bankholder = Bankholder(name, balance, num)
        self.bankh.add_to_list(bankholder)
        print("Successfully added " + name + " to our system!")


    def deposit(self):
        name = input("Enter account name: ")
        ok = 0
        for bankholder in self.bankh.get_acc_list():
            if name == bankholder.get_name():
                ok = 1
                sum = int(input("Enter how much you would like to deposit: "))
                bankholder.add_balance(sum)
                print("Deposit successful! New balance: " + str(bankholder.get_balance()) + "$")

        if ok == 0:
            print(Exception("That account does not exist!"))


    def withdraw(self):
        name = input("Enter account name: ")
        ok = 0
        for bankholder in self.bankh.get_acc_list():
            if name == bankholder.get_name():
                ok = 1
                sum = int(input("Enter how much you would like to withdraw: "))
                if(sum>bankholder.get_balance()):
                    print(Exception("You don't have that much money in your account!"))
                else:
                    bankholder.subtract_balance(sum)
                    print("Withdraw successful! New balance: " + str(bankholder.get_balance()) + "$")
        if ok == 0:
            print(Exception("That account does not exist!"))

    def check_balance(self):
        ok = 0
        name = input("Enter account name: ")
        for bankholder in self.bankh.get_acc_list():
            if name == bankholder.get_name():
                ok = 1
                print("Your balance: " + str(bankholder.get_balance()) )
        if ok == 0:
            print(Exception("That account does not exist!"))

    def show_details(self):
        name = input("Enter account name: ")
        ok = 0
        for bankholder in self.bankh.get_acc_list():
            if name == bankholder.get_name():
                ok = 1
                print(str(bankholder))
        if ok == 0:
            print(Exception("That account does not exist!"))

    def show_all_accounts(self):
        for bankholder in self.bankh.get_acc_list():
            print(str(bankholder))

    def run(self):
        while True:
            self.menu()
            print(">")
            try:
                key =int(input(""))
            except Exception:
                print("Invalid input. Please try again!")

            if key == 1:
                self.register()
            elif key == 2:
                self.deposit()
            elif key == 3:
                self.withdraw()
            elif key == 4:
                self.check_balance()
            elif key == 5:
                self.show_details()
            elif key == 6:
                self.show_all_accounts()
            elif key == 0:
                self.exit()





