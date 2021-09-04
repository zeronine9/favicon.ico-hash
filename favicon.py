import mmh3 
import requests
import base64
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-u","--url",help="favicon url", required=True)

args = parser.parse_args()

url = (args.url).strip()
response = requests.get(url)
fav = response.content
test = base64.b64encode(fav)
hash = mmh3.hash(test)

print(hash)
