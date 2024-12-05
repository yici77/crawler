import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def write_txt(element):
    filename = "dcard.txt"
    with open(filename, "a", encoding = "utf-8") as inputfile:
        return inputfile.write(element)

driver = uc.Chrome()
driver.get("https://www.dcard.tw/search/posts?query=星座運勢&forum=horoscopes&sort=latest")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
find_path = soup.find_all("h2")
path_list = ["https://www.dcard.tw"+i.find("a").get("href") for i in find_path]

for path in path_list:
    driver.get(path)
    article = driver.find_element(By.TAG_NAME, "article")
  
    elements = article.find_elements(By.XPATH,".//h1 | .//span | .//picture | .//time | .//a[@target='_blank']")
    for element in elements:
        if element.tag_name == "h1":
            seperate = "\n====================\n\n"
            title = "Title:" + element.text + "\n"
            write_txt(seperate+title)
        elif element.tag_name == "time":
            post_time = "post time:" + element.get_attribute("title") + "\n"
            write_txt(post_time)
        elif element.tag_name == "span":
            text = element.text + "\n"
            write_txt(text)
        elif element.tag_name == "picture":
            img = element.find_element(By.TAG_NAME,"img").get_attribute("src") + "\n"
            write_txt(img)
        elif element.tag_name == "a":
            link = element.get_attribute("href") + "\n"
            write_txt(link)
driver.close()
