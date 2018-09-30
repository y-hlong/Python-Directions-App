#Yin Hao Long 49256403
import MapQuest_API_Functions
import Class_Generators

def main():
    '''
    runs all functions
    '''
    user_inputs = get_user_input()
    if user_inputs != None:
        print_outputs(user_inputs)

def print_outputs(user_inputs: list):
    '''
    This function prints out all the outputs that are specified by the user
    '''
    url_dictionary = MapQuest_API_Functions.url_to_dictionary(MapQuest_API_Functions.create_direction_url(user_inputs[0]))
    if url_dictionary != None:
        STEPS = Class_Generators.steps_generator()
        TOTALDISTANCE = Class_Generators.total_distance_generator()
        TOTALTIME = Class_Generators.total_time_generator()
        LATLONG = Class_Generators.latlng_generator()
        ELEVATION = Class_Generators.elevation_generator()
        possible_outputs = {'STEPS': STEPS, 'TOTALDISTANCE': TOTALDISTANCE, 'TOTALTIME': TOTALTIME, 'LATLONG': LATLONG, 'ELEVATION': ELEVATION}
        for x in user_inputs[1]:
            if x in possible_outputs:
                print('')
                possible_outputs[x].display_info(url_dictionary)
            else:
                print('\nInput Error')
                return
        print('\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')
    else:
        return
    
def get_user_input()-> list:
    '''
    This function gets the user's input and stores them in a list
    '''
    try:
        print('How many locations?')
        location_amount = int(input())
        if int(location_amount) < 2 :
            print('\nInput Error')
            return
        locations_list = []
        for x in range(0, location_amount):
            locations_list.append(input())
        output_amount = int(input())
        if output_amount < 1:
            print('\nInput Error')
            return
        output_list = []
        for x in range(0, output_amount):
            output_list.append(input())
        return [locations_list, output_list]
    except:
        print('\nInput Error')
        return

if __name__ == '__main__':
    main()
