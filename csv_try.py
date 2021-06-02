# -*- coding: utf-8 -*-
import csv

rssi_list = ["rssi"]
data_list = ["data"]

position = input("position(m):")
rssi_list.append(position + "m")
data_list.append(position + "m")

for i in range(50):
    rssi_list.append(str(i))
    data_list.append(str(50-i))

for i in range(2):
    with open("stock.csv", "a", encoding='utf-8') as f: # 文字コードをShift_JISに指定
        writer = csv.writer(f, lineterminator='\n') # writerオブジェクトの作成 改行記号で行を区切る
        writer.writerow(rssi_list) # csvファイルに書き込み
        writer.writerow(data_list)



print("rssi:",rssi_list)