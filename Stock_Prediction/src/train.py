from .model import prepare_data, build_model

def train_model(data):
    X_train, X_test, y_train, y_test = prepare_data(data)

    model = build_model()
    model.fit(X_train, y_train)

    return model, X_test, y_test