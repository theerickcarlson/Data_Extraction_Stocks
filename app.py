# Import the libraries
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib as plt

# Set the page title & layout
st.set_page_config(page_title = "Stock Data Extraction App", layout = "wide")

# Main title of the app
st.title("Stock Data Extraction App")

# Short description inder the title
st.write("Extract stock market data from Yahoo Finance using a ticker symbol.")

# Sidebar header
st.sidebar.header("User Input")

# Input box for stock ticker
ticker = st.sidebar.text_input("Enter Ticker", "AAPL")

# Input for start date
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023"))

# Input for end date
end_date = st.sidebar.date_input("End Date", dt.to_datetime("today"))

# Download data button
if st.sidebar.button("Get Data"):

    # Create ticker object
    stock = yf.Ticker(ticker)

    # Download historical price data
    df = stock.history(start = start_date, end = end_date)

    # Check if data exists
    if df.empty: 
        st.error("No Data Found. Please check the ticker symbol or date range.")
    else: 

        # Show successful message
        st.success(f"Data successfully extracted for {ticker}")
          
        # Display company information
        st.subheader("Company Information")
        info = stock.info

        company_name = info.get("longname", "N/A")
        sector = info.get("sector", "N/A")
        industry = info.get("industry", "N/A")
        market_cap = info.get("marketCap", "N/A")
        website = info.get("website", "N/A")

        st.write(f"Company Name: {company_name}")
        st.write(f"Sector: {sector}")
        st.write(f"Industry: {industry}")
        st.write(f"Market Cap: {market_cap}")
        st.write(f"Website: {website}")
          
        # Display stock data
        st.subheader("Historical Stock Data")
        st.dataframe(df)

        # Plot closing price
        st.subheader("Closing Price Chart")
        fig, ax = plt.subplots()
        ax.plot(df.index, df["Close"]
        ax.set_xlabel("Date")
        ax.set_ylabel("Closing Price")
        ax.set_title(f"{ticker} Closing Price")
        st.pyplot(fig)

        # Convert data frame to CSV for download
        csv = df.to_csv().encode("utf-8")

        # Download button for csv 
        st.download_button(
            label = "Download Data as CSV",
            data = csv,
            file_name = f"{ticker}_stock_data.csv",
            mime = "text/csv"
        )
