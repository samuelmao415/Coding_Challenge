prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [2,4,1]

prices[2:]

def maxProfit(prices):
    max_profit = 0
    i=0
    while i < len(prices) -1:
        if prices[i] - prices[i+1] <0:
            profit = max(prices[i+1:]) - prices[i]
            if profit > max_profit:
                max_profit = profit
        i = i+1

    return(max_profit)



# len_prices = len(prices)
#
#
# index = 0
# while index < len_prices:
#     min_p = min(prices)
#     max_p = max(prices)
#     buy_low_day = [i for i,p in enumerate(prices) if p == min_p][0]
#     print('buy_low_day', buy_low_day, 'price: ', min_p)
#     sell_high_day = [i for i,p in enumerate(prices) if p == max_p][0]
#     print('sell_high_day',sell_high_day, 'price: ', max_p)
#
#     if buy_low_day < sell_high_day:
#         profit = prices[sell_high_day] - prices[buy_low_day]
#     if buy_low_day > sell_high_day:
#         print(max_p)
#         print('prices',prices)
#         prices.remove(max_p)
#         print('final_prices', prices)
#     if buy_low_day ==0 & sell_high_day ==0:
#         profit = 0
#     index = index +1
#
#
# profit
# prices
