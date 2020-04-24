import requests

class HeFeng():

    def __init__(self):
        self.url="https://cdn.heweather.com/china-city-list.txt"

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding='utf8'
        print(html.text)
        cities

if __name__=='__main__':
    hefeng=HeFeng()
    hefeng.get_citys()
