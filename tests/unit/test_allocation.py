from app.allocation import allocate


def test_enough_stock_everyone_gets_full_demand():
    assert allocate(100, {"a": 30, "b": 20}) == {"a": 30, "b": 20}


def test_shortage_allocates_all_stock():
    result = allocate(10, {"a": 5, "b": 4, "c": 2})
    assert sum(result.values()) == 10


def test_shortage_split():
    assert allocate(10, {"a": 5, "b": 4, "c": 2}) == {"a": 5, "b": 4, "c": 1}
