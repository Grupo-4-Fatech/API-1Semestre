import urllib.request, json

from pymongo import MongoClient
client = MongoClient('mongodb+srv://piAdmin:pi1234@cluster0-vpcqm.gcp.mongodb.net/test?retryWrites=true&w=majority', 27017)

db = client['metadata']
collection_currency = db['landsat']


def getImages():
    i = 1
    info = {1:{'collection': '','scene_id': '','datetime': '','cloud_cover': '' ,'column': '','row': '', 'href': ''}}
    cursor = collection_currency.find({})
    for document in cursor:
        if "010/022" in document['links'][0]['href'] and int(document['properties']['eo:cloud_cover']) < 20:
            info[i] = {}
            info[i]['collection'] = document['properties']['collection']
            info[i]['scene_id'] = document['properties']['landsat:scene_id']
            info[i]['datetime'] = document['properties']['datetime']
            info[i]['cloud_cover'] = document['properties']['eo:cloud_cover']
            info[i]['column'] = document['properties']['eo:column']
            info[i]['row'] = document['properties']['eo:row']

            with urllib.request.urlopen(document['links'][0]['href']) as url:
                data = json.loads(url.read().decode())
                print(data['assets']['thumbnail']['href'])
                info[i]['href'] = data['assets']['thumbnail']['href']
                i = i + 1
                with open("test.txt", "a") as myfile:
                    myfile.write(data['assets']['thumbnail']['href'] + "\n")
    print(info)
    return info
    with open("my.json","w") as f:
        json.dump(info,f)
