# Marcel Champagne, 52532335, Lab Sect. 6 Assignment 3.

import datetime
import download
import indicators
import signals

def get_ticker_symbol() -> str:
    '''Returns a ticker symbol.'''
    
    symbol = input("Please enter a ticker symbol for a stock: ")
    
    return symbol.upper()


def before_date(date: str, original_date: str) -> bool or None:
    '''Checks if a date is before another date.'''
    date = date.split(sep='-')
    date = datetime.date(int(date[0]),int(date[1]),int(date[2]))

    original_date = original_date.split(sep='-')
    original_date = datetime.date(int(original_date[0]),int(original_date[1]),int(original_date[2]))

    if date < original_date:
        return True
    elif date == original_date:
        return None
    else:
        return False
    

def get_date() -> str:
    '''Returns a date in format YYYY-MM-DD.'''
    while True:
        date = input("Please enter in format YYYY-MM-DD: ")
        possible_date = date.split(sep="-")
        try:
            # Check date for length format
            date_len = len(possible_date)
            year_len = len(possible_date[0])
            month_len = len(possible_date[1])
            day_len = len(possible_date[2])

            # Check date for correct numbers
            datetime.date(int(possible_date[0]),int(possible_date[1]),int(possible_date[2]))
            
            if year_len == 4 and month_len == 2 and day_len == 2 and date_len == 3:
                break
            else:
                print("Invalid date, please enter another.")
        except:
            print("Invalid date, please enter another.")
        
    print()    
    return date

def format_url(symbol: str, start_month: str, start_day: str, start_year: str, end_month: str, end_day: str, end_year: str) -> str:
    '''Returns a yahoo url based on the parameters'''
    
    start_month = int(start_month)-1
    end_month = int(end_month)-1
    
    url = "http://ichart.yahoo.com/table.csv?s="+symbol+"&a="+str(start_month)+"&b="+start_day+"&c="+start_year+"&d="+str(end_month)+"&e="+end_day+"&f="+end_year+"&g=d"

    return url


def analysis(quotes: [str], symbol: str) -> None:
    '''Runs analyis part of the user interface.'''
    num_quotes = len(quotes)-1
    menu = '''Choose one of the options for analysis:
1. Simple moving average
2. Directional indicator'''
    while True:
        print(menu)
        print("You are analysing "+str(num_quotes)+" days worth of quotes.")
        strategy = input("Please select an analysis option: ")

        if strategy == '1':
            number = input("How many days would you like to consider? ")
            try:
                n_day = int(number)
            except:
                print("Invalid number.")
            else:
                if n_day > 0 and n_day < num_quotes:
                    simple_analysis(quotes, n_day, symbol)
                    break
                else:
                    print("The number must be greater than 0 and less than the number of quotes.")

        elif strategy == '2':
            number = input("How many days would you like to consider? ")
            try:
                n_day = int(number)
            except:
                print("Invalid number.")
            else:
                if n_day > 0 and n_day < num_quotes:
                    directional_analysis(quotes, n_day, symbol)
                    break
                else:
                    print("The number must be greater than 0 and less than the number of quotes.")
        else:    
            print("Invalid choice, please try again.")
        print()


def simple_analysis(quotes: [str], num_days: int, symbol: str) -> [str]:
    '''Analyzes the quotes and utlizes the classes with simple moving average.'''
    simple_moving_average = indicators.SimpleMovingAverage(num_days)
    indicator = simple_moving_average.execute(quotes)

    simple_moving_average_signal = signals.SimpleMovingAverageSignal(indicator)
    signals_list = simple_moving_average_signal.execute(quotes)

    strategy = "Simple moving average ("+str(num_days)+"-day)"
    final_report(signals_list,quotes,symbol,indicator,strategy)


def directional_analysis(quotes: [str], num_days: int, symbol: str) -> [str]:
    '''Analyzes the quotes and utilizes the classes with directional indicators.'''
    directional_indicator = indicators.DirectionalIndicator(num_days)
    indicator = directional_indicator.execute(quotes)
    
    while True:
        buy = input("What would you like the buy threshold to be? ")
        try:
            buy = int(buy)
            break
        except:
            print("Invalid number.")
    while True:
        sell = input("What would you like the sell threshold to be? ")
        try:
            sell = int(sell)
            break
        except:
            print("Invalid number.")
            
    directional_indicator_signal = signals.DirectionalIndicatorSignal(indicator,buy,sell)
    signals_list = directional_indicator_signal.execute(quotes)

    buy,sell = directional_indicator_signal.get_buy_sell()

    strategy  = "Directional ("+str(num_days)+"-day), buy above +"+str(buy)+", sell below "+str(sell)
    final_report(signals_list,quotes,symbol,indicator,strategy)

def final_report(final_signals: [str], quotes: [str], symbol: str, final_indicators: [str],strategy: str) -> None:
    '''Prints the final report.'''
    del quotes[0]
    print()
    print("Symbol: "+symbol)
    print("Strategy: "+strategy)
    print()
    heading = "{:12}{:12}{:12}{:12}"
    print(heading.format("DATE","CLOSE","INDICATOR","SIGNAL"))
    index = 0
    formatting = "{:12}{:12}{:12}{:12}"
    for element in final_signals:
        quote_info = quotes[index].split(sep=',')
        if element == None:
            element = ' '
        try:
            if type(final_indicators[index]) != int:
                indicator_element = str(round(float(final_indicators[index]),2))
            else:
                indicator_element = str(final_indicators[index])
            print(formatting.format(quote_info[0],quote_info[1],indicator_element,element))
        except:
            print(heading.format(quote_info[0],quote_info[1],' ',element))
        index += 1
               

def main() -> None:
    '''Runs the main user interface.'''
    ticker = get_ticker_symbol()
    
    while True:
        print("Enter a starting date,")
        start_date = get_date()
        if before_date(start_date, str(datetime.date.today())) == True:
            break
        else:
            print("The start date must be before the current date.")
        
    while True:
        print("Enter a ending date,")
        end_date = get_date()
        if before_date(end_date, str(datetime.date.today())) != False and before_date(start_date,end_date) == True:
            break
        else:
            print("The end date must not be after the current date and must be before the start date.")

    start_date = start_date.split(sep='-')
    end_date = end_date.split(sep='-')

    start_year = start_date[0]
    start_month = start_date[1]
    start_day = start_date[2]

    end_year = end_date[0]
    end_month = end_date[1]
    end_day = end_date[2]

    try:
        url = format_url(ticker,start_month,start_day,start_year,end_month,end_day,end_year)
        content = download.return_url_content(url)
    except:
        print("There was a problem accessing stock qoutes from those dates, the program will now exit.")
    else:
        analysis(content,ticker)

if __name__ == "__main__":
    main()
