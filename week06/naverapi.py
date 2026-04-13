# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'Client_ID'
client_secret = 'Client_Secret'

def main():

    node = 'news'
    srcText = input('검색어를 입력하세요: ')        # 크롤링할 대상

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)      # [CODE 2]
    total = jsonResponse['total']  
    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)                # [CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100) # [CODE 2]
    
    print('전체 검색 : %d 건' %total)
    
