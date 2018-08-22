# coding: UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ブラウザのオプション変数
options = Options()

# Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
# options.set_headless(True)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://tv.yahoo.co.jp/listings/?&st=4&s=1&va=24&vb=1&vc=1&vd=0&ve=0&d=20180827")

html = driver.page_source.encode('utf-8')

# BeautifulSoup???
soup = BeautifulSoup(html, "html.parser")

tags = soup.select("#tvpgm")

with open("tvpg.html", mode="w") as f:
   f.write(str(tags))

# with open("tvpg.html", mode="w") as f:
#     f.write(str(tags))

driver.close()
driver.quit()

for tag in tags:
    print(tag.text)
