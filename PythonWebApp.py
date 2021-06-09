import streamlit as st
import pandas as pd
from PIL import Image

#Title & Image
st.header("""
Stock Market Web Application in **Python** 
Visual stock Data charts, Dates Jan 1, 2020 - Aug 10, 2020
""")

image = Image.open("./image.jpg")
st.image(image, use_column_width=True)

#side bar header
st.sidebar.header('User Input')

#get user input function
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-03-15")
    end_date = st.sidebar.text_input("End Date", "2020-08-05")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

#get company name function
def get_company_name(Symbol):
    if symbol == 'AMZN':
        return 'Amazon '
    elif symbol == 'TSLA':
        return 'Tesla '
    elif symbol == 'GOOG':
        return 'Alphabet '
    else:
        'None'

#get proper company data and proper time frame from user imput 'start' 'end'

def get_data (symbol, start, end):
#load data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("./data/AMZN.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("./data/TSLA.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("./data/GOOG.csv")
    else:
        df = pd.DataFrame(columns = ['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])
#get date range from user input
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
#set start and end index rows to 0
    start_row = 0
    end_row = 0
#Start date top of the data set and go down check if user date is less(for the weeknds stock maket close) then or equal to the date in dataset
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
        #End date bottom of the dataset and go up graiter of equal to date in dataset
            for j in range(0, len(df)):
                if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
                    end_row = [len(df)-1 - j]
                    break
        #set the index to be the date
        df = df.set_index(pd.DatetimeIndex(df['Date'].values))
            
        return df.iloc[start_row:end_row +1, :]

#Get users input
start, end, symbol = get_input()
#Get the data
df = get_data(symbol, start, end)
#Get company name
company_name = get_company_name(symbol.upper())

#display close price
st.header(company_name + "Close Price\n")
st.line_chart(df['Close'])

#display Volume
st.header(company_name + "Volume\n")
st.line_chart(df['Volume'])

#get statistics on data 
st.header('Data Statistics')
st.write(df.describe())