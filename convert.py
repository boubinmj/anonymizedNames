import requests
import numpy as np
import pandas as pd
import csv

dat = pd.read_csv('responses_anon.csv')
# .iloc[0:50].to_string()
text_file = open("Output.txt", "w")
text_file.close()

i = 0
while(i< 2):
    
  text_file = open("Output.txt", "a")
  url = "https://api.tableconvert.com/v2/convert/csv-to-textile"
  payload = {
    'data': dat.iloc[i*50:(i+1)*50].to_string(),
    # 'file': ('f', open('responses_anon.csv', 'rb')),
    # 'url': 'https://github.com/boubinmj/anonymizedNames/blob/main/responses_anon.csv',
    'output[escape]': 'true',
    'output[rowHeader]': 'true',
    'output[thead]': 'true',
  }
  headers = {
    # Get your API key: https://tableconvert.com/profile/
    'Authorization': 'Bearer 2dl6AXWry1ZTYDTUR8NI4Ed9Icrkvpmt'
  }

  i = i + 1

  response = requests.post(url, data=payload, headers=headers)
  text_file.write(response.text)

url = "https://api.tableconvert.com/v2/convert/csv-to-textile"
payload = {
  'data': dat.iloc[i*50:len(dat)].to_string(),
  # 'file': ('f', open('responses_anon.csv', 'rb')),
  # 'url': 'https://github.com/boubinmj/anonymizedNames/blob/main/responses_anon.csv',
  'output[escape]': 'true',
  'output[rowHeader]': 'true',
  'output[thead]': 'true',
}
headers = {
  # Get your API key: https://tableconvert.com/profile/
  'Authorization': 'Bearer 2dl6AXWry1ZTYDTUR8NI4Ed9Icrkvpmt'
}

response = requests.post(url, data=payload, headers=headers)
text_file.write(response.text)

text_file.close()