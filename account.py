class account:
    numCreated = 0
    Actions = 0
    def __init__(self, initial):
        self._balance = initial
        account.numCreated += 1
    def __Actions(self):
        self.Actions += 1
        if(self.Actions == 3):
            self._balance -= 7
            self.Actions = 0

    def deposit(self, amt):
        self._balance = self._balance + amt
        self.__Actions()

    def withdraw(self, amt):
        self._balance = self._balance - amt
        self.__Actions()
    def getbalance(self):
        self.__Actions()
        return self._balance