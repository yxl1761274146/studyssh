import requests

url="https://cdn.heweather.com/china-city-list.txt"
html=requests.get(url)
html.encoding='utf8'
print(html.text)
