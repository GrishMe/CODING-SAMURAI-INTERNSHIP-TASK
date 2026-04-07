from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def prepare_data(data):
    data["Target"] = data["Close"].shift(-1)
    data.dropna(inplace=True)

    X = data[["Close"]].values
    y = data["Target"].values

    return train_test_split(X, y, test_size=0.2, shuffle=False)

def build_model():
    return RandomForestRegressor(n_estimators=200)