from inspect import classify_class_attrs
from msilib.schema import Class
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.espn.com.br/nba/classificacao")

element = driver.find_element(By.CLASS_NAME, 'Table Table-align-rigth')
# element.find_element(By.CLASS_NAME, 'Table Table-align-rigth')
print(element)
