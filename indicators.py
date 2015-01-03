# Marcel Champagne, 52532335, Lab Sect. 6 Assignment 3.

class SimpleMovingAverage:
    
    def __init__(self, num_days):
        self._num_days = num_days

    def execute(self, quotes):
        '''Calculates simple moving averages'''
        closing_prices = []
        
        for quote in range(1,len(quotes)):
            closing_prices.append(float(quotes[quote].split(sep=',')[-1]))

        number_of_closing_prices = len(closing_prices)

        average_prices = []
        
        for i in range(1,number_of_closing_prices+1):
            if i < self._num_days:
                average_prices.append(None)
            else:
                total = 0
                for j in range(i-self._num_days,i):
                    total += closing_prices[j]

                average = total/self._num_days
                average_prices.append(average)
                
        return average_prices

class DirectionalIndicator:
    
    def __init__(self, num_days):
        self._num_days = num_days

    def execute(self, quotes):
        '''Calculates directional indicators'''
        closing_prices = []
        
        for quote in range(1,len(quotes)):
            closing_prices.append(float(quotes[quote].split(sep=',')[-1]))

        number_of_closing_prices = len(closing_prices)

        change = []
        
        for i in range(number_of_closing_prices):
            if i == 0:
                change.append(0)
            else:
                if closing_prices[i] > closing_prices[i-1]:
                    change.append(1)
                else:
                    change.append(-1)

        indicators = []

        for i in range(number_of_closing_prices):
            index_start = i-self._num_days+1
            if index_start < 0:
                index_start = 0
                
            index_end = i

            indicator = 0
            
            for j in range(index_start,index_end+1):
                indicator += change[j]
                
            indicators.append(indicator)
            
        return indicators
