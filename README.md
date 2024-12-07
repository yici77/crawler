### 這裡有我寫過的爬蟲code

#### threads.py
-爬蟲的網址
```python
userid = ""  #放入要爬蟲的帳號
driver = uc.Chrome()
driver.get(f"https://www.threads.net/@{userid}")
driver.execute_script("window.scrollTo(0, 300);")
```
- 找到頁面中所有發文
```python
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
posts = soup.find_all("div",'x78zum5 xdt5ytf') 
```
- 發文時間、內文、圖片，依序寫入檔案
```python
for post in posts:
    for element in post.find_all():
        if element.name == "time":
            element = element.get("title")+"\n"
            write_txt(element)   #寫檔
        elif element.name == "div" and "x1a6qonq" in element.get("class",[]):
            element = element.text+"\n"
            write_txt(element)
        elif element.name == "picture":
            element = "img："+element.find("img").get("src")
            write_txt(element)
    write_txt("\n==================\n")
```

#### dcard.py
- 要爬蟲的網址
```python
query = ""   #輸入查詢關鍵字
forum = ""   #輸入查詢看板
driver = uc.Chrome()
driver.get(f"https://www.dcard.tw/search/posts?query={query}&forum={forum}&sort=latest")
time.sleep(3)
```
- 找到所有文章的連結
```python
find_path = driver.find_elements(By.TAG_NAME, "h2")
path_list = [i.find_element(By.TAG_NAME, "a").get_attribute("href") for i in find_path]
```
- 標題、發文時間、內文、文章內的連結、圖片，照文章中的順序找出
```python
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
```
- 寫檔
```python
filename = "dcard.txt"
with open(filename, "w", encoding = "utf-8") as outputfile:
    outputfile.write("".join(write_article))
```
