from datetime import date
from db.sqlite import SQLite
import datetime
import requests
import pandas as pd
import glob
import pickle
import time


class Scrape:
    def __init__(self, url:str='https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'):
        self.url = url
    
    def proxysale():
        
        cookies = {
            'JSESSIONID': '70B8B03895C2D41F4C587D9011F9F9B9',
            '_ga_PDN0GKXB6R': 'GS1.1.1709585778.1.0.1709585778.60.0.0',
            '_ym_uid': '1709585779239221843',
            '_ym_d': '1709585779',
            '_ga': 'GA1.2.2146692544.1709585779',
            '_gid': 'GA1.2.1240199425.1709585779',
            '_gat_UA-77454321-1': '1',
            '_ym_isad': '1',
        }

        headers = {
            'authority': 'free.proxy-sale.com',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'client-ip': '37.78.252.88',
            'content-type': 'application/json',
            # 'cookie': 'JSESSIONID=70B8B03895C2D41F4C587D9011F9F9B9; _ga_PDN0GKXB6R=GS1.1.1709585778.1.0.1709585778.60.0.0; _ym_uid=1709585779239221843; _ym_d=1709585779; _ga=GA1.2.2146692544.1709585779; _gid=GA1.2.1240199425.1709585779; _gat_UA-77454321-1=1; _ym_isad=1',
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


        # .json()
        # return response['data'][0]['adv']['price']

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"page":0,"size":10,"countries":[],"proxyProtocols":["HTTP","HTTPS"],"proxyTypes":[]}'
        #response = requests.post(
        #    'https://free.proxy-sale.com/api/front/main/pagination/filtration',
        #    cookies=cookies,
        #    headers=headers,
        #    data=data,
        #)






















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