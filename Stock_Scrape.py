import yfinance as yf

def analysis(ticker):
    stock=ticker

#under the cover this is creating a request to the yfinance server
    bucket=yf.Ticker(stock)

#This is how i make sure that only Stock tickers are put in
    try:
        print(bucket.info['shortName'])
    except:
        return("Not a token")
#array of allowed periods within 
#the Ticker.history(period=ARGUMENT) section 
#'1d' also available
    
    periods=['5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']

#calling the current price
#i can move this into the moving_average function to the 1d interval
#using an if statement
    def current_price(Ticker):
            stock=Ticker.history(period = "1d" , interval = "1m")
            Close=stock['Close']
            latest_time=Close.index[len(Close.index)-1]
            return Close.loc[latest_time]

#getting the moving average by calling all closing values
#for N= days
#from today to the past N days
#days available currently '5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'
    def moving_average(stock, periods):
        stock=stock
        periods=periods
#defining a function that gets the ticker for a stock
#isolates the Closing column
#and finding the mean [using Pandas Dataframe calls]
        def history_means(Ticker, time):
            stock=Ticker.history(period=time)
            Close=stock['Close']
            return Close.mean()//1
        dict={}
#appending to a dict for constant look up time
        for time in periods:
            mean=history_means(stock,time)
            dict.update({
                "Moving Average of " + time : mean} )
#print("Moving Average of "+time+" = "+str(mean)) 

#returning a dict for data transfer
        return dict

    current_price=current_price(bucket)

    #recieving a dict with 1d 5d 1mo etc moving average
    data=moving_average(bucket, periods)


    data.update({"Current Price":current_price})

#a reverse sort..Highest value > Lowest value
    technicalAnalysis=sorted(data.items(), key=lambda x: x[1], reverse=True)
    for key in technicalAnalysis:
        print(key[0], key[1])

