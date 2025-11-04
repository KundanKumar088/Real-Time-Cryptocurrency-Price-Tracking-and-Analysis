# requests
# pandas
# datetime

# This function get real time crypto currency price every day at 8am
# this also saves the data to a csv file

# it identify  top 10 crypto and send mail


import requests
import pandas as pd
from datetime import datetime


# API information
url = 'https://api.coingecko.com/api/v3/coins/markets'
param = {
    'vs_currency' : 'usd',
    'order' : 'market_cap_desc',
    'per_page': 250,
    'page': 1
}


# sending request 
response =requests.get(url, params=param)

if response.status_code == 200:
    print('Connection successful! \nGetting the data...')
    
    # storing the response into data
    data = response.json()
    
    # creating a dataframe
    df=pd.DataFrame(data)
    # print(df.columns)
    # print(df.head())
    
    df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'high_24h', 'low_24h', 'price_change_24h', 'price_change_percentage_24h', 'ath', 'atl', ]]   
    
    
    # creating new columns
    today = datetime.now().strftime('%Y-%m-%d')
    df['time_stamp'] = today
    
    # getting top 10
    top_negative = df.sort_values(by='price_change_percentage_24h', ascending=True)
    top_negative_10 = top_negative.head(10)
    top_negative_10.to_csv("crypto_data_temp.csv", index=False)


    
    top_positive = df.sort_values(by='price_change_percentage_24h', ascending=False)
    top_positive_10 = top_positive.head(10)
    top_positive_10.to_csv("crypto_data_temp.csv", index=False)
    
    
    
    
    
    # saving the data to csv file
    df.to_csv("crypto_data_temp.csv", index=False)
    print(f"Top 10 cryptos with highest price decrease % on {today}:\n", top_negative_10)

    print(f"Top 10 cryptos with highest price increase % on {today}:\n", top_positive_10)
    print("data saved successfully!")
    
    
    
    
else:
    print(f"Connection error: {response.status_code}")    