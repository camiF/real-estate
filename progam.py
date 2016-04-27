import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_from_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print("Real state app")


def get_data_from_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'Sacramentorealestatetransactions.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases =[]
        for row in reader:
            #print(type(row), row)
            p = Purchase.create_from_dict(row)
            purchases.append(p)
        return purchases

        #print(purchases[0].__dict__)


        # header = fin.readline().strip()
        # reader = csv.reader(fin)
        # for row in reader:
        #     print(row)

# def load_file(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('header: '+header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#         print(lines[:5])

# def get_price(p):
#     return p.price


def query_data(data):
    #data sorted by price:
    #data.sort(key=get_price)
    data.sort(key=lambda p: p.price)


    #most expensive house
    high_purchase = data[-1]
    print('{:,}'.format(high_purchase.price))

    #least expensive house
    low_purchase = data[0]
    print('{:,}'.format(low_purchase.price))

    #average price house
    # prices=[]
    # for pur in data:
    #     prices.append(pur.price)
    #
    # --------------------------------
    prices = [
        # (p.price, p.beds, p.city)
        p.price
        for p in data
        ]

    ave_price = statistics.mean(prices)
    print("{:,}".format(int(ave_price)))

    #average house of two bedroom house
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)
    #
    #--------------------------------
    #data data list comprehension
    two_beds_homes =[
        p
        for p in data
        if p.beds == 2
    ]
    ave_price = statistics.mean(p.price for p in two_beds_homes)
    ave_baths = statistics.mean(p.baths for p in two_beds_homes)
    ave_sq_ft = statistics.mean(p.sq__ft for p in two_beds_homes)
    print("Average 2 bedroom home is {:,}, baths={}, sq_ft={}".format(int(ave_price), round(ave_baths, 1), round(ave_sq_ft, 1)))


if __name__ == '__main__':
    main()