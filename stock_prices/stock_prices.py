#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy_price = prices[0]
  buy_index = prices.index(buy_price)

  sell_price = None
  # sell_index = prices.index(sell_price)

  profit = 0

  for i in range(buy_index, len(prices) - 1):
    if prices[i] < buy_price:
      buy_price = prices[i]
    for j in range(1, len(prices)):
      if not sell_price:
        if prices[j] > buy_price:
          sell_price = prices[j]
      else:
        if sell_price < prices[j] > buy_price:
          sell_price = prices[j]
      
  
  print(buy_price)
  print(sell_price)

  profit = sell_price - buy_price
  return profit

find_max_profit([1050, 270, 1540, 3800, 2])

# THIS IS PASSING THE FIRST COUPLE TESTS, BUT IS NOT COMPLETE.

# def find_max_profit(prices):
#   buy_price = prices[0]
#   sell_price = buy_price
#   profit = 0

#   for i in range(0, len(prices)):
#     if prices[i] < buy_price:
#       buy_price = prices[i]
#       print("Buy price: ", i, buy_price)
#     for j in range(1, len(prices)):
#       if prices[j] > buy_price and prices[j] > sell_price:
#         sell_price = prices[j]
#         print("Sell price: ", sell_price)

#   if sell_price == prices[0]:
#     profit -= buy_price
#   else:
#     profit = sell_price - buy_price
  
#   return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))