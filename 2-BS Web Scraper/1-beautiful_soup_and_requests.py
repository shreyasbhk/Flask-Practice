# Beautiful Soup Tutorial - Web Scraping in Python
#  https://video.hukkeri.org/watch?v=GMppyAPbLYk

import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.youtube.com/')

print(result.status_code)