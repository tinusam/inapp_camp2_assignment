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
        return self.num2 / self.num1


sum = CalcSum()
sum.num1 = 9
sum.num2 = 8
print(sum.calculate())