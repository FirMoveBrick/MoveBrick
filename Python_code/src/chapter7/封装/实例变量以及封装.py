class hello:
    def setname(self,yourName):
        self.name = yourName
    def print(self):
        print('hello',self.name)


h = hello()
h.setname('User')
h.print()
