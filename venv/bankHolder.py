
class Bankholder:
    def __init__(self,name,balance, ID):
        self._name = name
        self._balance = balance
        self._ID = ID
        self._list_of_accs = []


    def set_balance(self,new_balance):
        self._balance = new_balance

    def add_balance(self,balance):
        self._balance += balance

    def subtract_balance(self, balance):
        self._balance -= balance

    def get_balance(self):
        return self._balance

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name

    def get_ID(self):
        return self._ID

    def get_acc_list(self):
        return self._list_of_accs

    def add_to_list(self, bankholder):
        self.get_acc_list().append(bankholder)

    def __repr__(self):
        return str(self)
    def __str__(self):
        return "Account name: " + self.get_name() + "\n ID: " + str(self.get_ID()) + "\n Balance: " + str(self.get_balance() + "$")
