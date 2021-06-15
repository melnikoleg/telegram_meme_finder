
import time
import requests
SERVICE_URL = 'http://localhost:8010/clip/'


def process(search_query):
    s0 = time.time()

    res = requests.post(SERVICE_URL, json={'search_query': search_query,})
    res = res.json()

    return res
