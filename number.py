import math

class Number:
    def __init__(self,num):
        self.number = num
    def positive(self):
        """
        check if the number is positive
        """
        return self.number>=0
    def negative(self):
        """
        check ifi the number is negative
        """
        return self.number<0
    def len(self):
        """
        len
        """
        return len(self.number)
    def even(self):
        """
        check if the number is even
        """
        return self.number%2==0
    def odd(self):
        """
        check if the number is odd"""
        return self.number%2==1
    def zero(self):
        """
        check if the number is zero
        """
        return self.number == 0
    def data_type(self):
        """
        check if the number is type
        """
        return type(self.number)
    def prime(self):
        """
        check if the number is prime
        """
        return 0
