from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys
from pyzbar.pyzbar import decode
import re
import requests
sys.path.append('../data/')
import numpy as np
import urllib
import matplotlib.pyplot as plt
from isbntools.app import meta


def BarcodeReader(book_url):
    ###req = urllib.request.urlopen(book_url)
    ###arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    ###img = cv2.imdecode(arr, -1).imread(book_url)
    try:
        with requests.Session() as s:
            page = s.get(book_url)
            with open('temp_img.jpg', 'wb') as f:
                f.write(page.content)
        #img = np.asarray(Image.open('temp_img.jpg'))
        ##img = io.imread(book_url)
        img = plt.imread('temp_img.jpg')
        detectedBarcodes = decode(img)
        if not detectedBarcodes:
            print("Error")
        else:
            for barcode in detectedBarcodes:
                if barcode.data != "":
                    result = barcode.data
                    return result.decode()
        return None
    except:
        return None


def BarcodeLookup(barcode):
    #DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
    ##DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"
    #driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    #url = 'https://www.barcodelookup.com/' + barcode
    #driver.get(url)
    #timeout = 10
    #element = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section[2]/div/div/div[2]'))
    #WebDriverWait(driver, timeout).until(element)
    #result = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[2]').text
    #driver.close()
    #title = result.split('\n')[1]
    #author = re.findall('\nAuthor.*\n',result)[0].replace('\n','')[8:]
    #final_result = re.sub(r'\W+', ' ', title + ' ' + author)
    #return final_result
    try:
        result_dict = meta(barcode)
        result = result_dict['Title'] + ' ' + ' '.join(result_dict['Authors'])
        return result
    except:
        return None

    
def image_to_title(image_url):
    barcode = BarcodeReader(image_url)
    information = BarcodeLookup(barcode)
    return information


if __name__ == "__main__":
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MMfae04ceb6882537e1d8a5b8e772074f7/Media/ME2e69eb7cb514cd0acea6e382cd810eed"
    print(image_to_title(url))
