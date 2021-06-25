import requests

SERVICE_URL = 'http://localhost:8010/clip/'


def process(search_query, best=False, ):
    res = requests.post(SERVICE_URL, json={'search_query': search_query, 'best': best})
    res = res.json()
    return res
