# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:21:21 2020

@author: Stian
"""

import json
from selenium import webdriver
import time


class ordlisten:
    
    def __init__(self):
        with open('ticket_navn_ordliste.json') as f:
            self.data = json.load(f)
    
    
    def oversett(self, ticket):
        temp = []
        for ticks in ticket:
            temp.append(self.data[ticks])
        
        return temp
        
    def oversett_inv(self, navn):
        self.inv_data = {v: k for k, v in self.data.items()}
            
        temp = []
        for name in navn:
            temp.append(self.inv_data[name])
        
        return temp
    

def lag_ordliste():
    browser = webdriver.Chrome()
    browser.get('https://www.oslobors.no/markedsaktivitet/#/list/shares/quotelist/ob/all/all/false')
    time.sleep(2)
    
    with open('lag_ticket_navn_ordliste.js','r') as f:
        script = f.read()
    info = browser.execute_script(script)
    browser.close()
    
    with open('ticket_navn_ordliste.json', 'w') as f:
        json.dump(eval(info), f)
        
def komma_oversett(tall_tabell):
    new_tall_tabell = []
    
    for tall in tall_tabell:
        if("," in tall):
            y = tall.split(",")
            x = ".".join(y)
            new_tall_tabell.append(float(x))
        else:
            new_tall_tabell.append(float(tall))
      
    return new_tall_tabell
    
    
    
        
    