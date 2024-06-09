test = int(input("Enter the number of stocks: "))
for i in range(test):
    stock_cmp = float(input("Enter the CMP of the Stock: "))
    inv = float(input("Enter the investment: "))
    margin = stock_cmp / 5
    print(f"Number of shares: {int(inv / margin)}")

