import streamlit as st
from datetime import date

import yfinance as yf
# from prophet import Prophet
# from prophet.plot import plot_plotly
from plotly import graph_objects as go


START = "2010-01-23"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Previsão de Stocks")

#2 variaveis 
stocks = ("AAPL", "TSLA", "BTC-USD", "NFLX")
selected_stock = st.selectbox("selecione a stock", stocks)

#st.cache - forma eficiente do website trabalhar - guarda downloads já feitos
@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

#variavel data_load muda de significado na 2a x q é chamada, dps do download feito
data_load = st.text("Aguarde...")
data = load_data(selected_stock)
data_load.text("Concluído")

st.subheader("Tabela 1 - valores não manipulados")
st.write(data)

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock_open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock_close"))
    #xaxis_rangerslider_visible - facilita a análise do gráfico (eixo do x)
    fig.layout.update(title_text="Open and Close", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

#Previsão até 10 anos
st.subheader("Previsão da stock")
years = st.slider("Anos", 1,10)
period = years * 365

#ValueError: Column ds has timezone specified, which is not supported. Remove timezone.
# df_train = data[["Date", "Close"]]
# df_train = df_train.rename(columns={"Date":"ds", "Close":"y"})

# prophet = Prophet()
# prophet.fit(df_train)
# future = prophet.make_future_dataframe(periods=period)
# forecast = prophet.predict(future)

# st.write(forecast.tail())