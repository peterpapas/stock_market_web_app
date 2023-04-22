import streamlit as st
import pandas as pd
from PIL import Image
import yfinance as yf
from datetime import datetime


# Set Streamlit page configuration
st.set_page_config(
    page_title="Stock Market Web Application",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="./image.jpg"
)

# Custom CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title & Image

st.markdown("""
    <style>
        .title {
            font-weight: bold;
            font-size: 30px;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 16px;
            margin-bottom: 20px;
        }
    </style>
    <div class="title">Stock Market Web Application in Python</div>
    <div class="subtitle">
        This web application provides real-time stock data visualization using Yahoo Finance. Users can enter a stock symbol, along with custom start and end dates, to view historical stock data, including the stock's closing price and trading volume. The application also displays key statistics on the selected stock data, providing insights into the stock's performance over the specified time period.
    </div>
""", unsafe_allow_html=True)

image = Image.open("./image.jpg")
st.image(image, use_column_width=True)

# side bar header
st.sidebar.header('User Input')

# get user input function


def get_input():
    today = datetime.today().strftime("%Y-%m-%d")
    start_date = st.sidebar.text_input("Start Date", "2010-01-10")
    end_date = st.sidebar.text_input("End Date", today)
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

# get company name function


def get_company_name(Symbol):
    if symbol == 'AMZN':
        return 'Amazon '
    elif symbol == 'TSLA':
        return 'Tesla '
    elif symbol == 'GOOG':
        return 'Alphabet '
    else:
        'None'

# get proper company data and proper time frame from user imput 'start' 'end'


def get_data(symbol, start, end):
    # Fetch data from Yahoo Finance
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end)

    # Reset the index to be the date
    df.reset_index(inplace=True)

    return df


# Get users input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
# Get company name
company_name = get_company_name(symbol.upper())

# display close price
st.header(company_name + "Close Price\n")
st.line_chart(df['Close'])

# display Volume
st.header(company_name + "Volume\n")
st.line_chart(df['Volume'])

# get statistics on data
st.header('Data Statistics')
st.write(df.describe())
