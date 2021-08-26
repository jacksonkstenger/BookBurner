from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
#import cv2
from pyzbar.pyzbar import decode
import re
import requests
import PIL
sys.path.append('../data/')
import numpy as np
import urllib
from skimage import io

def BarcodeReader(book_url):
    ###req = urllib.request.urlopen(book_url)
    ###arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    ###img = cv2.imdecode(arr, -1).imread(book_url)
    with requests.Session() as s:
        s.get(book_url)
        with open('temp_img.jpg', 'wb') as f:
            f.write(page.content)
    img = np.asarray(Image.open('temp_img.jpg'))
    #img = io.imread(book_url)
    detectedBarcodes = decode(img)
    if not detectedBarcodes:
        print("Error")
    else:
        for barcode in detectedBarcodes:
            if barcode.data != "":
                result = barcode.data
                return result.decode()
    return None

def BarcodeLookup(barcode):
    DRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', None)
    #DRIVER_PATH = r"C:\Users\Jackson\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    url = 'https://www.barcodelookup.com/' + barcode
    driver.get(url)
    element = driver.find_element_by_xpath('/html/body/div[1]/section[2]/div/div/div[2]')
    result = element.text
    driver.close()
    title = result.split('\n')[1]
    author = re.findall('\nAuthor.*\n',result)[0].replace('\n','')[8:]
    final_result = re.sub(r'\W+', ' ', title + ' ' + author)
    return final_result
    
def image_to_title(image_url):
    barcode = BarcodeReader(image_url)
    information = BarcodeLookup(barcode)
    return information


if __name__ == "__main__":
    # url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM2731b3d74b95937e4caea55f86530858/Media/ME0b75de784bb7dd2b33d4e97ddc156ccd"
    url = "https://api.twilio.com/2010-04-01/Accounts/AC15abe67bd635f83f4fa678d17ccf9e6d/Messages/MM5da7bbd6c8af667b494b94d1dfb8c215/Media/ME828bbe7ea2257e7dbb0b370a7eba1908"
    print(image_to_title(url))
