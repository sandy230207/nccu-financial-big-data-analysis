from modules.driver_loader import DriverLoader
import time
import pandas as pd
from selenium.webdriver.common.by import By
from modules import wait_util

#開啟Browser
driver = DriverLoader().get_chrome_driver()

#開啟新聞頭條
driver.get('https://news.cnyes.com/news/cat/headline?exp=a')

#關上可能跳出的視窗
try:
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[2]/button[2]').click()
except:
    pass

target_time = driver.find_element_by_css_selector('fieldset._Qfx4 > input').click()
for i in range(12):
    left = driver.find_element_by_tag_name("svg").click()
dates = driver.find_elements_by_css_selector("div.react-date-picker__month-view-day-text")
for date in dates:
    if date.text == "1":
        date.click()
        print(date.text)
        break

for i in range(10):
    right = driver.find_elements_by_tag_name("svg")[2].click()
dates = driver.find_elements_by_css_selector("div.react-date-picker__month-view-day-text")
for date in dates:
    if date.text == "31":
        date.click()
        print(date.text)
#72


# #向下滾動N次(N = stop)
# index = 0
# stop = 1
# while True:
#     if index == stop:
#         break
#     driver.execute_script('window.scrollBy(0, 1000)')      
#     time.sleep(1)
#     index += 1
    
# #取得新聞資料
# html_elements = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div[2]/main/div[3]/div[2]/div')

# news_list = []

# count = 0
# #把每筆新聞資料的值填入dictionary的list
# for element in html_elements:
#     count += 1

#     news_dict = {}
#     data_list = element.get_attribute('innerText').split('\n')

#     if len(data_list) != 3:
#         continue        
#     atag_element = element.find_elements(By.XPATH, "./a")
#     if len(atag_element) == 0:
#         continue
#     url = atag_element[0].get_attribute('href')
#     current_handle = driver.current_window_handle
#     driver.execute_script("window.open('" + url + "', 'new_window')","_blank")
#     for i in driver.window_handles:
#         if current_handle !=i:
#             driver.switch_to.window(i)
#             # driver.switch_to.window(driver.window_handles[-1])
  
#     wait_util.wait_by_xpath(driver, '//*[@id="content"]/div/div/div[2]/main/div[3]/article/section[1]')
#     news = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div[2]/main/div[3]/article/section[1]')[0].get_attribute('innerText')
#     news = news.replace('\n', '').replace(',', '，')
#     news_date = driver.find_elements_by_xpath('//*[@id="content"]/div/div/div[2]/main/div[2]/div[2]/time')[0].get_attribute('innerText')
#     news_source = data_list[1]
#     #news = data_list[2]
#     news_dict = {'日期' : news_date, '來源' : news_source, '新聞' : news}
#     news_list.append(news_dict)
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])

# #轉成dataframe 
# df = pd.DataFrame(news_list, columns=['日期', '來源', '新聞'])
# #儲存成csv檔
# df.to_csv('result.csv')

# driver.execute_script("alert('資料下載完成!')")
# input('按任何一鍵跳出')