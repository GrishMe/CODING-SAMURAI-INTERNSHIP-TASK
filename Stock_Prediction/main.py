from src.data_loader import load_stock_data
from src.train import train_model
from src.predict import plot_predictions

def main():
    ticker = "AAPL"  # You can change this to TSLA, MSFT, etc.
    data = load_stock_data(ticker)
    model, X_test, y_test = train_model(data)
    predictions = model.predict(X_test)
    plot_predictions(y_test, predictions, ticker)

if __name__ == "__main__":
    main()