import sys
def stock_prices():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) != 2:
        return
    company_input = sys.argv[1].lower()

    ticker = None
    for name, code in COMPANIES.items():
        if code.lower() == company_input:
            ticker = name
            break

    if ticker:

        print(ticker, STOCKS[company_input.upper()])
    else:
        print("Unknown company")


if __name__ == '__main__':
    stock_prices()