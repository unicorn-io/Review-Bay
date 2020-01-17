import pandas as pd
import seaborn as sns



def get_prod_count():
    return len(data['prodID'])

def get_good_count():
    return list(data['Positive'].value_counts())[1]

def get_neutral_count():
    return list(data['Neutral'].value_counts())[1]

def get_bad_count():
    return list(data['Negative'].value_counts())[1]

def get_good_percent():
    return get_good_count()/get_prod_count() * 100

def get_neutral_percent():
    return get_neutral_count()/get_prod_count() * 100
    
def get_bad_percent():
    return get_bad_count()/get_prod_count() * 100


data = pd.read_csv('a.csv')

print(data.head())