import requests 
import json
from math import sin, cos, sqrt, atan2, radians
from yelpapi import YelpAPI
from uszipcode import ZipcodeSearchEngine
import forecastio

API_KEY = 'x'
Client_ID = 'x'

class Route:
    
    def __init__(self,distance,duration):
        self.distance = distance
        self.duration = duration
        self.steps_list = list()
        self.route_score = 0
        
    def add_Step(self,Step):
        self.steps_list.append(Step)
        
    
class Step:
  
    def __init__(self,distance,lat,long,duration,html):
        self.distance = distance
        self.duration = duration
        self.html = html
        self.lat = lat
        self.long = long
        self.foodCount = 0
        
class Shop:
    
    def __init__(self,lat,lng,shop_id):
        self.lat = lat
        self.lng = lng
        self.shop_id = shop_id
        self.visited = False

def get_routes_json(start,end):
    r = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin='+start+'&destination='+end+'&alternatives=true&key=AIzaSyAtIUNwNdWLE_txqk3K0Hoh75EApCofXSM')
    j = r.json();
    return j

def parse_json(json_data):
    count = 0;
    routes_list = [];
    for route in json_data['routes']:
#         num_of_routes = num_of_routes + 1
        for leg in route['legs']:
            route_dist = leg['distance']['value']
            route_dura = leg['duration']['value']
            r = Route(route_dist,route_dura)
            for step in leg['steps']:
                distance = step['distance']['value']
                duration = step['duration']['value']
                lat = step['end_location']['lat']
                long = step['end_location']['lng']
                html = step['html_instructions']
                s = Step(distance,lat,long,duration,html)
                r.add_Step(s)
        routes_list.append(r)
    
    return routes_list

def calculate_distance(lat1,lon1,lat2,lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    
    return distance
    print("Result:", distance)

# set up search for rest based on long and lat
def getCountsForRoute(route):
    uniques = set()
    final = set()
    shops = list()
    yelp_api = YelpAPI(API_KEY)
    search = ZipcodeSearchEngine()
    for step in route.steps_list:
        res = search.by_coordinate(step.lat, step.long, radius=10, returns=5)
        codes = list()
        for zipcode in res:
            codes.append(zipcode.Zipcode)
        searchTerm = "Taco Bell"
        # quick empty check
        if len(codes) > 0:
            search_results = yelp_api.search_query(term=searchTerm,location=codes[0],price="1,2")      
        restCount = 0
        # looks through all the search query results
        for buis in search_results['businesses']:
            if searchTerm in buis['name']:
#                 print(buis['name'])
                if buis['id'] not in uniques:
                    uniques.add(buis['id'])
                    s = Shop(buis['coordinates']['latitude'],buis['coordinates']['longitude'],buis['id'])
                    shops.append(s)
    
        for shop_object in shops:
            for shop_object1 in shops:
                if shop_object.shop_id != shop_object1.shop_id and shop_object.visited == False and shop_object1.visited == False:
                    dist = calculate_distance(shop_object.lat,shop_object.lng,shop_object1.lat,shop_object1.lng)
                    if dist < 10:
                        shop_object.visited = True
        for x in shops:
            if x == False:
                restCount = restCount + 1
        shops = list()
        step.foodCount = restCount
#         print(step.foodCount)
	    print('Route Distance')
	    print((route.distance*3.28084)/5280)
	    print('Route Duration')
	    print(route.duration/3600)
	    
	    print('Total Restaraunts')
	    print(len(uniques))

a = get_routes_json('Seatle','Portland')
routes = parse_json(a)

for rou in routes:
    print('NEW ROUTTTTTE')
    getCountsForRoute(rou)
