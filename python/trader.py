def execute_trade(signal, crypto='BTC', amount=100):
    if signal == 1:
        print(f"Buying ${amount} of {crypto}")
    elif signal == 0:
        print(f"Selling ${amount} of {crypto}")
