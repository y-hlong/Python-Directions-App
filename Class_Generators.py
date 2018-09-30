#Yin Hao Long 49256403
import MapQuest_API_Functions

class steps_generator:
    def find_directions(self, n):
        '''
        This method takes in a dictionary and searchs for the directions and puts it into a list.
        '''
        list_of_directions = []
        for x in n['route']['legs']:
            for y in x['maneuvers']:
                list_of_directions.append(y['narrative'])
        return list_of_directions

    def display_info(self, n):
        '''
        Takes a list  of directions and prints them out in sequence.
        '''
        print('DIRECTIONS')
        list_of_directions = self.find_directions(n)
        for x in list_of_directions:
            print(x)

class total_distance_generator:
    def display_info(self, n):
        '''
        This method takes in a dictionary
        and searchs for and displays the total distance traveled in miles.
        '''
        print('TOTAL DISTANCE: ' + str(int(round(n['route']['legs'][0]['distance']))) + ' miles')

class total_time_generator:
    def display_info(self, n):
        '''
        This method takes in a dictionary
        and searchs for and displays the total time in minutes rounded to the nearest minute.
        '''
        print('TOTAL TIME: ' + str(int(round(n['route']['legs'][0]['time']/60))) + ' minutes')

class latlng_generator:
    def find_latlng(self, n):
        '''
        This method takes in a dictionary
        and searchs for latlng coordinates and stores them in a 2D list.
        '''
        list_of_lat = []
        list_of_lng = []
        for x in n['route']['locations']:
            list_of_lat.append(x['latLng']['lat'])
            list_of_lng.append(x['latLng']['lng'])
        return [list_of_lat, list_of_lng]

    def format_latlng_bearings(self, n):
        '''
        This method takes in a 2d list of coordinates
        and formats it in such a way that it has bearings rather than +,-.
        '''
        bearings_lat = self.find_latlng(n)[0]
        bearings_lng = self.find_latlng(n)[1]
        for x in range(len(bearings_lat)):
            if bearings_lat[x] < 0:
                bearings_lat[x] = str(round(-bearings_lat[x], 2)) +'S'
            else:
                bearings_lat[x] = str(round(bearings_lat[x], 2)) +'N'
            if bearings_lng[x] < 0:
                bearings_lng[x] = str(round(-bearings_lng[x], 2)) +'W'
            else:

                bearings_lat[x] = str(round(bearings_lng[x], 2)) +'E'
        return [bearings_lat, bearings_lng]
    
    def display_info(self, n):
        '''
        This method takes in a dictionary
        and prints out the latlong with bearings.
        '''
        latlong = self.format_latlng_bearings(n)
        print('LATLONGS')
        for x in range(len(latlong[0])):
            print('{} {}'.format(latlong[0][x], latlong[1][x]))

class elevation_generator:
     def find_latlng(self, n):
        '''
        This method takes in a dictionary
        and searchs for latlng coordinates and stores them in a 2D list.
        '''
        list_of_lat = []
        list_of_lng = []
        for x in n['route']['locations']:
            list_of_lat.append(x['latLng']['lat'])
            list_of_lng.append(x['latLng']['lng'])
        return [list_of_lat, list_of_lng]
            
     def display_info(self, n):
        '''
        This method takes in a dictionary
        and prints out the elevations.
        '''
        print('ELEVATIONS')
        all_latlng = self.find_latlng(n)
        for x in range(len(all_latlng[0])):
            temp_latlng_set = []
            temp_latlng_set.append(all_latlng[0][x])
            temp_latlng_set.append(all_latlng[1][x])
            print(int(round(MapQuest_API_Functions.url_to_dictionary(MapQuest_API_Functions.create_elevation_url(temp_latlng_set))['elevationProfile'][0]['height'])))
