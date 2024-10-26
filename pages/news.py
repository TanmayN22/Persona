import streamlit as st
from stocknews import StockNews
import yfinance as yf
from prophet import Prophet
import plotly.graph_objects as go

class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")



def fetch_stock_news(ticker="", num_articles=5, column=None):
    if column:
        column.header("Latest Stock News")
    else:
        st.header("Latest Stock News")

    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()

    for i in range(min(num_articles, len(df_news))):
        with column:
            column.subheader(f"News {i + 1}")
            column.write(f"**Published:** {df_news['published'][i]}")
            column.write(f"**Title:** {df_news['title'][i]}")
            column.write(f"**Summary:** {df_news['summary'][i]}")


def fetch_stock_data_and_visualize(ticker, column=None):
    try:
        data = yf.download(ticker, start="2010-01-01")
        if data.empty:
            column.error(f"No data found for ticker: {ticker}")
            return

        data.reset_index(inplace=True)
        data = data[['Date', 'Open', 'High', 'Low', 'Close']]
        data.columns = ['ds', 'Open', 'High', 'Low', 'y']
        data['ds'] = data['ds'].dt.tz_localize(None)

        model = Prophet(daily_seasonality=True)
        model.fit(data[['ds', 'y']])

        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)

        # Create a copy of forecast with renamed columns for display only
        forecast_display = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].copy()
        forecast_display = forecast_display.rename(columns={
            'yhat': 'Actual Prediction', 
            'yhat_lower': '-10', 
            'yhat_upper': '+10'
        })

        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data['ds'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['y'],
                                     name='Historical Data'))

        fig.add_trace(go.Scatter(x=forecast['ds'],
                                 y=forecast['yhat'],
                                 mode='lines',
                                 name='Forecast',
                                 line=dict(color='orange', dash='dash')))

        fig.add_trace(go.Scatter(x=forecast['ds'],
                                 y=forecast['yhat_lower'],
                                 mode='lines',
                                 name='Lower Bound',
                                 line=dict(color='red', dash='dash')))

        fig.add_trace(go.Scatter(x=forecast['ds'],
                                 y=forecast['yhat_upper'],
                                 mode='lines',
                                 name='Upper Bound',
                                 line=dict(color='green', dash='dash'),
                                 fill='tonexty'))

        fig.update_layout(title=f'{ticker} Stock Price and Forecast',
                          xaxis_title='Date',
                          yaxis_title='Price (USD)',
                          xaxis_rangeslider_visible=False)

        column.plotly_chart(fig)

        column.write(forecast_display.tail(30))

    except Exception as e:
        column.error(f"An error occurred: {e}")


def main():
    st.title("Stock News and Price Forecast App")

    ticker = st.text_input("Enter Stock Ticker:").upper()
    
    # Create two columns
    col1, col2 = st.columns(2)

    if ticker:
        fetch_stock_news(ticker, column=col1)
        fetch_stock_data_and_visualize(ticker, column=col2)
    else:
        fetch_stock_news(column=col1)

if __name__ == "__main__":
    main()