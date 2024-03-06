from datetime import date
from db.sqlite import SQLite
import json
import datetime
import requests
import pandas as pd
import glob
import pickle
import time


class Scrape:
    def __init__(self, url:str='https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'):
        self.url = url
    
    def proxysale(self):
        cookies = {
            '_ga_PDN0GKXB6R': 'GS1.1.1709585778.1.0.1709585778.60.0.0',
            '_ym_uid': '1709585779239221843',
            '_ym_d': '1709585779',
            '_ga': 'GA1.2.2146692544.1709585779',
            'JSESSIONID': '193325E20E3006F0EFE153AFB101CD78',
        }

        headers = {
            'authority': 'free.proxy-sale.com',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'client-ip': '5.139.228.44',
            'content-type': 'application/json',
            'origin': 'https://free.proxy-sale.com',
            'referer': 'https://free.proxy-sale.com/ru/http/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }

        json_data = {
            'page': 0,
            'size': 10,
            'countries': [],
            'proxyProtocols': [
                'HTTP',
                'HTTPS',
            ],
            'proxyTypes': [],
        }

        response = requests.post(
            'https://free.proxy-sale.com/api/front/main/pagination/filtration',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        return response
    
    def response_to_json(self, path:str, response):
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(response.json(), file, indent=2)

if __name__ == '__main__':
    scraper = Scrape()
    response = scraper.proxysale()
    scraper.response_to_json('proxy.json', response)
    





















# class Scrape:
#     def __init__(self):
    #     self.proxy_in = None
    #     self.proxy_out = None
    #     self.proxy_diff = None
    #     self.proxy_diff_seconds = 120

    # def _refresh_proxy(self):
    #     """
    #     Refreshes the proxy if necessary. If the proxy has been in use for more than 120 seconds, 
    #     it restarts the proxy by sending a request to the specified URL. 
    #     If the request returns a status code of 400, it sleeps for 55 seconds and tries to refresh the proxy again.
    #     If the proxy has been in use for less than 120 seconds, it sleeps for the remaining time before refreshing the proxy.
    #     """
    #     if self.proxy_out is not None:
    #         self.proxy_in = datetime.datetime.now()
    #         self.proxy_diff = self.proxy_in - self.proxy_out
    #         self.proxy_diff_seconds = self.proxy_diff.total_seconds()
        
    #     if self.proxy_diff_seconds is None or self.proxy_diff_seconds >= 120:
    #         headers = {}