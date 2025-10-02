class MyStr:
    def getString(self):
        self.text = input("Введите строку: ")

    def printString(self):
        print(self.text.upper())

s = MyStr()
s.getString()
s.printString()