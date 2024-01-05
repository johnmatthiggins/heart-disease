#!/usr/bin/env python
from dataset import pull_heart_disease_dataset

def main():
    X, y = pull_heart_disease_dataset()
    print(X)

if __name__ == '__main__':
    main()
