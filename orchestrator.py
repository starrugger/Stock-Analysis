import Stock_Scrape
from Stock_Scrape import analysis

print("OnGoing Analysis")

data=input(" Enter stock Ticker  " )
i=0
while(data != "quit"):
    analysis(data)
    print("")
    data=input(" Enter stock Ticker  " )
