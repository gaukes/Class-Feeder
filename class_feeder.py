from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://schedule.berkeley.edu/srchsprg.html')

support_browser = webdriver.Chrome()

department = "***** DEPARTMENT *****"
course_num = "***** COURSE NUMBER ******"

browser.find_element_by_name('p_dept').send_keys(department)
browser.find_element_by_name('p_course').send_keys(course_num)
browser.find_element_by_name('p_course').send_keys(Keys.ENTER)

table_num = 2

WebDriverWait(browser, 10).until(EC.title_contains('UCB Online Schedule'))

while type(table_num) is int:
	try:
		name = browser.find_element_by_xpath('/html/body/table[{0}]/tbody/tr[1]/td[3]/font/b'.format(table_num)).text
		print('ok1')
		more_info = browser.find_element_by_xpath('/html/body/table[{0}]/tbody/tr[12]/td/font/b/input'.format(table_num))
		print('ok2')
		more_info.click()
		print('ok3')
		info = browser.find_element_by_xpath('/html/body/blockquote[1]/div[1]/text()')
		info.send_keys(Keys.CONTROL + 'w')
		print(name)
		print(info.text)
		browser.back()
		table_num += 1
	except:
		table_num = 'exceeded limit'
		print(table_num)

print('Done')