#!/usr/local/bin

"""
We need to calculate the daily sales of each product, but our DB is overloaded, and we're writing an endpoint that already has the 
info for orders and products loaded up so we can do it directly in code.


Sample input data (language-agnostic):

products = [
    Product(id=1, name='product_2.5', price_in_usd=2.5),
    Product(id=2, name='product_3.5', price_in_usd=3.5),
    Product(id=3, name='product_5', price_in_usd=5),
]

orders = [
    Order(id=1, product_id= 1, purchased_at='2019-02-24'),
    Order(id=2, product_id=1, purchased_at='2019-02-24'),
    Order(id=3, product_id=1, purchased_at='2019-02-24'),
    Order(id=5, product_id=1, purchased_at='2019-02-23'),
    Order(id=6, product_id=2, purchased_at='2019-02-23'),
    Order(id=7, product_id=2, purchased_at='2019-02-23'),
]
```


Sample output

| date       | product_name | amount |
| ---------- | ------------ | ------ |
| 2019-02-24 | product_2.5  | 7.5    |
| 2019-02-24 | product_3.5  | 0.0    |
| 2019-02-24 | product_5    | 0.0    |
| 2019-02-23 | product_2.5  | 2.5    |
| 2019-02-23 | product_3.5  | 7.0    |
| 2019-02-23 | product_5    | 0.0    |
"""

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price_in_usd: float

@dataclass
class Order:
    id: int
    product_id: int
    purchased_at: str

def main():
    # daily sales of each product 

    products = [
    Product(id=1, name='product_2.5', price_in_usd=2.5),
    Product(id=2, name='product_3.5', price_in_usd=3.5),
    Product(id=3, name='product_5', price_in_usd=5),
]

    orders = [
    Order(id=1, product_id= 1, purchased_at='2019-02-24'),
    Order(id=2, product_id=1, purchased_at='2019-02-24'),
    Order(id=3, product_id=1, purchased_at='2019-02-24'),
    Order(id=5, product_id=1, purchased_at='2019-02-23'),
    Order(id=6, product_id=2, purchased_at='2019-02-23'),
    Order(id=7, product_id=2, purchased_at='2019-02-23'),
    ]
    """
    Sample output

    | date       | product_name | amount |
    | ---------- | ------------ | ------ |
    | 2019-02-24 | product_2.5  | 7.5    |
    | 2019-02-24 | product_3.5  | 0.0    |
    | 2019-02-24 | product_5    | 0.0    |
    | 2019-02-23 | product_2.5  | 2.5    |
    | 2019-02-23 | product_3.5  | 7.0    |
    | 2019-02-23 | product_5    | 0.0    |
    """
    # we need a lookup of product id to name
    product_lookup = {}

    for p in products:
        product_lookup[p.id] = (p.name, p.price_in_usd)

    # we want to print orders per day per product including zeroes
    report = {}

    for o in orders:
        # we key per day since we are going to report per day
        d = o.purchased_at
        product_name = product_lookup[o.product_id][0]
        if report.get(d) is None:
            report[d] = {}
            for p in product_lookup.keys():
                name = product_lookup[p][0]
                report[d][name] = 0.0
        #print (report)
        #print (product_name)
        report[d][product_name] += product_lookup[o.product_id][1]
    
   
    for d in report.keys():
        for k in report[d]:
            print ("{0}, {1}, {2}".format(d,k,report[d][k]))









if __name__=="__main__":
    main()
