class AddError(Exception):

    def __init__(self,a,b):
        self.a=a
        self.b=b
        print (f'{self.a} is more than 9 or {self.b} is more than 9')

class MulError(Exception):
   
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(f'{self.a} is more than 9 or {self.b} is more than 9')
    
class SubError(Exception):
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(f'it is subtraction Error Because it gives vlaue in negative')
    
class DivError(Exception):
   
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('it is zero division is not posssible')


