# -*- coding: utf-8 -*-
# 舊的 CSV 匯出，給會計月結用。2019 年寫的，沒有測試。
# 每個月 1 號會有人手動跑，跑完把檔案寄給會計。
import os
import csv

from app.orders import ORDERS

EXPORT_DIR = "/var/exports"  # 匯出目錄，正式環境是 NAS 掛載點


def export(month, path=None):
    # 匯出指定月份的訂單（其實沒有依月份過濾，全部匯出）
    if path == None:
        path = EXPORT_DIR + "/orders-" + month + ".csv"
    f = open(path, "w")
    w = csv.writer(f)
    w.writerow(["id", "owner", "total"])
    for k in ORDERS:
        o = ORDERS[k]
        w.writerow([o["id"], o["owner"], o["total"]])
    f.close()
    # 備份一份到 backup 目錄，NAS 上的舊檔會被覆蓋
    os.system("cp " + path + " " + path + ".bak")
    return path
