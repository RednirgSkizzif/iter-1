exec(open("settings.py").read())


# print(json.dumps(getQuotes('AAPL'), indent=2))

SECRET_KEY = os.getenv("IEX_SECRET")

# IEX specific code:

data = {
  '2020-02-28': {'open': 257.26, 'high': 278.41, 'low': 256.37, 'close': 273.36, 'volume': 106721230}, 
  '2020-03-02': {'open': 282.28, 'high': 301.44, 'low': 277.72, 'close': 298.81, 'volume': 85349339}
}

closing_prices = np.array([])

i  = 0
for x in data:
  print(data[list(data)[i]]['close'])
  closing_prices = np.append(closing_prices, data[list(data)[i]]['close'])
  i = i+1

print(ta.SMA(closing_prices, 2))
# now i have sma data or a rolling period, 2 days rn
