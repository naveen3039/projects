from exceptionn import *
class Operations:
     
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    
    def add(self,a,b):
        try:
            if self.a>9 or self.b>9:          
                raise AddError(self.a,self.b)
            return (self.a)+(self.b)
        except AddError as adde:
            return str(adde)


    def sub(self,a,b):
        if (self.a - self.b)<0:
            raise SubError(self.a,self.b) 
        return self.a - self.b 

    def mul(self,a,b):
        if self.a>9 or self.b>9:
            raise MulError(self.a,self.b)
        return (self.a)*(self.b)

    def div(self,a,b):
        if self.a==0 or self.b==0:
            raise DivError(self.a,self.b)
        elif self.a > self.b :
            return self.a/self.b
        else:
            return self.b/self.a
        
