# Import Dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#from lxml import html#, etree
#import pandas as pd
import urllib.parse
import requests
import time
import os


def title_to_link(title):

    # If the google search returned a title with the word book, remove "book"
    if title[-4:] == "book":
        title = title[:-5]
    title = title.replace('cover','')
    title = title.replace('audiobook','')
    title = title.replace('book','')
    
    url = "https://libgen.is/search.php?&"
    params = {
        'req': title,
        'view': 'simple',
        'sort': 'extension',
        'sortmode': 'DESC'
    }
    url += urllib.parse.urlencode(params)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find_all('table')[2]
    pdf_url = ""#"I can't find this title."
    file_type_lst = ['pdf','epub']
    for e in table:
        try:
            file_type = e.find_all('td')[8].text
            if file_type in file_type_lst:
                links = e.find_all('td')[2].find_all('a')
                for link in links:
                    print(link['href'])
                    if 'book' in link['href']:
                        book_code = link['href'].split('=')[1]
                        library_url = "http://library.lol/main/" + book_code
                        print(f"library_url: {library_url}")
                        pdf_url = requests.get(library_url).text.split("\">Cloudflare")[0].split("href=\"")[-1]
                        print(f"pdf_url: {pdf_url}")
                break
        except:
            pass

    return pdf_url


def title_to_link_old(title):
    
    timeout = 6
    
    try:
        # Using Chrome to access web
        ## DRIVER_PATH = r'/Users/gstenger/Downloads/chromedriver 2'
        ##DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"
        DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
        title = title.replace('cover','')
        title = title.replace('audiobook','')
        title = title.replace('book','')
        
        url = "https://libgen.is/search.php?&"
        params = {
            'req': title,
            'view': 'simple',
            'sort': 'extension',
            'sortmode': 'DESC'
        }
        url += urllib.parse.urlencode(params)
        
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        
        # Open the website
        driver.get(url)
        print(str(driver.page_source)[:1000])

        # Click the link of the first pdf
        file_type_lst = ['pdf','epub','txt']
        
        found = False
        for i in range(10):
            pdf_element = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[{}]/td[9]'.format(2+i))
            if pdf_element.text in file_type_lst:
                try:
                    element = EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[3]/a[2]'))
                    WebDriverWait(driver, timeout).until(element)
                    link = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[3]/a[2]').get_attribute("href")
                    driver.get(link)
                    found = True
                except Exception as E:
                    print(E)
                try:
                    element = EC.presence_of_element_located((By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[3]/a'))
                    WebDriverWait(driver, timeout).until(element)
                    link = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[2]/td[3]/a').get_attribute('href')
                    driver.get(link)
                    found = True
                except Exception as E:
                    print(E)
                if found:
                    break
        
        # Click the link to get to pdfs
        element = EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td[3]/b/a'))
        WebDriverWait(driver, timeout).until(element)
        final_url = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]/b/a').get_attribute("href")#.click()
        driver.close()

        return final_url

    except Exception as E:
        print(E)
        driver.close()

    return None

if __name__ == "__main__":
    title = 'discourse on method rene descartes'
    print(title_to_link_old(title))
