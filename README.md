# Stock Market Web Application

This is a Stock Market Web Application built in Python using Streamlit. The application provides real-time stock data visualization using Yahoo Finance. Users can enter a stock symbol, along with custom start and end dates, to view historical stock data, including the stock's closing price and trading volume. The application also displays key statistics on the selected stock data, providing insights into the stock's performance over the specified time period.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.6 or later.
* You have installed the necessary packages (listed below).

## Installing dependencies

To install the required packages, use the following command:

pip install -r requirements.txt

* streamlit
* pandas
* Pillow
* yfinance

To run the application locally, follow these steps:

1. Clone the repository:

git clone https://github.com/peterpapas/stock_market_web_app.git

2. Change to the project directory:
cd stock-market-web-app

3. Run the Streamlit application:
streamlit run app.py

4. Open your browser and visit the URL displayed in the terminal (usually http://localhost:8501).