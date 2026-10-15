import pytest

from app.orders import get_order


def test_contract_shape():
    order = get_order(1, "alice")
    assert {"id", "owner", "total"} <= set(order.keys())


def test_contract_total_is_int():
    assert isinstance(get_order(1, "alice")["total"], int)


def test_contract_denial_uses_permission_error():
    """docs/api.md：拒絕存取一律用 PermissionError，不可回傳 None 或 False。"""
    with pytest.raises(PermissionError):
        get_order(2, "alice")
