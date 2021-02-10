import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto = input("Enter the crpyto you want to check: ")
currency = input("Enter the currency: ")

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

data= web.DataReader(f"{crypto}-{currency}", "yahoo")

plt.figure(figsize=(8,6))
plt.title(f"{crypto} Coin Price Visualizer")
plt.xlabel("Year")
plt.ylabel(f"Price in {currency}")
plt.plot(data['Close'],color='green')
plt.legend(loc="upper left")
plt.show()

# mpf.title(f"{crypto} Price Visualizer")
# mpf.plot(data,type="candle",style="yahoo",volume=True)