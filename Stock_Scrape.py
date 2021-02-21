import yfinance as yf

try:
    def analysis(ticker):

        stock=ticker
        bucket=yf.Ticker(stock)
        print(bucket.info['shortName'])
        periods=['5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']

        def current_price(Ticker):
                stock=Ticker.history(period = "1d" , interval = "1m")
                Close=stock['Close']
                latest_time=Close.index[len(Close.index)-1]
                return Close.loc[latest_time]
            


        def moving_average(stock, periods):
            stock=stock
            periods=periods
            def history_means(Ticker, time):
                stock=Ticker.history(period=time)
                Close=stock['Close']
                return Close.mean()//1
            dict={}
            for time in periods:
                mean=history_means(stock,time)
                dict.update({
                    "Moving Average of " + time : mean} )
                #print("Moving Average of "+time+" = "+str(mean)) 
            return dict

        current_price=current_price(bucket)

        #recieving a dict with 1d 5d 1mo etc moving average
        data=moving_average(bucket, periods)


        data.update({"Current Price":current_price})

        technicalAnalysis=sorted(data.items(), key=lambda x: x[1], reverse=True)
        for key in technicalAnalysis:
            print(key[0], key[1])

except:
    print("No Stock entered, or not run properly")