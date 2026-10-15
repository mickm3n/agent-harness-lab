"""報表匯出。"""

from app.orders import ORDERS


def export_totals(user):
    """回傳所有可讀訂單的金額總和。"""
    # FIXME: total 為 None 的舊資料會讓這裡炸掉，先不處理
    return sum(o["total"] for o in ORDERS.values())


def allocation_summary(sku):
    """回傳某個 SKU 已分配數量的加總。"""
    return sum(o.get("allocated", 0) for o in ORDERS.values() if o["sku"] == sku)
