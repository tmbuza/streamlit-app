import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Homepage"
        ]
    )

    if page == "Homepage":
        homepage()

def homepage():
    st.write("""
        # Simple Stock Price App
        ### Shown are the stock **closing price** and **volume** of _**Tesla !**_ ###
        #""")
    
    tickerSymbol = 'TSLA'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-31')

    st.line_chart(tickerDf.Close)

if __name__ == "__main__":
    main()
