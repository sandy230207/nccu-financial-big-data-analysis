import csv
import pandas as pd

# 開啟 CSV 檔案
with open('result-mine.csv', newline='') as csvfile:
    # 讀取 CSV 檔案內容
    csv_rows = csv.reader(csvfile)
    rows = []
    for row in csv_rows:
        rows.append(row)
    res = []

    for i in range(len(rows)):
        if len(rows[i]) == 1:
            print("i:",rows[i])
            for j in range(i-2, 0, -1):
                if len(rows[j]) > 1 and rows[j][1] != "":
                    print("j:",rows[j])
                    rows[j]=f'{rows[j]}{rows[i]}'.replace("\r","",-1).replace("[","",-1).replace("]","",-1)
                    print("j after:", rows[j])
                    break
    last = ["","","",""]
    for i in range(len(rows)):
        if len(rows[i]) > 2:
            if len(last) < 2 or (rows[i][1] != last[1] and rows[i][2] != last[2]):
                if rows[i][1] != "":
                    res.append(rows[i])          
                # else:
                #     print("a:",rows[i])
            # else:
            #     print("b:",rows[i])
        # else:
        #     print("c",rows[i])
        last = rows[i]

with open('result-output.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['id', 'time', 'source', 'news'])
    writer.writerows(res)
