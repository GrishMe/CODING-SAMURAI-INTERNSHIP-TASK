import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

st.title("📈 Stock & Crypto Price Prediction App")

symbol = st.text_input("Enter symbol (AAPL, TSLA, BTC-USD, etc.)", "AAPL")

if st.button("Predict"):
    data = yf.download(symbol, period="5y")

    st.subheader("Historical Price Chart")
    st.line_chart(data["Close"])

    # Random Forest
    data_rf = data.copy()
    data_rf["Target"] = data_rf["Close"].shift(-1)
    data_rf = data_rf.dropna()

    X = data_rf[["Open", "High", "Low", "Close", "Volume"]]
    y = data_rf["Target"]

    rf = RandomForestRegressor(n_estimators=200)
    rf.fit(X, y)

    next_day_features = data[["Open", "High", "Low", "Close", "Volume"]].iloc[-1:].values
    rf_pred = rf.predict(next_day_features)[0]

    st.write(f"### 🔮 Random Forest Prediction: **{rf_pred:.2f}**")

    # LSTM
    lstm_data = data[["Close"]].values
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(lstm_data)

    X_lstm, y_lstm = [], []
    for i in range(60, len(scaled)):
        X_lstm.append(scaled[i-60:i, 0])
        y_lstm.append(scaled[i, 0])

    X_lstm = np.array(X_lstm).reshape(-1, 60, 1)
    y_lstm = np.array(y_lstm)

    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(60, 1)),
        LSTM(50),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    model.fit(X_lstm, y_lstm, epochs=3, batch_size=32, verbose=0)

    last_60 = scaled[-60:].reshape(1, 60, 1)
    lstm_pred = scaler.inverse_transform(model.predict(last_60))[0][0]

    st.write(f"### 🤖 LSTM Prediction: **{lstm_pred:.2f}**")
