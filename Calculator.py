class Calculator:
    def __init__(self,Number1,Number2):
        self.Number1=Number1
        self.Number2=Number2

    def addition(self):
        sum=self.Number1 + self.Number2
        print('Sum :',sum)

    def subtract(self):
        sub=self.Number1 - self.Number2
        print("Subtract :",sub)

    def multiplication(self):
        mul=self.Number1 * self.Number2
        print("Multiplication :",mul)

    def division(self):
        div=self.Number1 / self.Number2
        print("Division :",div)

class UseCalculator:
    num1=int(input('Enter First Number :'))
    num2=int(input('Enter Second Number :'))
    obj=Calculator(num1,num2)
    obj.addition()
    obj.subtract()
    obj.division()
    obj.multiplication()


a=UseCalculator()