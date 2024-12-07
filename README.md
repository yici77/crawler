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
