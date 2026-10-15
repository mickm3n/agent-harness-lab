"""出貨分配：把現有庫存分給待出貨（pending）的訂單。"""

from app.allocation import allocate
from app.orders import ORDERS

# 目前庫存。正式環境由 WMS 同步（見 docs/ARCHITECTURE.md）。
STOCK = {"widget": 10, "gadget": 3}


def pending_demands(sku):
    """回傳某個 SKU 所有待出貨訂單的需求量，依訂單 id 排序。"""
    return {
        oid: o["qty"]
        for oid, o in sorted(ORDERS.items())
        if o["sku"] == sku and o["status"] == "pending"
    }


def run_fulfillment(sku, user):
    """執行一次出貨分配，把分配量寫回各訂單的 allocated 欄位並回傳分配結果。"""
    demands = pending_demands(sku)
    plan = allocate(STOCK.get(sku, 0), demands)
    for oid, qty in plan.items():
        ORDERS[oid]["allocated"] = qty
    return plan
