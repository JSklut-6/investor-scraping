import os
from anthropic import Anthropic

api_key = open(".env").read().split("ANTHROPIC_API_KEY=")[1].split()[0]
client = Anthropic(api_key=api_key)

property_data = {
    "address": "123 Main St, Dallas, TX 75201",
    "purchase_price": 250000,
    "arv": 350000,
    "rehab_cost": 50000,
    "property_type": "Single Family",
    "bedrooms": 3,
    "bathrooms": 2,
    "market_rent": 2200
}

prompt = f"""Analyze this property for Prophet Homes:
- Address: {property_data['address']}
- Purchase: ${property_data['purchase_price']:,}
- ARV: ${property_data['arv']:,}
- Rehab: ${property_data['rehab_cost']:,}

Give: 1) Recommendation 2) ROI 3) Risks"""

print("Analyzing...")
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=[{"role": "user", "content": prompt}]
)

print("="*80)
print(response.content[0].text)
print("="*80)
