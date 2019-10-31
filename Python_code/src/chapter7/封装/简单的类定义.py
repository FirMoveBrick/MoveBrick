class fruit:
    name = 'apple'
    price = 6.5
    def printName(self):
        print(self.name)
        print(self.price)
if __name__ == '__main__':
    print('fruit.name={0},fruit.price={1}'.format(fruit.name,fruit.price))
    myFruit = fruit()
    # myFruit.printName()
    print('myfruit.name={0},myfruit.price={1}'.format(myFruit.name,myFruit.price))
    myFruit.name = 'orange'
    myFruit.price = 11.1
    print('myfruit.name={0},myfruit.price={1}'.format(myFruit.name, myFruit.price))
    # 不能通过类名，方法名来访问方法！！！！1
    # fruit.printName()