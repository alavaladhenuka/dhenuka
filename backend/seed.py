from datetime import date, timedelta
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.inventory import InventoryItem
from app.models.order import Order

Base.metadata.create_all(bind=engine)
db = SessionLocal()

db.query(InventoryItem).delete()
db.query(Order).delete()

# Full 20 Inventory Products
grocery_items = [
    InventoryItem(product_name="Fortune Sunlite Sunflower Oil 1L", product_code="OIL-01", quantity=25, quality="GOOD", expiry_date=date.today() + timedelta(days=180), aisle_location="Aisle A1"),
    InventoryItem(product_name="Saffola Gold Cooking Oil 1L", product_code="OIL-02", quantity=15, quality="GOOD", expiry_date=date.today() + timedelta(days=120), aisle_location="Aisle A1"),
    InventoryItem(product_name="Amul Pure Ghee 1L Tin", product_code="GHEE-01", quantity=40, quality="GOOD", expiry_date=date.today() + timedelta(days=200), aisle_location="Aisle A2"),
    InventoryItem(product_name="Aashirvaad Shuddh Chakki Atta 10kg", product_code="ATTA-01", quantity=30, quality="GOOD", expiry_date=date.today() + timedelta(days=90), aisle_location="Aisle B1"),
    InventoryItem(product_name="Fortune Chakki Fresh Atta 5kg", product_code="ATTA-02", quantity=20, quality="GOOD", expiry_date=date.today() + timedelta(days=60), aisle_location="Aisle B1"),
    InventoryItem(product_name="Tata Sampann Toor Dal 1kg", product_code="DAL-01", quantity=18, quality="GOOD", expiry_date=date.today() + timedelta(days=180), aisle_location="Aisle B3"),
    InventoryItem(product_name="Tata Sampann Moong Dal 1kg", product_code="DAL-02", quantity=22, quality="GOOD", expiry_date=date.today() + timedelta(days=150), aisle_location="Aisle B3"),
    InventoryItem(product_name="Clinic Plus Shampoo 650ml", product_code="SHMP-01", quantity=14, quality="GOOD", expiry_date=date.today() + timedelta(days=500), aisle_location="Aisle C1"),
    InventoryItem(product_name="Dove Intense Repair Shampoo 650ml", product_code="SHMP-02", quantity=12, quality="GOOD", expiry_date=date.today() + timedelta(days=400), aisle_location="Aisle C1"),
    InventoryItem(product_name="Dettol Soap 125g (Pack of 4)", product_code="SOP-01", quantity=50, quality="GOOD", expiry_date=date.today() + timedelta(days=700), aisle_location="Aisle C2"),
    InventoryItem(product_name="Lux Rose Soap 150g", product_code="SOP-02", quantity=35, quality="GOOD", expiry_date=date.today() + timedelta(days=650), aisle_location="Aisle C2"),
    InventoryItem(product_name="Tata Salt Iodized 1kg", product_code="SPC-01", quantity=100, quality="GOOD", expiry_date=date.today() + timedelta(days=800), aisle_location="Aisle D1"),
    InventoryItem(product_name="MDH Red Chilli Powder 200g", product_code="SPC-02", quantity=45, quality="GOOD", expiry_date=date.today() + timedelta(days=240), aisle_location="Aisle D1"),
    InventoryItem(product_name="India Gate Basmati Rice 5kg", product_code="RCE-01", quantity=16, quality="GOOD", expiry_date=date.today() + timedelta(days=365), aisle_location="Aisle B5"),
    InventoryItem(product_name="Maggi Masala Noodles 420g", product_code="SNK-01", quantity=60, quality="GOOD", expiry_date=date.today() + timedelta(days=120), aisle_location="Aisle E1"),
    InventoryItem(product_name="Lays Salted Potato Chips 50g", product_code="SNK-02", quantity=80, quality="GOOD", expiry_date=date.today() + timedelta(days=60), aisle_location="Aisle E1"),
    InventoryItem(product_name="Britannia Good Day Biscuits 600g", product_code="SNK-03", quantity=40, quality="GOOD", expiry_date=date.today() + timedelta(days=90), aisle_location="Aisle E2"),
    InventoryItem(product_name="Coca-Cola Original 1.25L", product_code="BEV-01", quantity=28, quality="GOOD", expiry_date=date.today() + timedelta(days=90), aisle_location="Beverage Cooler"),
    InventoryItem(product_name="Nescafe Classic Coffee 100g", product_code="BEV-02", quantity=25, quality="GOOD", expiry_date=date.today() + timedelta(days=365), aisle_location="Aisle E3"),
    InventoryItem(product_name="Surf Excel Detergent 1kg", product_code="CLN-01", quantity=32, quality="GOOD", expiry_date=date.today() + timedelta(days=700), aisle_location="Aisle F1")
]

db.add_all(grocery_items)

demo_orders = [
    Order(product_code="OIL-01", requested_qty=2, distance_km=5.0, priority="HIGH", status="PENDING"),
    Order(product_code="ATTA-01", requested_qty=1, distance_km=12.0, priority="HIGH", status="ALLOCATED"),
    Order(product_code="SHMP-01", requested_qty=3, distance_km=18.0, priority="MEDIUM", status="PICKED"),
    Order(product_code="DAL-01", requested_qty=4, distance_km=25.0, priority="MEDIUM", status="PACKED"),
    Order(product_code="BEV-01", requested_qty=6, distance_km=40.0, priority="LOW", status="DISPATCHED"),
    Order(product_code="SOP-01", requested_qty=2, distance_km=3.5, priority="HIGH", status="PENDING"),
    Order(product_code="RCE-01", requested_qty=1, distance_km=8.0, priority="HIGH", status="ALLOCATED"),
    Order(product_code="CLN-01", requested_qty=2, distance_km=15.0, priority="MEDIUM", status="PICKED")
]

db.add_all(demo_orders)
db.commit()
print("20 Inventory Items & Demo Orders Seeded Successfully!")
db.close()