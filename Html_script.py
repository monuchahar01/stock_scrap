# -*- coding: utf-8 -*-
"""
Created on 02012022

@author: monu@chahar
"""
import os
import time
import requests
import sys
import shutil


def retrieve_html():
    shutil.rmtree("Data/ _Data", ignore_errors=True)
    
    #url_ = 'https://www.screener.in'
    values = {'username': 'Chaharmonu',
              'password': 'Screener@123'}

    
    for page in range(1,116):
        
        url='https://www.screener.in/screens/605012/sample/?sort=market+capitalization&order=desc&page={}'.format(page)
        
        requests.post(url, data=values)
        texts=requests.get(url)
        
        text_utf=texts.text.encode('utf=8')
        if not os.path.exists("Data/Html_Data"):
            os.makedirs("Data/Html_Data")
        with open("Data/Html_Data/{}.html".format(page),"wb") as output:
            output.write(text_utf)
        time.sleep(1)    
            
    sys.stdout.flush()


        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
        
    
