"""庫存分配。

當庫存不足以滿足所有訂單時，依各訂單需求量按比例分配，
餘數的處理方式見 docs/api.md。
"""


def allocate(stock, demands):
    """將 stock 分配給 demands（dict: 訂單代號 -> 需求量）。

    回傳 dict: 訂單代號 -> 實際分配量。
    """
    total = sum(demands.values())
    if total <= stock:
        return dict(demands)

    result = {name: round(stock * qty / total) for name, qty in demands.items()}

    # 四捨五入後可能超過庫存，從最後一筆往前扣回
    over = sum(result.values()) - stock
    for name in reversed(list(result)):
        if over <= 0:
            break
        take = min(over, result[name])
        result[name] -= take
        over -= take
    return result
