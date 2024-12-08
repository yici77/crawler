import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from io import StringIO

def get_web(id):
    url = f"https://www.vscinemas.com.tw/vsweb/film/detail.aspx?id={id}"
    headers = {"user-agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    return resp.text

soup = BeautifulSoup(get_web(""), "html.parser")
value1 = soup.find("h2").find("a").get("href").strip("detail.aspx?id=")

soup = BeautifulSoup(get(value1), "html.parser")
values = soup.find("div","fastSelect").find_all("option")

dfs = []
for i in values[1:]:
    movie = i.text
    if not re.search(r"現場直播|觀影會|見面會", movie):
        html = get_web(i.get("value"))
        if "<table" in html:
            html = StringIO(html)
            df = pd.read_html(html)[0]
            
            new_row = {0: "電影", 1: movie}
            df = pd.concat([pd.DataFrame([new_row]),df], ignore_index=True)
            dfs.append(df)

rows = [df[1].values for df in dfs]
columns = dfs[0][0].str.strip("：").values
combine_df = pd.DataFrame(rows,columns=columns)

combine_df.to_csv("movie.csv", index=False, encoding="utf-8")
