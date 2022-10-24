#importo tutti i pacchetti necessari allo scritp
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

#setto il browser da usare
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#impostiamo le classi per contenere i dati
tessera=[]

#login
driver.get("https://gestionale.sism.org/login.php")

login = driver.find_element_by_xpath("//input").send_keys(aUSERNAME)
password = driver.find_element_by_xpath("//input[@type='password']").send_keys(PASSWORD)
submit = driver.find_element_by_xpath("//input[@value='login']").click()

#passa alla pagina soci
driver.get("https://gestionale.sism.org/iscrizioni_new.php")