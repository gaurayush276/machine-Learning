import pandas as pd
# from urllib.request import urlretrieve
# medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'


# urlretrieve(medical_charges_url, 'medical.csv')
medical_df = pd.read_csv('medical.csv')
print(medical_df)
# provides the schema of the data
print(medical_df.info())
# medical_df.describe() gives you all those values by default — but only for numeric columns unless you tell it otherwise.
print(medical_df.describe())
# If you want non-numeric columns included (like sex, region, smoker), use:
# medical_df.describe(include='all')
print("fine")