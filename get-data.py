import requests
from bs4 import BeautifulSoup
import re
import time
from modules.driver_loader import DriverLoader
import pandas as pd


news_list = []

# response = requests.get("https://udn.com/search/tagging/2/%E5%8F%B0%E6%8C%87%E6%9C%9F")
# soup = BeautifulSoup(response.text, "html.parser")

driver = DriverLoader().get_chrome_driver()
#開啟新聞頭條
driver.get('https://udn.com/search/tagging/2/%E5%8F%B0%E6%8C%87%E6%9C%9F')

#向下滾動N次(N = stop)
index = 0
stop = 150
while True:
    if index == stop:
        break
    driver.execute_script('window.scrollBy(0, 1500)')      
    time.sleep(1)
    index += 1

links = driver.find_elements_by_css_selector("div.story-list__text [href]")
urls = [link.get_attribute('href') for link in links]
for url in urls:
    news_dict = {}
    if url != "#":
        news = requests.get(url)
        news_soup = BeautifulSoup(news.text, "html.parser")
        contents = news_soup.select(".article-content__editor")

        time = str(news_soup.select(".article-content__time")).lstrip("[<time class=\"article-content__time\">").rstrip("</time>]")
        source = str(news_soup.select(".article-content__author")).lstrip("[<span class=\"article-content__author\">").replace("\n","").replace(" ","").split("/")[0]
        news_dict["time"] = time
        news_dict["source"] = source

        news = ""
        for content in contents:
            targets = content.find_all("p")
            for target in targets:
                tstring = str(target).rstrip("</p>").replace("<p>","").replace("\n","",-1)
                tlist = re.split("<a |<strong>|</strong>|</a>", tstring)
                for t in tlist:
                    if t.startswith("href=\""):
                        tlist.remove(t)
                    elif t == "":
                        tlist.remove(t)
                tstring = ""
                for t in tlist:
                    tstring = f'{tstring}{t}'
                news = f'{news}{tstring}'
            res_list = re.split("\">", news)
            for r in res_list:
                if r.startswith("href=\""):
                    res_list.remove(r)
            news = ""
            for r in res_list:
                news = f'{news}{r}'.replace("\n","",-1)
        news_dict["news"] = news
        news_list.append(news_dict)

# print(news_list)

#轉成dataframe 
df = pd.DataFrame(news_list, columns=['time', 'source', 'news'])
#儲存成csv檔
df.to_csv('result-mine.csv')

driver.execute_script("alert('資料下載完成!')")
input('按任何一鍵跳出')