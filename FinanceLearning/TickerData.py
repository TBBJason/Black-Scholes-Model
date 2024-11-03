import yfinance as yf

class ticker_data:
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.information = yf.Ticker(self.ticker)
    def current_close(self):
        current = self.information.history(period='1y')['Close']
        return current
    def columns(self):
        columns = self.information.columns
        return columns




if __name__ == "__main__":
    aapl = ticker_data('aapl')
    columns = aapl.columns
    current = aapl.current_close()
    print(current, columns)