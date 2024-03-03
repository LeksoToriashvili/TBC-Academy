import datetime
from forex_python.bitcoin import BtcConverter

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
spent = float(input("Enter amount of money in USD: "))

buy_date = datetime.date(year, month, day)

btc = BtcConverter()

btc_amount = spent/btc.get_previous_price("USD", buy_date)
current_usd = btc_amount * btc.get_latest_price("USD")

print(f"Profit is: {current_usd-spent} USD")