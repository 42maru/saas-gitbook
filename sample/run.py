import json
from pprint import pprint

from f2maru_qa.client import Client

app_code = "143e6a1a2384405ebdd98d8174c4080f"
api_key = "938214eb094c432b8f893bbdc8732a26"
client = Client(app_code, api_key)

result = client.bulk_insert(json.load(open('sample.json')))
print("bulk insert result is {}".format(result))

res = client.inquiry("유승호 나이는?")
pprint(res)


