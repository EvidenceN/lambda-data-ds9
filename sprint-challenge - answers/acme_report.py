import random
from random import randint, sample, uniform
from acme import Product
import math

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    '''
    generate a given number of products (default
  30), randomly, and return them as a list
  '''
    products = []
    adjectives_sample = random.sample(adjectives, 1)
    nouns_sample = random.sample(nouns, 1)
    name = f'{adjectives_sample} {nouns_sample}'

    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    flammability = random.uniform(0.0, 2.5)

    prod = Product(
        name=name,
        price=price,
        weight=weight,
        flammability=flammability
    )

    products_list = [prod.name, prod.price, prod.weight, prod.flammability]

    products.append(products_list * num_products)

    return products


def inventory_report(products):
    '''
    takes a list of products, and prints a "nice" summary
    '''
    for name in products:
        count = []
        if name not in count:
            count.append(name)
        num_unique_products = len(count)
    return num_unique_products

    unique_products = num_unique_products

    average_price = sum(products.price)/len(products.price)

    average_weight = sum(products.weight)/len(products.weight)

    average_flammability = sum(products.flammability)/len(products.flammability)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {unique_products}')

    print(f'Average Price: {average_price}')

    print(f'Average Weight: {average_weight}')

    print(f'Average Flammability: {average_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
