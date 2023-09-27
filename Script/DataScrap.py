from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import csv


csv_file =  open('earthquake.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)



url = 'https://seismonepal.gov.np/earthquakes'

def get_page_source(url):
    start_date = '2015-04-01'
    end_date = '2023-09-01'
    driver = webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(4)

    start = driver.find_element(By.XPATH, '//*[@id="dStart"]')
    end = driver.find_element(By.XPATH, '//*[@id="dEnd"]')
    search_button = driver.find_element(By.XPATH, '//*[@id="searchEQ"]')

    start.send_keys(start_date)
    end.send_keys(end_date)
    search_button.click()
    time.sleep(5)
    return driver.page_source

source = get_page_source(url)
soup = BeautifulSoup(source, 'html.parser')

table_body = soup.find('tbody', id='searchResultBody')
table_rows = table_body.find_all('tr')

for row in table_rows:
    row_data = row.find_all('td')
    cell_data = []
    for cell in row_data[0:-1]:
        cell_data.append(cell.text)
    print(cell_data)
    csv_writer.writerow(cell_data)
    print(cell_data)




