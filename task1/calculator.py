class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def multy(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b==0:
            raise ValueError("Error! can not divide by Zero!")
        return a / b
    