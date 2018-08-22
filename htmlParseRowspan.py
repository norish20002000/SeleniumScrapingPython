#cording: UTF-8
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import inspect
import sampleRowspanScreaping

pd.set_option("display.max_colwidth", 1000)
pd.set_option("display.max_columns", 20)
pd.set_option('display.max_rows', 2000)

with open("tvpg.html") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# programTrList = soup.findAll("#tvpgm > table > tbody > tr > td > table:nth-of-type(2) > tbody > tr")
programTrList = soup.select("#tvpgm > table > tbody > tr > td > table")
# print(programTrList[1])
rows, num_rows, num_cols = sampleRowspanScreaping.pre_process_table(programTrList[1])
df = sampleRowspanScreaping.process_rows(rows, num_rows, num_cols)
# print(df.iloc[0:1, 0:2])
print(df)

with open("ex3.txt", mode="w") as f:
    # f.write(str(df.iloc[:, :]))
    f.write(str(df))

# programDatas = [[data.get_text() for data in row.find_all('td')] for row in programTrList]

# rowspan = []
# for trNo, tr in enumerate(programTrList):
#     for tdNo, td in enumerate(tr.find_all('td')):
#         # print(td.has_key("rowspan"])

#         if td.has_attr("rowspan"):
#            rowspan.append([trNo, tdNo, int(td["rowspan"]), td.get_text()])

# if rowspan:
#     for i in rowspan:
#         print(i)
#         for j in range(1, i[2]):
#             # rowspan分 行追加
#             programDatas[i[0]+j].insert(i[1], i[3])

# df = pd.DataFrame(data=programDatas[31])


# print(df)

# data = [str(i) + '\n' for i in programDatas]
# print(programDatas)
# with open("ex3.txt", mode="w") as f:
#    f.write(str(data))

# trList = []
# rowspanList = []
# for trIndex, programTr in enumerate(programTrList):
#     programTdList = programTr.select("td")

#     for tdIndex, programTd in enumerate(programTdList):
#         rowspanCnt = programTd.get('rowspan')

#         if rowspanCnt:
#             # print(rowspanCnt)

#             # time title programID?
#             timeStrList = programTd.select("span > span")
#             timeStr = ""
#             if timeStrList:
#                 # print(timeStrList[0].text)
#                 timeStr = timeStrList[0].text

#             programTitleList = programTd.select("span > a")
#             programTitle = ""
#             if programTitleList:
#                 # print(programTitleList[0].text)
#                 programTitle = programTitleList[0].text
            
#             trList.append([rowspanCnt, timeStr, programTitle])

#             # for timeStr in timeStrList:
#             #     print(timeStr.text)
#             # for titleStr in programTitleList:
#             #     print(titleStr.text)
#             #     print(titleStr.get('href'))

#             # programStr += programTd.text + "\n"
#             # print(programTd.text)
# print(trList)
# with open("ex3.html", mode="w") as f:
#    f.write(str(programStr))
