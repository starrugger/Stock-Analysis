# Stock-Analysis
A orchestrator that takes an input of a Stock Ticker (TSLA, AAPL, BA etc) and return my desired statistics:
Flow would be :
Enter a Stock Ticker _________


Under the hood, I used the yFnance api, provided by https://github.com/ranaroussi/yfinance, to derive the technial stats I was looking for:

***So make sure you "pip install yfinance"***

One you run "python orchestrator.py", you will be asked to
 "enter a stock ticker:"

 
The orchestrator will keep going until you enter "quit" or until you perform a keyboard interrupt with "Ctrl+C"

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
 


