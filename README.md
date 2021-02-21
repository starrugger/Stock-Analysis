# Stock-Analysis
A orchestrator who takes an input of a Stock Ticker (TSLA, AAPL, BA etc) and return my desired statistics

I used the yFnance api, provided by https://github.com/ranaroussi/yfinance, to provide technical analyis:

***So make sure you "pip install yfinance"

(TECHNICAL ANALYSIS categories as of 02/21/2021
Current Price 
Moving Average of 5d 
Moving Average of 1mo 
Moving Average of ytd 
Moving Average of 3mo 
Moving Average of 6mo 
Moving Average of 1y 
Moving Average of 2y 
Moving Average of 5y 
Moving Average of 10y 
Moving Average of max 
  )
 
One you run "python orchestrator.py", you will be asked to "enter a stock ticker:"

The orchastrator will keep going till, you enter "quit" or untill you keyboard interrupt with "Ctrl+C"


## STILL NEED TO ADD AND ADOPT THE StockScrape TO SCENARIOS WHERE WRONG INPUTS SUCH AS #'S OR STOCK TICKER'S ARE NOT ENTERED ##
SOOO PLEASE DON'T ENTER INPUTS THAT ARE NOT STOCK TICKERS:
if you do, just re-run program


