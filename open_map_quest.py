#Yongxuan Fu ID:15065638 ICS 32A
#This module interacts with the Open MapQuest APIs.

import json
import urllib.parse
import urllib.request
import urllib.error

BASE_DIRECTION_URL = 'http://open.mapquestapi.com/directions/v2/route'

BASE_ELEVATION_URL = 'http://open.mapquestapi.com/elevation/v1/profile'

KEY = 'SpG3Q6TvQiMAsAfyFE7M1J8FiwHVnHTm'

def build_route_url(location_list:list) ->str:
    '''
    This function takes locations, and builds and returns a URL that can be used
    to ask the Open route API for information about routes between the locations.
    '''
    
    query_parameter =[('key',KEY),('from',location_list[0])]
    for location in location_list[1:]:
        query_parameter.append(('to',location))
    
    return BASE_DIRECTION_URL + '?' + urllib.parse.urlencode(query_parameter)

def build_elevation_url(latlong_list:list) ->str:
    '''
    This function takes string of latlongs, and builds and returns a URL that
    can be used to ask the Open Elevation API for information about elevation
    profile about the latlongs.
    '''
    
    lat_lng_parameter =['latLngCollection']
    collection =''
    for n in latlong_list:
        #In order to get latLngCollection parameter
        collection += str(n)+','
    lat_lng_parameter.append(collection)
    query_parameter =[('key',KEY),('unit','f')]
    query_parameter.append(tuple(lat_lng_parameter))

    return BASE_ELEVATION_URL + '?' + urllib.parse.urlencode(query_parameter)


def http_request(url:str) ->dict:
    '''
    This function takes a URL and returns a Python dictionary response.
    '''
    try:
        response = None
        response = urllib.request.urlopen(url)
        dict_data = json.load(response)
        return dict_data
    #If there is a error occur when requst http. It will print error.
    except urllib.error.URLError:
        print('\nERROR: get http request failed\n')
    finally:
        if response !=None:
            response.close()

    
