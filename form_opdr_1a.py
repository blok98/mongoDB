import json
from pprint import pprint
from pymongo import MongoClient

client             = MongoClient('mongodb://localhost:27017')
db                 = client['mijndb']
collection_student = db['products']
data               = collection_student.find()

customerNumber      = 1
customer_info    = data[0]


name                = customer_info['name']
selling_price       = customer_info['price']['selling_price']

print('name: ',name)
print('selling_price: ', selling_price)


totPrice=0
count=0
for value in data:
    count+=1
    name          =  value['name']
    selling_price =  value['price']['selling_price']
    totPrice      += selling_price
    if name[0]    == 'R':
        naamMetR  =  name

avPrice           = totPrice/count
print('\n')
print('eerste naam met R: ',naamMetR)
print('\n')
print('gemiddelde prijs van producten: ',avPrice)

