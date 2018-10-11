#Yongxuan Fu ID：15065638 ICS 32A
#This module implements the various outputs as a separate class.

import open_map_quest


class Steps:
    def result(self,dic:dict) ->list:
        '''
            Printing the directions
        '''
        self._dic = dic
        self._steps = ['DIRECTIONS']
        for loc in self._dic['route']['legs']:
            for dirct in loc['maneuvers']:
                self._steps.append(dirct['narrative'])

        return self._steps


class TotalDistance:
    def __init__(self):
        '''Initializes a TotalDistance with a count of zero'''
        self._total = 0

    def result(self,dic:dict) ->list:
        '''
            Printing the total distance which is a integer
        '''
        self._distance = []
        
        self._total += int(round(dic['route']['distance']))        
        self._distance.append('TOTAL DISTANCE: '+ str(self._total) + ' miles')

        return self._distance


class TotalTime:
    def __init__(self):
        '''Initializes a TotalTime with a count of zero'''
        self._total = 0
        self._time =[]
        
    def result(self,dic:dict) ->list:
        '''
            Printing the total time which is a integer
        '''
        
        time = dic['route']['time']
        self._total += int(round(time/60))
        self._time.append('TOTAL DISTANCE: '+ str(self._total) + ' minutes')
        return self._time

class Latlong:
    def result(self,dic:dict) ->list:
        '''
            Printing the latitude and longitude in format
        '''
        self._latlong_list = ['LATLONGS']
        self._loc_list = dic['route']['locations']
        
        for num in self._loc_list:
            n = num['latLng']['lat']
            if  n<0:
                self._lat = str("%.2f" % -n) +'S'
            elif n>0:
                self._lat = str("%.2f" % n) +'N'
            elif n == 0:
                self._lat = 0
            
            y = num['latLng']['lng']

            if y < 0:
                self._lng = str("%.2f" % -y) + 'W'
            elif y>0:
                self._lng = str("%.2f" % y) +'E'
            elif y == 0:
                self._lng = 0
            self._latlong_list.append(self._lat + ' ' + self._lng)

        return self._latlong_list

    

class Elevation:
    def result(self,dic:dict) ->list:
        '''
            Printing the elevation which is a integer in ft
            Printing error if there is getting wrong
        '''
        self._elevation_list = ['ELEVATIONS']
        for num in dic['route']['locations']:
            self._lat_list = []
            self._lat_list.append(num['latLng']['lat'])
            self._lat_list.append(num['latLng']['lng'])
            #Building elevation url
            elevation_url = open_map_quest.build_elevation_url(self._lat_list)
            elevation_response =open_map_quest.http_request(elevation_url)
            for x in elevation_response['elevationProfile']:
                self._elevation_list.append(int(round(x['height'])))

        return self._elevation_list
            
                                              
def run(outputs_list:[str],route_response:dict) ->None:
    '''
        This private function is used Duck typing and display the specific
        outputs
    '''
    #Building a dict for connecting to class
    class_out = {'STEPS':'Steps','TOTALDISTANCE':'TotalDistance',
                 'TOTALTIME':'TotalTime','LATLONG':'Latlong',
                 'ELEVATION':'Elevation'}    
    
    for output in outputs_list:
        #Getting result by call the class
        response_list = eval(class_out[output]+'()').result(route_response)
        for line in response_list:
            print(line)

        print()
    

        

