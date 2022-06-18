def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    prices = {}
    for i, dict in enumerate(data):
        prices[i] = dict['price']
    
    results = []
    while limit != 0:
        maxIndex = list(prices.values()).index(max(list(prices.values())))
        results.append(data[maxIndex])
        data.remove(data[maxIndex])
        del prices[maxIndex]
        limit -= 1

    return results

print(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

"""
>>> a
[{'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]

>>> sorted(a, key=lambda x: x['price']) 
[{'name': 'water', 'price': 1}, {'name': 'meat', 'price': 15}, {'name': 'bread', 'price': 100}, {'name': 'wine', 'price': 138}]

>>> sorted(a, key=lambda x: x['price'], reverse=True)
[{'name': 'wine', 'price': 138}, {'name': 'bread', 'price': 100}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}]
"""