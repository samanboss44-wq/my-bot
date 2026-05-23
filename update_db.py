import requests
from bs4 import BeautifulSoup
import json
import re

def get_price(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        price_tag = soup.find('span', class_='price')
        if price_tag:
            price_text = re.sub(r'\D', '', price_tag.text)
            return int(price_text) if price_text else 0
    except: return 0
    return 0

# لیست محصولاتی که می‌خواهید اتوماتیک آپدیت شوند
data = {
    "whey": [
        {"name": "پروتئین وی گلد استاندارد", "url": "https://mesterfit.me/product/on-whey-gold-standard/"},
        {"name": "پروتئین وی کوین لورون", "url": "https://mesterfit.me/product/kevin-levrone-whey/"}
    ]
}

# آپدیت قیمت‌ها
for cat in data:
    for item in data[cat]:
        item['price'] = get_price(item['url'])
        item.pop('url') # حذف لینک برای تمیز شدن فایل نهایی

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)