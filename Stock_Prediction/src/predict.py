import matplotlib.pyplot as plt

def plot_predictions(y_test, predictions, ticker):
    plt.figure(figsize=(10,5))
    plt.plot(y_test, label="Actual Price")
    plt.plot(predictions, label="Predicted Price")
    plt.title(f"Stock Price Prediction for {ticker}")
    plt.legend()
    plt.show()