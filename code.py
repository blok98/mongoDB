import json
from pprint import pprint
from pymongo import MongoClient

client             = MongoClient('mongodb://localhost:27017')
db                 = client['mijndb']
collection_student = db['products']
data               = collection_student.find()

def data_list():
    data_list=[]
    for value in data:
        data_list.append(value)
    return data_list

def customer_info():
    customerNumber      = 1
    customer_info    = data_list[0]
    name                = customer_info['name']
    selling_price       = customer_info['price']['selling_price']
    return name,selling_price

def name_with_R():
    naamMetR='geen naam gevonden'
    for value in data_list:
        name        = value['name']
        if name[0] == 'R':
            naamMetR= name
            break
    return naamMetR

def average_price():
    totPrice=0
    count=0
    for value in data_list:
        count+=1
        selling_price = value['price']['selling_price']
        totPrice +=selling_price
    average=totPrice/count
    return average


data_list=data_list()
print(customer_info())
print(name_with_R())
print(average_price())
