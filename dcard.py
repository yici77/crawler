import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

query = ""   #輸入查詢關鍵字
forum = ""   #輸入查詢看板
driver = uc.Chrome()
driver.get(f"https://www.dcard.tw/search/posts?query={query}&forum={forum}&sort=latest")
time.sleep(3)

find_path = driver.find_elements(By.TAG_NAME, "h2")
path_list = [i.find_element(By.TAG_NAME, "a").get_attribute("href") for i in find_path]

write_article = []
for path in path_list:
    driver.get(path)
    article = driver.find_element(By.TAG_NAME, "article")

    elements = article.find_elements(By.XPATH,".//h1 | .//span | .//picture | .//time | .//a[@target='_blank']")
    for element in elements:
        if element.tag_name == "h1":
            title = "Title：" + element.text + "\n"
            write_article.append(title)
        elif element.tag_name == "time":
            post_time = "post time:" + element.get_attribute("title") + "\n"
            write_article.append(post_time)
        elif element.tag_name == "span":
            text = element.text + "\n"
            write_article.append(text)
        elif element.tag_name == "picture" and elements.index(element) !=1 :
            img = "img："+element.find_element(By.TAG_NAME,"img").get_attribute("src") + "\n"
            write_article.append(img)
        elif element.tag_name == "a":
            link = "link："+element.get_attribute("href") + "\n"
            write_article.append(link)
    write_article.append("\n==================\n")
driver.close()

filename = "dcard.txt"
with open(filename, "w", encoding = "utf-8") as outputfile:
    outputfile.write("".join(write_article))
