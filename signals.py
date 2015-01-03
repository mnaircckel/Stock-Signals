# Marcel Champagne, 52532335, Lab Sect. 6 Assignment 3.

class SimpleMovingAverageSignal:
    
    def __init__(self, indicator):
        self._indicator = indicator

    def execute(self, quotes,):
        '''Calculates buy and sell signals'''
        closing_prices = []
        
        for quote in range(1,len(quotes)):
            closing_prices.append(float(quotes[quote].split(sep=',')[-1]))
            
        signals = []

        for i in range(len(self._indicator)):
            if i == 0:
                signals.append(None)
            else:
                try:
                    if closing_prices[i] > self._indicator[i] and closing_prices[i-1] < self._indicator[i-1]:
                        signals.append("Buy")
                    elif closing_prices[i] < self._indicator[i] and closing_prices[i-1] > self._indicator[i-1]:
                        signals.append("Sell")
                    else:
                        signals.append(None)
                except:
                    signals.append(None)

        return signals
        


class DirectionalIndicatorSignal:
    
    def __init__(self, indicator, buy, sell):
        self._indicator = indicator
        self._buy = buy
        self._sell = sell

    def execute(self, quotes):
        '''Generate buy and sell signals'''
            
        signals = []

        for i in range(len(self._indicator)):
            if i == 0:
                signals.append(None)
            else:
                try:
                    
                    if self._buy < self._indicator[i] and self._buy >= self._indicator[i-1]:
                        signals.append("Buy")
                    elif self._sell > self._indicator[i] and self._sell <= self._indicator[i-1]:
                        signals.append("Sell")
                    else:
                        signals.append(None)
                except:
                    signals.append(None)

        return signals

    def get_buy_sell(self) -> int and int:
        
        return self._buy,self._sell
