class ToLowerString():
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
str = ToLowerString()
str.getString()
str.printString()