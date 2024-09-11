import pandas as pd
import wget 
import os
import zipfile


# 創建raw data 資料夾
folderPath = "rawData"
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
    for year in range(107, 113):
        os.makedirs(f"{folderPath}/{year}")

# 下載資料
with open(file="data_resource.csv", mode="r", encoding="utf-8") as f:
    resource = f.readlines()
    for line in resource:
        url = line.split(": ")
        wget.download(url[1], out=f"{url[0]}.zip")


# 解壓縮原始檔到相對應年份的資料夾
for i in range(107, 113):
    with zipfile.ZipFile(f"{i}年傷亡道路交通事故資料.zip", "r") as zip_ref:
        zip_ref.extractall(f"./rawData/{i}")



# 將107-110 的檔案西元年轉換成民國年
for i in range(107, 111):
    folderpath = f"./rawData/{i}"
    for filename in os.listdir(folderpath):
        if f"{i+1911}" in filename:
            
            # 將西元年換成民國年
            new_filename = filename.replace(f"{i+1911}", f"{i}")
            
            # 建立完整路徑
            old_file = os.path.join(folderpath, filename)
            new_file = os.path.join(folderpath, new_filename)
            
            # 更換檔名
            os.rename(old_file, new_file)


# 把107-112年份A1A2的CSV檔串在一起成新的CSV
for year in range(107, 113):
    merge_data = pd.read_csv(f"./rawData/{year}/{year}年度A1交通事故資料.csv")[:-2]
    for month in range(1, 13):
        data_A2 = pd.read_csv(f"./rawData/{year}/{year}年度A2交通事故資料_{month}.csv")[:-2]
        merge_data = pd.concat([merge_data, data_A2], ignore_index=True)
    
    merge_data.to_csv(f"./rawData/{year}A1A2交通事故資料.csv", index=False)
