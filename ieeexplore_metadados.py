import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Referer": "https://ieeexplore.ieee.org",
}

api_url = "https://ieeexplore.ieee.org/rest/search"

payload = {
    "action": "search",
    "highlight": True,
    "matchBoolean": True,
    "matchPubs": True,
    "newsearch": True,
    "queryText": '("All Metadata":"Network automation") AND ("All Metadata":"Closed loop")',
    "ranges": ["2017_2024_Year"],
    "returnFacets": ["ALL"],
    "returnType": "SEARCH",
}


response = requests.post(api_url, json=payload, headers=headers).json()
print(response)

# uncomment this to print all data:
# print(json.dumps(response, indent=4))

for r in response['records']:
    if 'publicationDate' in r:
        print(r['publicationDate'])
    print(r['articleTitle'])
    print(r['abstract'])
    print('-' * 80)