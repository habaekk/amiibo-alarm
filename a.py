import requests
from bs4 import BeautifulSoup
import time

result = requests.get("https://www.nintendo.co.kr/news/list.php",verify=False)
cnt = 0

soup = BeautifulSoup(result.content, "html.parser")
for tit in soup.find_all('span', "ellip"):
    title = tit.get_text()
    # print(title)
    if "amiibo" in title:
        cnt += 1

print("found amiibo:", cnt)
