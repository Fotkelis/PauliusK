 
class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number
        
    def add(self, number) -> float:
        return self.number + number
    
    def sub(self) -> float:
        ...
    def div(self) -> float:
        ...
    def mul(self, sk) -> float:
        return self.number * sk
    def calculate(self) -> float:
        ...
 
 
