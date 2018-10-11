#Yongxuan Fu ID：15065638 ICS 32A
#This module reads the input and constructs the objects that will generate
#the program's output.

import outputs
import open_map_quest


def _get_input() ->list:
    '''
        This private function gather the inputs and return a list of them.
    '''
    location_num = int(input())
    location_list = []
    for x in range(location_num):
        location_list.append(input())

    outputs_num = int(input())
    outputs_list = []
    for x in range(outputs_num):
        outputs_list.append(input())
        
    return location_list,outputs_list

    
def user_inter():
    '''
    This function is the user interface and run the main programs.
    It will gather the inputs and display the specific outputs
    '''
    
    location_list,outputs_list = _get_input()

    try:
        route_response = open_map_quest.http_request(open_map_quest.build_route_url(location_list))
        #If there is an error the statuscode will no be 0
        if route_response['info']['statuscode'] ==0:
            outputs.run(outputs_list,route_response)
        #No route error when statuscode equal 402 or 612
        elif route_response['info']['statuscode'] in(402,612):
            print('\nNO ROUTE FOUND\n')
        else:
            print('\nMAPQUEST ERROR\n')
    #If there is a error occur when requst http. It will print error in
    #open_map_quest module and end the function
    except:
       pass    
    
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')



if __name__ == '__main__':
    user_inter()
