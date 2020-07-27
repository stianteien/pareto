# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:00:06 2020

@author: Stian
"""

import time
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pareto
import ordliste


class nettbank:
    def __init__(self):
        self.browser = webdriver.Chrome()
    
    def log_in(self, mobil='90202452', født='180295'):
        self.browser.get('https://nettbanken.nordea.no/login/bankid-mobile')
        
        time.sleep(1)
        
        self.browser.find_element_by_id('input-mobile-number').send_keys(mobil)
        self.browser.find_element_by_id('input-dob').send_keys(født)
        self.browser.find_element_by_id('nd-bim-next').click()
        print('logger inn... avventer bankID')
        
        # Sjekker når man er logget inn
        my_switch = True
        while(my_switch):
            time.sleep(1)
            try:
                self.browser.find_element_by_id('nd-bankid-header')
            except:
                my_switch = False
                self.til_oversikt()
        
    
    def til_oversikt(self):
        self.browser.find_element_by_link_text('Sparing og Investering').click()
        self.browser.find_element_by_link_text('Min Spareoversikt').click()
        
        with open('change_dropdown.js','r') as f:
            script = f.read()
        self.browser.execute_script(script) 
        time.sleep(2)
        
    def oversikt(self):
        with open('oversikt_aksjer.js','r') as f:
            script = f.read()
        info = self.browser.execute_script(script)
        
        ordlist1 = ordliste.ordlisten()
        self.mine_aksjer = pd.DataFrame({'Navn':ordlist1.oversett_inv(info[0]),
                                         'Kurs':ordliste.komma_oversett(info[1]),
                                         'Gj.kurs':ordliste.komma_oversett(info[2]),
                                         'Prosent':(info[3]),
                                         'Gevinst':ordliste.komma_oversett(info[4]),
                                         'Antall':ordliste.komma_oversett(info[5]),
                                         'Totalverdi':ordliste.komma_oversett(info[6])})
        
        print(self.mine_aksjer) 
        
        with open('midler.js','r') as f:
           script = f.read()
        markedsverdi, tilgjenglig = self.browser.execute_script(script)   
        
        print(markedsverdi)
        print(tilgjenglig)
        # Penger i markedet
        # Penger på konto/tilgjenlig
        
    def selg(self, ticket, antall):
        # sjekk om man eier aksjen først og gi tilbake antall
        
        
        with open('press_kjøp.js','r') as f:
            script = f.read()
        self.browser.execute_script(script)
        
        with open('søk_aksje.js','r') as f:
           script = f.read()
        self.browser.execute_script("var selg=true;var ticket='"+ticket+"';"+script)
        
        with open('salg_ordre.js','r') as f:
            script = f.read()
        self.browser.execute_script("var antall='"+str(antall)+"';"+script)
        
        with open('bekreft.js','r') as f:
            script = f.read()
        self.browser.execute_script(script)
        
        print("Solgt: ",ticket, antall)
        
    
    def kjøp(self, ticket, antall):
        with open('press_kjøp.js','r') as f:
            script = f.read()
        self.browser.execute_script(script)
        
        
        with open('søk_aksje.js','r') as f:
            script = f.read()
        self.browser.execute_script("var selg=false; var ticket='"+ticket+"';"+script)
        
        with open('kjøps_ordre.js','r') as f:
            script = f.read()
        self.browser.execute_script("var antall='"+str(antall)+"';"+script)
        
        with open('bekreft.js','r') as f:
            script = f.read()
        self.browser.execute_script(script)
        
        print("Kjøpt: ",ticket, antall)
        
        
        
        

#print(ordliste.komma_oversett(["333", "4,44"]))

#print(pareto.month_portofolio())
#ordliste.lag_ordliste()


nordea = nettbank()
nordea.log_in()

