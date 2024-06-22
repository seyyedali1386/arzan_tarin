import urllib.request
from bs4 import BeautifulSoup

# لیست 10 ارز دیجیتال برتر
crypto_list = [
    "BTC",
    "ETH",
    "USDT",
    "USDC",
    "BNB",
    "XRP",
    "ADA",
    "SOL",
    "DOT",
    "DOGE"
]
def get_coinranking_price(symbol):
    url = f"https://coinranking.com/{symbol.lower()}"
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
    except urllib.error.URLError:
        return None

    soup = BeautifulSoup(html, 'lxml')
    price_element = soup.find('span', class_='price')
    if price_element:
        return float(price_element.text.strip().replace(',', ''))
    else:
        return None

def get_coinmarketcap_price(symbol):
    url = f"https://coinmarketcap.com/currencies/{symbol.lower()}/"
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
    except urllib.error.URLError:
        return None

    soup = BeautifulSoup(html, 'lxml')
    price_element = soup.find('span', class_='price')
    if price_element:
        return float(price_element.text.strip().replace(',', ''))
    else:
        return None

# مقایسه قیمت ها
for symbol in crypto_list:
    coinranking_price = get_coinranking_price(symbol)
    coinmarketcap_price = get_coinmarketcap_price(symbol)

    # تعیین ارزان ترین سایت
    cheapest_price = min(coinranking_price, coinmarketcap_price) if coinranking_price and coinmarketcap_price else None
    cheapest_site = "CoinRanking" if cheapest_price == coinranking_price else "CoinMarketCap" if cheapest_price == coinmarketcap_price else None

    print(f"{symbol}:")
    print(f"  CoinRanking: {coinranking_price:.2f}")
    print(f"  CoinMarketCap: {coinmarketcap_price:.2f}")
    if cheapest_price:
        print(f" arzan tarin site: {cheapest_site} ({cheapest_price:.2f})")
    else:
        print("gheimat ha da dast ras nist!")
    print("-" * 20)