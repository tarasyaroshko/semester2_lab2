'''
map.py
'''
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster
import locations
def get_coordinates(place):
    '''
    returns coordinates of place
    >>> get_coordinates('Kyiv, Ukraine')
    (49.841952, 24.0315921)
    '''
    if not place:
        return None
    try:
        geolocator = Nominatim(user_agent="followers_map")
        location = geolocator.geocode(place)
        coordinates = (location.latitude, location.longitude)
        return coordinates
    except AttributeError:
        return get_coordinates(','.join(place.split(',')[1:]))


def create_map(followers):
    '''
    creates the map with markers of films
    '''
    map = folium.Map(location = [50.4500336, 30.5241361], zoom_start = 2)
    fg = folium.FeatureGroup(name="Followers Locations")
    markers = folium.FeatureGroup(name = "Markers")
    # for name, coords in dct.items():
    #     fg.add_child(folium.Marker(location = [coords[0], coords[1]], popup = name, icon = folium.Icon()))
    #     markers.add_child(folium.CircleMarker(location = [coords[0], coords[1]], radius = 15, color = "orange", fill_color = "orange"))
    # def main(username):
    # info = get_info_API(f'https://api.twitter.com/2/users/by/username/{username}')
    # id = info['data']['id']
    # followers = get_followers(f'https://api.twitter.com/2/users/{id}/following')
    # print(followers)
    # coordinates = {}
    # for follower in followers['data']:
    #     try:
    #         place = get_coords(follower['location'])
    #         if place != None:
    #             if place not in coordinates:
    #                 coordinates[place] = [follower['name']]
    #             else:
    #                 coords[place].append(follower['name'])
    #             pprint(coords)
    #     except KeyError:
    #         continue
    # map = folium.Map()
    # markers_of_followers = folium.FeatureGroup(name=f" of {info['data']['name']}")
    # for i in coords:
    #     markers_of_followers.add_child(folium.Marker(location=[follower[0], follower[1]], popup=',\n\n'.join(coordinates[follower]), icon=folium.Icon()))
    # map.add_child(markers_of_followers)
    # map.add_child(folium.LayerControl())
    # map.save('templates/Map.html')
    # return render_template('Map.html')
    # map.add_child(fg)
    # map.add_child(markers)
    # map.add_child(folium.LayerControl())
    # map.save('Map.html')
    # print(friends)
    # group=folium.FeatureGroup(name='Friends')
    # mapp.add_child(group)
    # marker_cluster = MarkerCluster().add_to(group)
    for follower in followers:
        name = follower[0]
        location = get_coordinates(follower[1])
        if not location:
            continue
        fg.add_child(folium.Marker(location=location, popup=name+', '+ follower[1],icon=folium.Icon(color='darkblue', icon_color='white', icon='male')))
        markers.add_child(markers.add_child(folium.CircleMarker(location = location, radius = 15, color = "orange", fill_color = "orange")))
    map.add_child(fg)
    map.add_child(markers)
    map.add_child(folium.LayerControl())
    map.save('Map.html')

if __name__=='__main__':
    create_map(locations.get_friends_locations('FabrizioRomano'))
