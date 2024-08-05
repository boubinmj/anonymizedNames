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
    x = str(search).lower()
    if(x in str(s).lower()):
        return s.replace(search, "professor")
    else:
        return s

def load_text(filename):
    df = pd.read_csv(filename)
    return df
    
sf = salesforce_login()
name_keys = get_names(sf)
print(name_keys)

resp = pd.read_csv('NoNulls_NoCommas_Headers.csv')

for el in name_keys:
    resp = resp.apply(lambda x: x.map(lambda s: search_string(s, el)))

resp.to_csv('responses_anon.csv')