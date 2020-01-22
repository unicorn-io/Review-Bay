import pandas as pd
import seaborn as sns



def get_prod_count(data):
    return len(data['prodID'])

def get_good_count(data):
    return list(data['Positive'].value_counts())[0]

def get_neutral_count(data):
    return list(data['Neutral'].value_counts())[1]

def get_bad_count(data):
    return list(data['Negative'].value_counts())[1]

def get_good_percent(data):
    return round(get_good_count(data)/get_prod_count(data) * 100, 2)

def get_neutral_percent(data):
    return round(get_neutral_count(data)/get_prod_count(data) * 100,2)
    
def get_bad_percent(data):
    return round(get_bad_count(data)/get_prod_count(data) * 100,2)


#data = pd.read_csv('a.csv')

#print(data.head())