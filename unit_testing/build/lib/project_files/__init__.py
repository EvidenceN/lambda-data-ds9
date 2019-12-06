
"""
Functions for doing data analysis.

"""

# function to split data into train, test, validate data

import sklearn
from sklearn.model_selection import train_test_split


def split_data(df):
    '''
    function to split data into train, test, validate data

    The dataframe is split into 15% test, then 85% train. 
    The train data set is then further split into 20% validation
    and 80% train dataset. 

    So the final result is 15% of original data = test
    about 15% of original data is validation,
    and 70% of original data is train. 

    '''

    train, test = train_test_split(df, test_size=0.15, random_state=42)

    train, val = train_test_split(train, test_size=0.20, random_state=42)

    return train, test, val

# function to split into target and features dataset.


def target_features(target):
    '''
    function to split into target and features dataset.

    Target = target from the dataframe. 

    '''

    target = target
    features = train.columns.drop(target)

    x_train = train[features]
    y_train = train[target]
    x_val = val[features]
    y_val = val[target]
    x_test = test[features]
    y_test = test[target]

    return x_train, y_train, x_val, y_val, x_test, y_test
