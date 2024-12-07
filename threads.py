import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def write_txt(element):
    filename = "threads.txt"
    with open(filename, "a", encoding = "utf-8") as outputfile:
        return outputfile.write(element)

userid = ""  #放入要爬蟲的帳號
driver = uc.Chrome()
driver.get(f"https://www.threads.net/@{userid}")
driver.execute_script("window.scrollTo(0, 300);")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
posts = soup.find_all("div",'x78zum5 xdt5ytf')  #先找到存放文章的標籤

for post in posts:
    for element in post.find_all():
        if element.name == "time":
            post_time = "TIME："+element.get("title")+"\n"
            write_txt(post_time)
        elif element.name == "div" and "x1a6qonq" in element.get("class",[]):
            text = element.text+"\n"
            write_txt(text)
        elif element.name == "picture":
            img = "img："+element.find("img").get("src")
            write_txt(img)
    write_txt("\n==================\n")
driver.close()
