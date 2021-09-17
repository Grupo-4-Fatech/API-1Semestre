from satstac import Catalog, Collection, Item
import urllib.request, json
from pymongo import MongoClient
client = MongoClient('mongodb+srv://piAdmin:pi1234@cluster0-vpcqm.gcp.mongodb.net/test?retryWrites=true&w=majority', 27017)

db = client['metadata']
collection_currency = db['landsat']
cat = Catalog.open('https://landsat-stac.s3.amazonaws.com/landsat-8-l1/catalog.json')
print(cat)
#print(data)
#test
# create a Catalog object with JSON
#mycat = Catalog(data)
#https://landsat-stac.s3.amazonaws.com/landsat-8-l1/ LC80101172015002LGN00
col = Collection.open('https://landsat-stac.s3.amazonaws.com/landsat-8-l1/catalog.json')
print(col, col.extent)
#print(col.items())
i=1
def populateDatabase():
    for item in col.items():
        print(item)
        #item2 = Item.open(item)
        #print(item2)
        row = item.properties['eo:row']
        column = item.properties['eo:column']
        data = item.properties['datetime']
        data = data[0:10]
        id = str(item)
        url = f'https://landsat-stac.s3.amazonaws.com/landsat-8-l1/{column}/{row}/{data}/{id}.json'
        test = Collection.open(url)
        test.save('mycat/catalog' + str(i) +'.json')
        with open('mycat/catalog' + str(i) +'.json') as json_file:
            test2 = json.load(json_file)
        test2['_id'] = test2['id']
        del test2['id']
        del test2['assets']
        with open('mycat/catalog' + str(i) +'.json', 'w') as outfile:
            json.dump(test2, outfile)
        
        with open('mycat/catalog'+  str(i)  + '.json') as f:
            file_data = json.load(f)
        collection_currency.insert(file_data)
        print(url)
        i = i + 1
    client.close()

populateDatabase()