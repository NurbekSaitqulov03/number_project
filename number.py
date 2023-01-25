import math

class Number:
    def __init__(self,num):
        self.number = num
    def data_type(self):
        """check if the number is data type"""
        return type(self.number)
    def len(self):
        """check if the number is len"""
        x = self.number
        if type(x)==int:
            return len(str(x))
        elif type(x)==float:
            return len(str(x))-1
    def is_positive(self):
        """check if the number is positive"""
        return self.number>0
    def is_negative(self):
        """check if the number is negative"""
        return self.number<0
    def zero(self):
        """check is the number is zero"""
        return self.number==0
    def even(self):
        """check is the number is even"""
        return self.number%2==0
    def odd(self):
        """check is the number is odd"""
        return self.number%2==1
    def prime(self):
        """check is the number is prime"""
        x = self.number
        a = x//2
        m = 0
        for i in range(a+1)[2:]:
            if x%i==0:
                m = False
            if x%i==1:
                m = True
            return m
z = Number(23)
print(z.len())