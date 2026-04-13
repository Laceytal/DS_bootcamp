import sys

def all_stocks():
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

    raw_input = sys.argv[1]

    for i in range(0, len(raw_input)):
        if "," + i*" " + "," in raw_input:
            return


    expressions = [expr.strip() for expr in raw_input.split(",")]

    for expr in expressions:
        if not expr:
            return

        expr_lower = expr.lower()

        company_match = None
        for name, ticker in COMPANIES.items():
            if name.lower() == expr_lower:
                company_match = name
                print(f"{name} stock price is {STOCKS[ticker]}")
                break

        if company_match:
            continue

        ticker_match = None
        for name, ticker in COMPANIES.items():
            if ticker.lower() == expr_lower:
                ticker_match = ticker
                print(f"{ticker.upper()} is a ticker symbol for {name}")
                break

        if ticker_match:
            continue

        print(f"{expr} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    all_stocks()
