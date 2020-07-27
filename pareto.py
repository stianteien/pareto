# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:15:42 2020

@author: Stian
"""

from selenium import webdriver
import pandas as pd
import time
import ordliste

def month_portofolio():
    browser = webdriver.Chrome()
    browser.get('https://www.paretosec.no/maanedsportefoelje')
    
    time.sleep(5)
    
    with open('pareto.js','r') as f:
        script = f.read()
    info = browser.execute_script(script)
    
    pareto_data = pd.DataFrame({'Ticket':info[0], 
                                 'Lagt inn':info[1],
                                 'Måned sluttkurs':ordliste.komma_oversett(info[2]), 
                                 'Kurs':ordliste.komma_oversett(info[3]),
                                 'Dagsendring':(info[4]),
                                 'Månedsendring':(info[5])
                                 })

    browser.close()
    return pareto_data