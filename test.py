from bs4 import BeautifulSoup
import requests


## accessing the perosnal site
personal_source = requests.get('http://www.virtualwall.org/da/AadlandGL01a.htm').text
soup = BeautifulSoup(personal_source, 'lxml')
info = str(soup.head.find_all('script')).split('"')

print(info)
# info = str(soup.head.find_all('script')[1]).split('"')
