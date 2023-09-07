import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class UrlCheck():
    def __init__(self,url):
        self.url = url
        self.data = ''

    def rebrandly(self,wait):
        content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Text-Title.Text--SubDetail.Text--small.ellipsis')))
        self.data = content.text
        

    def bitly(self,wait):
        content= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.item-detail--url')))
        self.data = content.text
    
    def tinyurl(self,wait):
        content= wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.text-3xl.font-weight-bold.text-blue.ml-2.break-all')))
        self.data = content[1].text
        
            
    def siteCheck(self):
        if self.url.count('//rb.gy'):
            site = 're'
            self.drive(site)
            
        elif self.url.count('//bit.ly'):
            site = 'bit'
            self.drive(site)
            
        elif self.url.count('//tinyurl'):
            site = 'tiny'
            self.drive(site)
            
        else:
            self.data = self.expand_url()
            

    def drive(self,site):
        driver = webdriver.Chrome()
        driver.accept_untrusted_certs = True
        driver.get(self.url+'+')
        wait = WebDriverWait(driver, 10)
        if site == 're':
            self.rebrandly(wait)
        elif site == 'bit':
            self.bitly(wait)
        elif site == 'tiny':
            self.tinyurl(wait)
        driver.quit()
    
    def hyper(self):
        if not self.url.startswith('https://') and (not self.url.startswith('http://')):
            self.url = 'https://'+self.url
        return self.siteCheck()
    
    def expand_url(self):
        response = requests.head(self.url, allow_redirects=False)
        return response.headers['Location']

