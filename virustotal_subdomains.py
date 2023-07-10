import requests,sys,json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


API_KEY = ''
domain = sys.argv[1]

req = requests.get(f"https://www.virustotal.com/vtapi/v2/domain/report?apikey={API_KEY}&domain={domain}")

data = json.loads(req.text)

for sub in data["subdomains"]:

	print(sub)
