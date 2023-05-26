def min_coins(coins):
    heads = coins.count("heads")
    tails = coins.count("tails")
    return min(heads, tails)

coins = ["heads", "heads", "tails", "heads", "tails", "tails", "tails"]
print(min_coins(coins))
