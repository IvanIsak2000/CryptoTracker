from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from typing import Optional
from sqlmodel import SQLModel
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ.get('KEY')



class CryptoToken(SQLModel):
    id_: int
    name: str 
    slug: str 
    price_by_USD: float 
 
token_id = 1 #USD


#последние котировки
url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'id':token_id,  
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': f'{KEY}'
}


session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)

if response.status_code == 200:
    data = json.loads(response.text)
    status_code = data['status']['error_code']

    if status_code == 0:
        for _, i in data['data'].items():
            token = CryptoToken(
                id_=i['id'],
                name=i['name'],
                slug = i['slug'],
                price_by_USD=i['quote']['USD']['price']
                )
            print(token)

    else:
        print(f'{status_code}: {data["status"]["error_message"]}')
else:
    print(response.text)
