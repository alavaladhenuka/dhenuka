from datetime import date

def calculate_expiry_discount(expiry_date: date) -> float:
    if not expiry_date:
        return 0.0
    days_left = (expiry_date - date.today()).days
    if days_left <= 3:
        return 50.0
    elif days_left <= 7:
        return 20.0
    return 0.0

def trigger_out_of_stock_email(product_code: str, quantity: int):
    print(f"[ALERT] Stock low for product {product_code}. Remaining quantity: {quantity}")