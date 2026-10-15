from app import fulfillment
from app.orders import ORDERS


def test_pending_demands_only_includes_pending_orders_of_that_sku():
    assert fulfillment.pending_demands("widget") == {1: 5, 2: 4, 3: 2}


def test_run_fulfillment_writes_allocation_back_to_orders():
    plan = fulfillment.run_fulfillment("widget", "carol")
    assert sum(plan.values()) == fulfillment.STOCK["widget"]
    for oid, qty in plan.items():
        assert ORDERS[oid]["allocated"] == qty
