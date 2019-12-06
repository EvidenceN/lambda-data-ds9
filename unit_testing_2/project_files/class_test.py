import unittest
import pandas as pd 
from class_example import data_split

# url with test data for testing functions. 
data_url = 'https://raw.githubusercontent.com/EvidenceN/lambda-data-ds9/master/US%20Alcohol%20Consumption.csv'

data = pd.read_csv(data_url)

split = data_split()

train, test, val = split.split_data(data)