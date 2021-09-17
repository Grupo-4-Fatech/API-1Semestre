from  flask import Response, request
from flask_restful import Resource
from satsearch import Search
from satstac import Item
import json
import requests

class CatRequest(Resource):
    def post(self):
        body = request.get_json()
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
        print(body)
        cloud = "eo:cloud_cover<" + "5"#body['cloud']
        time = "2018-02-01/2018-02-10"#body["time"]
        
        search = Search(intersects=geom,
                        time=time,
                        property=[cloud])
        items = search.items()
        print(search.found())
        
        for item in items:
            print(item.assets["thumbnail"]["href"])
        return 200

