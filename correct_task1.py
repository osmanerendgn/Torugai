def calculate_average_order_value(orders):

    if not orders:
        return 0.0
    valid_orders = [o for o in orders if o.get("status") != "cancelled"]

    if not valid_orders:
        return 0.0

    total = sum(order["amount"] for order in valid_orders)
    count = len(valid_orders)
    return total / count
