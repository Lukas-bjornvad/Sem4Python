from selenium import webdriver
import time


browser = webdriver.Firefox()
browser.get('http://www.kultunaut.dk/perl/view/type-nynaut/forside')
browser.find_elements_by_xpath("//b[contains(text(), 'Film')]")[0].click()
time.sleep(2)
browser.find_elements_by_xpath("//div[contains(text(), 'OK')]")[0].click()
browser.find_elements_by_xpath("//b[contains(text(), 'Vælg alle')]")[0].click()
browser.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div/form/table[3]/tbody/tr[2]/td[2]/input[1]")[0].click()
