from ucimlrepo import fetch_ucirepo

HEART_DISEASE_ID = 45

def pull_heart_disease_dataset():
    data = fetch_ucirepo(id=HEART_DISEASE_ID)

    X = data.data.features
    y = data.data.targets

    return (X, y)

