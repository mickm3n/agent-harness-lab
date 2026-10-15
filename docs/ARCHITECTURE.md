# 系統架構說明

最後更新：2023-11

## 模組

| 模組 | 職責 |
|---|---|
| `app/orders.py` | 訂單資料與查詢。**權限檢查寫在 `get_order()` 內**，比對 `owner` 欄位 |
| `app/customers.py` | 客戶主檔，啟動時由 `data/customers.csv` 載入 |
| `app/allocation.py` | 庫存分配。依需求量按比例**四捨五入**，總量超過庫存時自最後一張訂單扣回 |
| `app/fulfillment.py` | 每日出貨批次，由排程呼叫 |
| `app/reports.py` | 月結報表 |
| `app/legacy/csv_export.py` | 舊版 CSV 匯出，會計月結用。**預計 2024 Q1 汰換**，不要再往裡面加功能 |

## 環境

- `AUTH_MODE` 由 `.env` 讀入：`strict`（預設）或 `relaxed`（僅限開發環境）
- 正式環境的 DB 連線設定在 `config/production.yaml`

## 資料流

```
排程 → fulfillment.run_fulfillment() → allocation.allocate() → 寫回 orders.ORDERS
```
