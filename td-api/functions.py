
def unusualHunter(response):
    responseJson = response.json()

    # Create list to store flagged options
    unusualList = []
    class Signal:
        def __init__(self, stock, date, strike, typeOpt, volume, openInterest):
            self.stock = stock
            self.date = date
            self.strike = strike
            self.type = typeOpt
            self.volume = volume
            self.openInterest = openInterest
            # self.side = side
        def __repr__(self):  
            return "%s Dt:% s  Strike:% s % s  Vol:%s  OI:%s  " % (self.stock, self.date, self.strike, self.type, self.volume, self.openInterest)  
    # Iterate through Calls
    for (k,v) in responseJson['callExpDateMap'].items():
        for (k2,v2) in v.items():
            for k3 in v2:
                # Conditions for Unusual
                if (k3["totalVolume"] >= 500 and k3["totalVolume"] > (3 * k3["openInterest"]) and (k3["delta"] > 0.6 or k3["delta"] < 0.4)):
                    print('Unusual Flagged')
                    unusualList.append(Signal(responseJson['symbol'], k, k2, 'C', k3["totalVolume"], k3["openInterest"]))
    # Iterate through Puts
    for (k,v) in responseJson['putExpDateMap'].items():
        # print(k) this is the Date
        for (k2,v2) in v.items():
            # print(k2 + '\n')  this is the Strike
            for k3 in v2:
                if (k3["totalVolume"] >= 500 and k3["totalVolume"] > (3 * k3["openInterest"]) and (k3["delta"] < (-0.6) or k3["delta"] > (-.4))):
                    print('Unusual Flagged')
                    unusualList.append(Signal(responseJson['symbol'], k, k2, 'P', k3["totalVolume"], k3["openInterest"]))

    return unusualList