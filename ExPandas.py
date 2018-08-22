from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://tv.yahoo.co.jp/listings/?&st=4&s=1&va=24&vb=1&vc=1&vd=0&ve=0&d=20180820'

with open("tvpg.html") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

programStrList = soup.select("#tvpgm > table > tbody > tr > td")
dfs = pd.read_html(str(programStrList))

dfs[1].to_csv("table.csv")
# print(len(dfs))
# print(dfs[1].head())

