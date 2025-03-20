import json

class WeightsService:
    def __init__(self, ticker):
        self.ticker = ticker

    def get_weights(self) -> list[float]:
        
        with open('./api/data/weights.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        for stock in data:
            if stock['ticker'].lower() == self.ticker.lower():
                return stock['weights']
                    
        raise ValueError(f"Não foi possível encontrar os pesos para o ticker {self.ticker}")