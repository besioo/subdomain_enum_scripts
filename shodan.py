import requests
import json
import sys

domain = sys.argv[1]

api_key = "YOUR_API_KEY"

results = requests.get(f"https://api.shodan.io/dns/domain/{domain}?key={api_key}")

jdata = json.loads(results.text)

subdomains = []

for sub in jdata["subdomains"]:
    subdomains.append(sub + "." + domain)

for sub in subdomains:
    print(sub)


