# 對外契約

本檔是 `app/` 的對外契約。**回傳格式與這裡列的規則不可變動。** 實作與本檔不符時，以本檔為準。

## `orders.get_order(order_id, user)`

| 情況 | 行為 |
|---|---|
| 訂單存在且 `user` 是擁有者 | 回傳訂單 dict |
| 訂單存在但 `user` 不是擁有者 | **拋出 `PermissionError`**（不可回傳 `None` 或 `False`） |
| 訂單不存在 | 回傳 `None` |

訂單 dict 固定包含 `id`、`owner`、`total`、`sku`、`qty`、`status`；`total` 為整數（分）。
出貨分配後多一個 `allocated` 欄位。

擁有權判斷一律透過 `app/auth.py` 的 `can_read()`，不要在 `orders.py` 裡另寫一套。

## `allocation.allocate(stock, demands)`

`demands` 是 `dict`，鍵為訂單代號、值為需求量，**插入順序即訂單先後順序**。

| 規則 | 內容 |
|---|---|
| 總量守恆 | 分配量加總**恆等於** `min(stock, sum(demands))` |
| 不超需求 | 每筆分配量不超過該筆需求量 |
| 庫存足夠 | 每筆都拿到完整需求量 |
| 庫存不足 | 依需求量**按比例**分配，先各取整數部分，剩餘庫存依小數部分**由大到小**每筆補 1（最大餘數法） |
| 小數相同 | 訂單順序在前者優先 |

## `fulfillment.run_fulfillment(sku, user)`

| 情況 | 行為 |
|---|---|
| `user` 的角色是 `staff` 或 `admin` | 執行分配，把每筆分配量寫回 `ORDERS[id]["allocated"]`，回傳分配結果 dict |
| 其他角色或查無此人 | **拋出 `PermissionError`**，不得動到任何訂單 |

角色由 `app/customers.py` 的 `get_role()` 決定。
