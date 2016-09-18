#!/usr/bin/env python

from urllib.request import urlopen
import json

AMADAEUS_KEY = 'TmP45v08vUF28rYQ0AxfVOkM93idify9'

"""
url = 'https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?apikey=TmP45v08vUF28rYQ0AxfVOkM93idify9&'
json_obj = urllib2.urlopen(url)

origin=BOS&destination=NYC&departure_date=2016-09-18--2016-09-20&one-way=true&direct=true&max_price=9000
"""

def amadeus_search(query):
    api_key = AMADAEUS_KEY
    url = 'https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?apikey='+ api_key
    origin = query #if we only search with origin
    final_url = url + "&origin=" + origin
    print(final_url)
    json_obj = urlopen(final_url).read().decode('UTF-8')
    data = json.loads(json_obj)

    for item in data['results']:
        print (item['destination'], item['departure_date'], item['return_date'], item['price'], item['airline'])


amadeus_search("SYD")
