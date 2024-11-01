import yfinance as yf

class ticker_data:
    def __init__(self, ticker):
        self.ticker = ticker.upper()

        self.information = self.information = yf.Ticker(self.ticker)
    def current_close(self):
        current = self.information.history(period='1d')['Close'][0]
        return current
    def columns(self):
        return 



if __name__ == "__main__":
    aapl = ticker_data('aapl')
    current = aapl.current_close()
    print(current)