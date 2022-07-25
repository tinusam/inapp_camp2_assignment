from abc import ABC, abstractmethod

class calculator(ABC):
    def __init__(self):
        self.__num1 = None
        self.__num2 = None 
    
    @property
    def num1(self):
        return self.__num1
    @num1.setter
    def num1(self, number):
         self.__num1 = number
    
    @property
    def num2(self):
        return self.__num2
    @num2.setter
    def num2(self, number):
        self.__num2 = number
    
    @abstractmethod
    def calculate(self):
        pass

class CalcSum(calculator):
    def calculate(self):
        return self.num1 + self.num2

class CalcDiff(calculator):
    def calculate(self):
        return self.num1 - self.num2

class CalcProd(calculator):
    def calculate(self):
        return self.num1 * self.num2

class CalcQuo(calculator):
    def calculate(self):
        return self.num2 // self.num1


option = 0
while option != 5:
    print("Calculator:\n 1.Add\n 2.Subtract\n 3.Product\n 4.Division\n 5.Exit")
    option = int(input("enter your option: "))
    if option == 1:
        sum = CalcSum()
        sum.num1 = int(input("Enter first number:"))
        sum.num2 = int(input("Enter second number:"))
        print(sum.calculate())

    elif option == 2:
        sub = CalcDiff()
        sub.num1 = int(input("Enter a number:"))
        sub.num2 = int(input("Enter a number:"))
        print(sub.calculate())

    elif option == 3:
        prod = CalcProd()
        prod.num1 = int(input("Enter a number:"))
        prod.num2 = int(input("Enter a number:"))
        print(prod.calculate())

    elif option == 4:
        quo = CalcQuo()
        quo.num1 = int(input("Enter a number:"))
        quo.num2 = int(input("Enter a number:"))
        print(quo.calculate())

    elif option == 5:
        pass
        
    else:
        print("wrong option")