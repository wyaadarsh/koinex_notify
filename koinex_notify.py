import json
import requests
import os
import time
response = requests.get('https://koinex.in/api/ticker')
json_data = json.loads(response.text)
prices = json_data['prices']
stats  = json_data['stats']
coins=['BTC','ETH','LTC','BCH','XRP']

def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

def BuySell(stat_coin):
    low = float(stat_coin['min_24hrs'])
    last = float(stat_coin['last_traded_price'])
    high = float(stat_coin['max_24hrs'])
    diff_low = (last - low)/last
    diff_high = (high - last)/last
    if diff_low < 0.25:
        return 1
    elif diff_high < 0.25:
        return 2
    else:
        return 3

while True:
    for i in range(len(coins)):
        decision = BuySell(stats[coins[i]])
        if decision == 1:
            notify(coins[i],"BUY", prices[coins[i]])
            time.sleep(200)
        elif decision == 2:
            notify(coins[i],"SELL", prices[coins[i]])
            time.sleep(200)
        else:
            time.sleep(100)