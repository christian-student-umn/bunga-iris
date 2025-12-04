import joblib


def predict(date):
    clf= joblib.load("kkn_model.sav")
    prediction = clf.predict(date)
    return prediction

