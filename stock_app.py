import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.title('Stock Trend Prediction')

# Input for stock ticker symbol
stock_symbol = st.text_input('Enter Stock Ticker', 'AAPL')

# Historical data parameters
start = '2010-01-01'
current_date = datetime.now().strftime('%Y-%m-%d')  # Get current date

# Fetching historical data
df = yf.download(stock_symbol, start=start, end=current_date)

# Calculating moving averages
df['MA100'] = df['Close'].rolling(window=100).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

# Displaying historical data and moving averages
st.subheader('Historical Stock Data')
st.write(df.tail())  # Display the last few rows of the fetched data

# Plotting stock price and moving averages
st.subheader('Stock Price and Moving Averages')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df['Close'], label='Close Price')
ax.plot(df.index, df['MA100'], 'r', label='100-day MA')
ax.plot(df.index, df['MA200'], 'g', label='200-day MA')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
st.pyplot(fig)

# Fetching real-time data
stock_data = yf.Ticker(stock_symbol)
current_price = stock_data.history(period='1d')['Close'].iloc[-1]

# Displaying current price
st.subheader('Real-Time Stock Price')
st.write(f"Current Price for {stock_symbol}: {current_price}")



# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import matplotlib.pyplot as plt  # Importing matplotlib for plotting
# from datetime import datetime

# st.title('Real-Time Stock Price')

# # Input for stock ticker symbol
# stock_symbol = st.text_input('Enter Stock Ticker', 'TATAMOTORS.NS')

# # Fetching real-time data
# current_date = datetime.now().strftime('%Y-%m-%d')  # Get current date
# stock_data = yf.download(stock_symbol, start='2010-01-01', end=current_date)

# # Calculating moving averages
# stock_data['MA100'] = stock_data['Close'].rolling(window=100).mean()
# stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

# # Displaying real-time data and moving averages
# st.subheader('Real-Time Stock Data')
# st.write(stock_data.tail())  # Display the last few rows of the fetched data

# # Plotting stock price and moving averages
# st.subheader('Stock Price and Moving Averages')
# fig, ax = plt.subplots(figsize=(10, 6))
# ax.plot(stock_data.index, stock_data['Close'], label='Stock Price')
# ax.plot(stock_data.index, stock_data['MA100'], label='100-day MA', color='red')  # Red line for 100-day MA
# ax.plot(stock_data.index, stock_data['MA200'], label='200-day MA', color='green')  # Green line for 200-day MA
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# ax.legend()
# st.pyplot(fig)

