import requests

headers = {'Referer': 'https://www.mzitu.com/166512/2',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'https://www.mzitu.com/xinggan/'

r = requests.get(url,headers=headers)

from bs4 import BeautifulSoup

bs = BeautifulSoup(r)

print(bs.find_all())


