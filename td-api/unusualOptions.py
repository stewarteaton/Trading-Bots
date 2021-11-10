from tda import auth, client
import json
import config
import datetime as dt

try:
    c = auth.client_from_token_file(config.TOKEN_PATH, config.API_KEY)
except FileNotFoundError:
    from selenium import webdriver
    with webdriver.Chrome(executable_path='/Users/stewarteaton/Desktop/td-api/chromedriver') as driver:
        c = auth.client_from_login_flow(
            driver, config.API_KEY, config.REDIRECT_URL, config.TOKEN_PATH)

# start_date = dt.datetime.strptime('2021-03-10', '%Y-%m-%d').date()
start_date = dt.datetime.today()
end_date = dt.datetime.strptime('2022-12-29', '%Y-%m-%d').date()
tickerList = ['FUTU', '', 'SNAP', 'UPST', 'TQQQ', 'AMD', 'TMDX', 'TSLA', 'NIO', 'QQQ']
unusualList = []
for ticker in tickerList:
    response = c.get_option_chain(ticker, contract_type=c.Options.ContractType.ALL,from_date=start_date, to_date=end_date)

    # print(json.dumps(response.json(), indent=4))
    responseJson = response.json()

    # Create list to store flagged options
    # unusualList = []
    class Signal:
        def __init__(self, stock, date, strike, typeOpt, volume, openInterest, dollars, side):
            self.stock = stock
            self.date = date
            self.strike = strike
            self.type = typeOpt
            self.volume = volume
            self.openInterest = openInterest
            self.dollars = dollars
            self.side = side
        def __repr__(self):  
            return "%s Dt:% s  Strike:% s % s  Vol:%s  OI:%s  $:%s % s" % (self.stock, self.date, self.strike, self.type, self.volume, self.openInterest, self.dollars, self.side)  
    # Iterate through Calls
    boughtSold = "undecided"
    for (k,v) in responseJson['callExpDateMap'].items():
        for (k2,v2) in v.items():
            for k3 in v2:
                # Conditions for Unusual
                dollarVolume = round(k3["totalVolume"] * k3["mark"] * 100)
                if (k3["totalVolume"] >= 500 and k3["totalVolume"] > (5 * k3["openInterest"]) and (k3["delta"] > 0.65 or k3["delta"] < 0.35) and dollarVolume > 200000):
                    # print('Unusual Flagged')
                    if (k3["bidSize"] > 3 * k3["askSize"]):
                        boughtSold = "bought"
                    elif (3 * k3["bidSize"] < k3["askSize"]):
                        boughtSold = "sold"
                    unusualList.append(Signal(responseJson['symbol'], k, k2, 'C', k3["totalVolume"], k3["openInterest"], dollarVolume, boughtSold))

    # Iterate through Puts
    for (k,v) in responseJson['putExpDateMap'].items():
        # print(k) this is the Date
        for (k2,v2) in v.items():
            # print(k2 + '\n')  this is the Strike 
            for k3 in v2:
                dollarVolume = round(k3["totalVolume"] * k3["mark"] * 100)
                if (k3["totalVolume"] >= 500 and k3["totalVolume"] > (5 * k3["openInterest"]) and (k3["delta"] < (-0.65) or k3["delta"] > (-.35)) and dollarVolume > 200000):
                    # print('Unusual Flagged')
                    if (k3["bidSize"] > 3 * k3["askSize"]):
                        boughtSold = "bought"
                    elif (3 * k3["bidSize"] < k3["askSize"]):
                        boughtSold = "sold"
                    unusualList.append(Signal(responseJson['symbol'], k, k2, 'P', k3["totalVolume"], k3["openInterest"], dollarVolume, boughtSold))

for signal in unusualList:
    print(signal)


        # print(str(v2))
# x = responseJson['callExpDateMap']['2021-03-12:2']['1000.0'][0]["totalVolume"]
# print("Volume: " + json.dumps(x,indent=4))


# for key in responseJson:
#     item = responseJson[key]
#     for key2 in item:
#         print(item[key2])
# for (k,v) in responseJson.items():
#     print("Key: " + k)
#     print("Value: " + str(v))