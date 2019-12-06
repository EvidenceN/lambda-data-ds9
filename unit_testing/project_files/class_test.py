import pandas as pd 

# url with test data for testing functions. 
data_url = 'https://raw.githubusercontent.com/EvidenceN/lambda-data-ds9/master/US%20Alcohol%20Consumption.csv'

data = pd.read_csv(data_url)

from class_example import data_split

split = data_split(data)

