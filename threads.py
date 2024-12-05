import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

userid_list = ["astrologer.patrick","riman.xs.zaia","miraclealpaca_tarot","macaumdd","astro_crystal2020"]   #要爬取的 userid
driver = self.driver
for userid in userid_list:
    driver.get(f"https://www.threads.net/@{userid}")
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(5)

    articles_list = driver.find_element(By.CSS_SELECTOR,"div.x1c1b4dv.x13dflua.x11xpdln").find_elements(By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x1ja2u2z")
    article_url = [i.find_element(By.CSS_SELECTOR,f'a[href*="/@{userid}/post/"]') for i in articles_list if re.search(self.pattern,i.text)]
    if article_url:
        driver.get(f"{article_url[0].get_attribute("href")}")
        time.sleep(3)

        article_list = driver.find_elements(By.CLASS_NAME,"x1a6qonq")[0:3]
        article = [i.text for i in article_list]
        if "留言" in article[0]:
            if "留言" in article[2]:
                article.pop(2)
                article = "\n".join(article)+"：D"
            else:
                article = "\n".join(article)+"：D"
        else:
            article = article[0]+"：D"
        self.write(article)
