# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import date

def get_data_frame():
    '''downloads the lates csv lotto file '''
    
    today = date.today()
    
    print("latest csv for ",today)
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.pais.co.il/lotto/archive.aspx')
    lotto_txt = driver.find_element_by_link_text('הורדת תוצאות ההגרלה בפורמט CSV').click()
    #with open('latest_lotto.txt','w') as latest_lotto:
        #.write(lotto_txt)
        

        
    #latest_lotto.close()
    
    #df = pd.read_csv(csv)
    
    driver.close()
    
       
    
    return None

#get_data_frame()
    




    
    