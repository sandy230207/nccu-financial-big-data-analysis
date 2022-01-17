# -*- coding: utf-8 -*-
from os.path import dirname, abspath, join
from selenium import webdriver
import os


class DriverLoader(object):
    
    _driver_path = None
    _download_dir = '.'
    
    def __init__(self):
        self.driver_path = abspath(join(dirname(__file__), '.', 'chromedriver'))
        self.download_dir = abspath(join(dirname(__file__), '../download', ''))

    # 取得driver 並指定下載路徑
    def get_chrome_driver(self):
        os.environ["DBUS_SESSION_BUS_ADDRESS"] = '/dev/null'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.download_dir}
#         chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=self.driver_path, chrome_options=chrome_options, keep_alive=True)
        driver.implicitly_wait(3)
        return driver

    # 設定下載路徑
    def set_download_path(self, path):
        self.download_dir = path
            

if __name__ == '__main__':
    driver = DriverLoader().get_chrome_driver();
    driver.delete_all_cookies()
    driver.get('https://python.org')
    for i in driver.get_cookies():
        print(i)

