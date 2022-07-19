import sys
import requests
import json

try:
  domain = sys.argv[1]
except:
  print(f"[-] Require Domain \n[+] Usage : python3 {sys.argv[0]} domain")
  exit()

api = "YOUR_API_KEY"

def security_trails(domain, token):
    url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"
    querystring = {"children_only":"true"}
    headers = {
        'accept': "application/json",
        'apikey': token
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result_json=json.loads(response.text)
    subdomains= [i+'.'+ domain for i in result_json['subdomains']]
    return subdomains

subdomains = security_trails(domain, api)

for subdomain  in subdomains:
   print(subdomain)
