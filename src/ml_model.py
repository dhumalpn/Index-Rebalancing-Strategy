from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)
    return model

def predict_probabilities(model, X):
    return model.predict_proba(X)[:, 1]
