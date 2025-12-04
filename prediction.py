import joblib


def predict(date):
    clf= joblib.load("rf_model.sav")
    prediction = clf.predict(date)
    return prediction

