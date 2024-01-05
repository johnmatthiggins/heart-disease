#!/usr/bin/env python3
import plotly.express as px

from dataset import pull_heart_disease_dataset

def main():
    X, y = pull_heart_disease_dataset()
    print(set(y['num']))

    fig = px.pie(y, values='num', names='num', title='Distribution of Heart Conditions')
    fig.show()




if __name__ == '__main__':
    main()
