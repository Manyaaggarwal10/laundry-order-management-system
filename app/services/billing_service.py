from app.utils.pricing import PRICE_MAP

def calculate_total(garments):
    total = 0

    for item in garments:
        name = item.get("type")
        qty = item.get("quantity", 0)

        price = PRICE_MAP.get(name, 0)
        total += price * qty

    return total