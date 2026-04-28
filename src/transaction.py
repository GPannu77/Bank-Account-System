from datetime import datetime


class Transaction:
    
    def __init__(self, t_type, amount, description):
        self.t_type = t_type
        self.amount = amount
        self.description = description
        self.date = datetime.now()
    
    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.type}: ${self.amount:.2f} - {self.description}"