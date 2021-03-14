from jsonpath import jsonpath
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.87 Safari/537.36',
}
url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

response = requests.get(url=url, headers=headers)

a = response.json()
print(jsonpath(a, "$..name"))
