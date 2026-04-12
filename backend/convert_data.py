import json
import pandas as pd
from datetime import datetime

# Load JSON
with open("price_history.json") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean price (make sure it's number)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Parse timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Save CSV
df.to_csv("price_history.csv", index=False)
print(f"✅ CSV created! {len(df)} records")
print(df.head())