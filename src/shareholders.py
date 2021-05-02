import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

emiten = input('Input Emiten : ')
chrome_options = Options()
chrome_options.add_argument('--incognito')
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options, executable_path=os.path.abspath('../drivers/chromedriver'))

url = 'https://www.idx.co.id/en-us/listed-companies/company-profiles/company-profile-detail/?kodeEmiten={}'.format(emiten)

driver.get(url)

# path = '//*[@id="shareholdersTable"]/tbody/tr[1]/td[1]'

row_count = len(driver.find_elements_by_xpath('//*[@id="shareholdersTable"]/tbody/tr'))
colom_count = len(driver.find_elements_by_xpath('//*[@id="shareholdersTable"]/tbody/tr[1]/td'))

first = '//*[@id="shareholdersTable"]/tbody/tr['
second = ']/td['
third = ']'
for n in range(1, row_count+1):
    for m in range(1, colom_count+1):
        final_path = first+str(n)+second+str(m)+third
        table_data = driver.find_element_by_xpath(final_path).text
        print(table_data, end=' ')
    print('')

driver.quit()