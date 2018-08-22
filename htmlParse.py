# coding: UTF-8
from bs4 import BeautifulSoup

with open("tvpg.html") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

channesStrs = soup.select("#ListingsHeader > tbody > tr > td")

channelList = []
for channelStr in channesStrs:
    channelList.append(channelStr.text)

print(channelList[4])

programStrList = soup.select("#tvpgm > table > tbody > tr > td > table:nth-of-type(2) > tbody > tr > td")
programList = []
for programStr in programStrList:
    timeStrList = programStr.select("span > span")
    programTitleList = programStr.select("span > a")

    # 番組情報List
    programList.append(programStr.text)

    for timeStr in timeStrList:
        print(timeStr.text)
    for titleStr in programTitleList:
        print(titleStr.text)
        print(titleStr.get('href'))
    # print(programStr.get('rowspan'))
    # print(programStr.text)
