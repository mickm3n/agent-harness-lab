"""客戶與員工資料。

角色（role）：
- customer：一般客戶，只能看自己的訂單
- staff：倉儲／客服人員
- admin：系統管理員
"""

CUSTOMERS = {
    "alice": {"role": "customer", "region": "north"},
    "bob": {"role": "customer", "region": "south"},
    "carol": {"role": "staff", "region": "north"},
    "root": {"role": "admin", "region": None},
}


def get_role(user):
    """回傳使用者角色；查無此人回傳 None。"""
    record = CUSTOMERS.get(user)
    return record["role"] if record else None
