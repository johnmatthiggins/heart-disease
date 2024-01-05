#!/usr/bin/env python

import sklearn as sk
from sklearn import tree
import plotly.express as px
from dataset import pull_heart_disease_dataset

def main():
    X, y = pull_heart_disease_dataset()

    X = X.dropna()

    # sample size
    train_X = X.sample(frac=0.75, random_state=1)
    train_y = y.iloc[train_X.index]

    y = y.iloc[X.index]

    test_X = X.drop(labels=train_X.index, axis=0)
    test_y = y.drop(labels=train_X.index, axis=0)

    model = tree.DecisionTreeClassifier()
    model.fit(train_X, train_y)

    y_hat = model.predict(test_X)

    accuracy = sk.metrics.accuracy_score(test_y, y_hat)
    print('accuracy = ', accuracy)

    # fig = px.histogram(y, x='num')
    # fig.show()


if __name__ == '__main__':
    main()
