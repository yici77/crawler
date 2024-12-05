import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

driver = uc.Chrome
driver.get("https://www.threads.net/search?q=周杰倫")
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(5)

articles_list = driver.find_element(By.CSS_SELECTOR,"div.x1c1b4dv.x13dflua.x11xpdln").find_elements(By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x1ja2u2z")
article_url = [i.find_element(By.CSS_SELECTOR,f'a[href*="/post/"]').get_attribute("href") for i in articles_list if re.search(self.pattern,i.text)]
if article_url:
	articles = []
	for url in article_url:
		driver.get(url)
		time.sleep(3)
		article = driver.find_element(By.CLASS_NAME,"x1a6qonq").text
		articles.append(article)
	if articles:
		article = "\n".join(articles).strip("\n")+"：D"
		self.write(article)
