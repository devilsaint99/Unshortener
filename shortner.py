import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
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

    def shorturl_at(self,wait):
        content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.squareboxbig')))
        self.data = content.text        
            
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

        elif self.url.count('//shorturl.at'):
            site = 'shorturl.at'
            self.drive(site)
            
        else:
            self.data = self.expand_url()
            

    def drive(self,site):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(options=chrome_options)
        driver.accept_untrusted_certs = True
        
        
        if site == 're':
            driver.get(self.url+'+')
            wait = WebDriverWait(driver, 10)
            self.rebrandly(wait)

        elif site == 'bit':
            driver.get(self.url+'+')
            wait = WebDriverWait(driver, 10)
            self.bitly(wait)

        elif site == 'tiny':
            driver.get(self.url+'+')
            wait = WebDriverWait(driver, 10)
            self.tinyurl(wait)
        
        elif site == 'shorturl.at':
            driver.get('https://www.shorturl.at/long-url.php?u='+self.url)
            wait = WebDriverWait(driver, 10)
            self.shorturl_at(wait)
        
        driver.quit()
    
    def hyper(self):
        if not self.url.startswith('https://') and (not self.url.startswith('http://')):
            self.url = 'https://'+self.url
        return self.siteCheck()
    
    def expand_url(self):
        response = requests.head(self.url, allow_redirects=False)
        return response.headers['Location']

