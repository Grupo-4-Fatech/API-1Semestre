from satsearch import Search
from satstac import Item

search = Search(bbox=[-110, 39.5, -105, 40.5])
print('bbox search: %s items' % search.found())

search = Search(time='2018-02-12T00:00:00Z/2018-03-18T12:31:12Z')
print('time search: %s items' % search.found())

search = Search(query={'eo:cloud_cover': {'lt': 10}})
print('cloud_cover search: %s items' % search.found())

search = Search(bbox=[-110, 39.5, -105, 40.5],
               time='2018-02-12T00:00:00Z/2018-03-18T12:31:12Z',
               query={'eo:cloud_cover': {'lt': 10}})
print('%s items' % search.found())

geom = {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -66.3958740234375,
          43.305193797650546
        ],
        [
          -64.390869140625,
          43.305193797650546
        ],
        [
          -64.390869140625,
          44.22945656830167
        ],
        [
          -66.3958740234375,
          44.22945656830167
        ],
        [
          -66.3958740234375,
          43.305193797650546
        ]
      ]
    ]
}

search = Search(intersects=geom)
print('intersects search: %s items' % search.found())


query = {
  "eo:cloud_cover": {
    "lt": 10
  },
  "collection": {
    "eq": "landsat-8-l1"
  }
}

search = Search(query=query)
print('%s items found' % search.found())

search = Search.search(property=["eo:cloud_cover<10", "collection=landsat-8-l1"])
print('%s items found' % search.found())

# or use collection shortcut
search = Search.search(collection='landsat-8-l1', property=["eo:cloud_cover<10"])
print('%s items found' % search.found())


#search = Search(bbox=[-110, 39.5, -105, 40.5],
#               datetime='2018-02-01/2018-02-04',
#               property=["eo:cloud_cover<5"])
#print('%s items' % search.found())

items = search.items()
print('%s items' % len(items))
print('%s collections' % len(items._collections))
print(items._collections)

#for item in items:
    #print(item.properties)

items[1].save('test.json')
items2 = Item.load('test.json')

print(items2.summary(['date', 'id', 'eo:cloud_cover']))


# download a specific asset from all items and put in a directory by date in 'downloads'
filenames = items.download('MTL', path='downloads/${date}')

items = search.items(limit=2)
print(items.summary())


#search = Search.search(bbox=[-110, 39.5, -105, 40.5],
#               datetime='2018-02-01/2018-02-10',
#               property=["eo:cloud_cover<50"],
#               collection='landsat-8-l1')
#items = search.items()
print(items.summary())

items.save('test.json')
items2 = items.load('test.json')

print(items2.summary(['date', 'id', 'eo:cloud_cover']))


search = Search.search(bbox=[-110, 39.5, -105, 40.5],
               datetime='2018-02-01/2018-02-10',
               property=["eo:cloud_cover<50"],
               collection='landsat-8-l1')
items = search.items()
print(items.summary())

items.save('test.json')
items2 = items.load('test.json')

print(items2.summary(['date', 'id', 'eo:cloud_cover']))


# download a specific asset from all items and put in a directory by date in 'downloads'
filenames = items.download('MTL', path='downloads/${date}')
print(filenames)



ids = ['LC80340332018034LGN00', 'LC80340322018034LGN00']
search = Search.search(ids=ids, collection='landsat-8-l1')
items = search.items()

print(items.summary())

