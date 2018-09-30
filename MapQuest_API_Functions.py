#Yin Hao Long 49256403
from collections import namedtuple
import json
import urllib.parse
import urllib.request

def create_direction_url(locations: list) -> str:
    '''
    This function takes in a list of places, from start to end, and constructs the url that inputs the locations
    into the MapQuest API.
    '''
    location_parameters = []
    location_parameters.append(('from', locations[0]))
    directions_url = 'http://open.mapquestapi.com/directions/v2/route?key=G4dEUTHxgCgc30aPM5WxqUhqaSbVW3xS&'
    for x in range(len(locations)):
        if x != 0:
            location_parameters.append(('to', locations[x]))
    directions_url = directions_url  + urllib.parse.urlencode(location_parameters) 
    return directions_url

def create_elevation_url(latlng_pairs: list):
    '''
    Takes in a list of of latlng coordinates
    and finds the elevation at a pair of latitudinal and longitudinal coordinates.
    '''
    elevation_url = 'http://open.mapquestapi.com/elevation/v1/profile?key=G4dEUTHxgCgc30aPM5WxqUhqaSbVW3xS&unit=f&shapeFormat=raw&latLngCollection='
    for x in latlng_pairs: 
        elevation_url = elevation_url + str(x) + ','
    return elevation_url
    
def url_to_dictionary(url: str) -> dict:
    '''
    Formats the info received from url, and puts it into a dictionary.
    Also handles errors in cases where a route is not found or a JSON format is not returned due to other errors.
    '''
    predictionary_text = None

    try:
        predictionary_text = urllib.request.urlopen(url)
        json_text = predictionary_text.read().decode(encoding = 'utf-8')
        if json.loads(json_text)['info']['statuscode'] != 0:
            print('')
            print('NO ROUTE FOUND')
            return
        return json.loads(json_text)
    except:
        print('')
        print('MAPQUEST ERROR')
        return
    finally:
        if predictionary_text != None:
            predictionary_text.close()
            
