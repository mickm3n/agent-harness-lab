"""訂單查詢。"""

from app.auth import can_read

# 記憶體內的假資料。正式環境由 DB 載入（見 docs/ARCHITECTURE.md）。
ORDERS = {
    1: {"id": 1, "owner": "alice", "total": 1200, "sku": "widget", "qty": 5, "status": "pending"},
    2: {"id": 2, "owner": "bob", "total": 850, "sku": "widget", "qty": 4, "status": "pending"},
    3: {"id": 3, "owner": "alice", "total": 400, "sku": "widget", "qty": 2, "status": "pending"},
    4: {"id": 4, "owner": "bob", "total": 300, "sku": "gadget", "qty": 1, "status": "shipped"},
}


def get_order(order_id, user):
    """回傳指定訂單；非擁有者拋出 PermissionError；不存在回傳 None。"""
    order = ORDERS.get(order_id)
    if order is None:
        return None
    if not can_read(order, user):
        raise PermissionError(f"{user} cannot read order {order_id}")
    return order


def list_orders(user):
    """回傳 user 擁有的所有訂單，依 id 排序。"""
    return [o for oid, o in sorted(ORDERS.items()) if o["owner"] == user]
