import requests
import numpy as np
import pandas as pd
import csv

dat = pd.read_csv('responses_anon.csv').iloc[0:5].to_string()

url = "https://api.tableconvert.com/v2/convert/csv-to-textile"
payload = {
  'data': dat,
  # 'file': ('f', open('responses_anon.csv', 'rb')),
  # 'url': 'https://github.com/boubinmj/anonymizedNames/blob/main/responses_anon.csv',
  'output[escape]': 'true',
  'output[rowHeader]': 'true',
  'output[thead]': 'true',
}
headers = {
  # Get your API key: https://tableconvert.com/profile/
  'Authorization': 'Bearer <bearer>'
}

response = requests.post(url, data=payload, headers=headers)
text_file = open("Output.txt", "w")
text_file.write(response.text)
text_file.close()