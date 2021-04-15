import yfinance as yf
import streamlit as st 
import pandas as pd

st.write("""
# Simple Stock Price Display App

Shown here are the stock price and volume for the Chinese conglomerate Tencent.

"""
)

tickerSymbol = 'TCEHY'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='Id', start='2015-05-06', end='2021-01-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)