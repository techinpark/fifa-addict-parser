import requests

url = "https://kr.fifaaddict.com/api2"

querystring = {"q":"fo4db","class":"tc","locale":"kr"}

headers = {
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
