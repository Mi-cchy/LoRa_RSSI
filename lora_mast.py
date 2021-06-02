# -*- coding: utf-8 -*-
import time
import csv

import lora_setting



# LoRa送受信用クラス（受信したらRSSIを送り返す）
class LoraMastClass:

    def __init__(self, lora_device, channel):
        self.mastDevice = lora_setting.LoraSettingClass(lora_device)
        self.channel = channel

    # ES920LRデータ送受信メソッド
    def lora_Mast(self):
        # LoRa初期化
        self.mastDevice.reset_lora()
        # LoRa設定コマンド　ここの設定が必要
        set_mode = ['1', 'd', self.channel, 'e', '0001', 'f', '0002', 'g', '0001',
                    'n', '2', 'l', '2', 'p', '1', 'y', 'z']
        # LoRa設定
        self.mastDevice.setup_lora(set_mode)
        # LoRa(ES920LR)受信待機
        while True:
            try:
                #キーボードでloraとの距離を入力
                distance = input('distance:')

                 #データ50回送信
                data = 'aaaa'
                print('<-- SEND -- [ {} ]'.format(data))

                for i in range(50):
                     self.mastDevice.cmd_lora('{}'.format(data))
                
                time_sta = time.time()

                #20s 受信継続
                rssi_list = ["rssi"]
                data_list = ["data"]
                while (time.time() - time_sta) < 20:

                    if self.mastDevice.device.inWaiting() > 0:
                        try:
                            line = self.mastDevice.device.readline()
                            line = line.decode("utf-8")
                        except Exception as e:
                            print(e)
                            continue
                        print(line)
                        if line.find('RSSI') >= 0 and line.find('information') == -1:
                            log = line
                            log_list = log.split('):Receive Data(')
                            # 受信電波強度
                            rssi = log_list[0][5:]
                            print(rssi)
                            # 受信フレーム
                            data = log_list[1][:-3]
                            print(data)
                            rssi_list.append(rssi)
                            data_list.append(data)
                            if len(rssi_list) > 50:
                                break
                
                with open("stock.csv", "w", encoding='utf-8') as f: # 文字コードをShift_JISに指定
                    writer = csv.writer(f, lineterminator='\n') # writerオブジェクトの作成 改行記号で行を区切る
                    writer.writerow(rssi_list) # csvファイルに書き込み
                    writer.writerow(data_list)
   
    
                           


                    # ES920LRモジュールから値を取得
                     
                     

               
                        
            except KeyboardInterrupt:
                self.mastDevice.close()
                
