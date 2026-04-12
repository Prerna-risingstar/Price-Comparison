import json
from datetime import datetime, timedelta
import pandas as pd
import random

print("🔥 Creating MULTI-MONTH data (Jan-Dec)...")

data = []
products = ["iPhone 15", "MacBook Air", "Samsung Galaxy", "Sony Headphones"]
sites = ["Amazon", "Flipkart", "Google"]

# Generate 12 MONTHS of data
for month in range(1, 13):  # Jan to Dec
    for day in range(1, 28):  # 1-27 each month
        for hour in [8, 12, 18, 22]:  # Morning, Noon, Evening, Night
            for product in products:
                for site in sites:
                    # Monthly price trends (lower in festive months)
                    base_price = random.randint(5000, 80000)
                    month_factor = 1.0
                    if month in [10, 11, 12]:  # Oct-Dec = festive discounts
                        month_factor = 0.85
                    elif month in [1, 2]:  # Jan-Feb = clearance
                        month_factor = 0.9
                    
                    price = int(base_price * month_factor * random.uniform(0.85, 1.15))
                    
                    timestamp = datetime(2024, month, day, hour, random.randint(0,59))
                    
                    data.append({
                        "query": product,
                        "site": site,
                        "price": max(1000, price),
                        "timestamp": timestamp.isoformat(),
                        "title": f"{product} - {site}"
                    })

print(f"✅ Created {len(data)} records (12 months!)")

# 🔥 FIXED: Convert timestamp BEFORE saving CSV
df = pd.DataFrame(data[:2000])  # 2000 records
df['timestamp'] = pd.to_datetime(df['timestamp'])  # ✅ FIX 1
df['price'] = pd.to_numeric(df['price'])           # ✅ FIX 2

df.to_csv("price_history.csv", index=False)
print("🎉 Multi-month CSV ready!")
print("\n📅 Months covered:", sorted(df['timestamp'].dt.month.unique()))
print(df.head())