import yfinance as yf
import streamlit as st
import plotly.graph_objects as go

tickerSymbolOption = st.sidebar.selectbox('Symbol', options=('PETR4', 'BBDC3', 'BBDC4', 'ITUB4'), index=0)
graphType = st.sidebar.radio('Graph Type', ('Line', 'Candlestick'))
st.write(f"""
# Stock Price Viewer App :sunglasses:
Shown stock closing price and volume of: **{tickerSymbolOption}** 
""")

tickerData = yf.Ticker(tickerSymbolOption + '.SA')
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits
if graphType == 'Line':
    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)
else:
    fig = go.Figure(data=[go.Candlestick(x=tickerDf.index,
                    open=tickerDf.Open,
                    high=tickerDf.High,
                    low=tickerDf.Low,
                    close=tickerDf.Close)])
    st.plotly_chart(fig)