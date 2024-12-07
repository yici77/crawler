import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def write_txt(element):
    filename = "threads.txt"
    with open(filename, "a", encoding = "utf-8") as outputfile:
        return outputfile.write(element)

driver = uc.Chrome()
driver.get("https://www.threads.net/@twtd003?hl=zh-tw")
driver.execute_script("window.scrollTo(0, 300);")
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
posts = soup.find_all("div",'x78zum5 xdt5ytf')  #先找到存放文章的標籤

for post in posts:
    for element in post.find_all():
        if element.name == "time":
            element = element.get("title")+"\n"
            write_txt(element)
        elif element.name == "div" and "x1a6qonq" in element.get("class",[]):
            element = element.text+"\n"
            write_txt(element)
        elif element.name == "picture":
            element = "img："+element.find("img").get("src")
            write_txt(element)
    write_txt("\n==================\n")
		self.write(article)
