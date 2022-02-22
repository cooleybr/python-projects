import requests

def CVE_Search(term):
    base = 'https://services.nvd.nist.gov/rest/json/cves/1.0/?keyword='
    r = requests.get(base + term)
    return r.json()