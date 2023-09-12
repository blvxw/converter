class Currency():
    def __init__(self, name, exchange_rate):
        self.name = name
        self.exchange_rate = exchange_rate
    
    def __str__(self):
        return f"{self.name}: {self.exchange_rate}"
    
    def transfer(self,second_currency, amount):
        return amount * self.exchange_rate / second_currency.exchange_rate