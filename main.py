import nltk
# from nltk.tokenize import word_tokenize
# nltk.download('punkt')
import numpy as np
import pandas as pd 
from credentials_connection import User

def salesforce_login():
    conn = User('dev')
    conn.getCredentials()
    sf = conn.sf_login()
    return sf

def get_names(sf):
    response = sf.query_all("SELECT FirstName, LastName FROM Contact WHERE Active_Full_Time_Faculty__c = True OR Wagner_Adjunct__c = True")
    print("Parsing " + str(len(response['records'])) +  " Names")

    name_list = []
    
    df = pd.DataFrame(response['records'])
    for index, row in df.iterrows():
        name_list.append(row['FirstName'])
        name_list.append(row['LastName'])

    return name_list

def search_string(s, search):
    return search in str(s).lower()

def load_text(filename):
    df = pd.read_csv(filename)
    return df
    
sf = salesforce_login()
name_keys = get_names(sf)

resp = pd.read_csv('NoNulls_NoCommas.csv')

for el in name_keys:
    found = resp.apply(lambda x: x.map(lambda s: search_string(s, el)))
    print(found)

