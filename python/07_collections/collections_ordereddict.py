"""
HackerRank Chanllenge: collections.OrderedDict() (Python)
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

Print a dictionary of items that retains its order.
"""

from collections import OrderedDict

products = OrderedDict()

for _ in range(int(input())):
    name, price = input().rsplit(maxsplit=1)
    products[name] = products.get(name, 0) + int(price)

for item in products.items():
    print(*item)