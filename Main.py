from __future__ import division
from pprint import pprint as pp
from Distance import *
from GeoCoding import *
from Optimise import *
from FileManagement import *
from Functions import *
from Time import *
from operator import itemgetter


# Start Arrays

location_results = []
duration_results_one = []
duration_results_two = []



# Builds a list of location details from various sources

def get_location_details(list_of_locations):
    for x in list_of_locations:
        location_one = x
        for x in list_of_locations:
            location_two = x

            google_result = distance_google(location_one, location_two)
            haversine_result = distance_haversine(location_one, location_two)
            mapbox_result = time_mapbox_matrix(location_one, location_two)

            location_results.append(google_result)
            location_results[-1]['Haversine_distance'] = haversine_result
            location_results[-1]['Mapbox_time'] = mapbox_result

            google_distance = location_results[-1]["distance"]
            haversine_google_diff = haversine_google_difference(haversine_result, google_distance)
            location_results[-1]['Haversine_Google_Distance_Diff'] = haversine_google_diff

            google_time = location_results[-1]['duration']
            mapbox_google_diff = abs(google_time - int(mapbox_result))
            location_results[-1]['Mapbox_Google_Distance_Diff'] = mapbox_google_diff

    return location_results



# Compares Google and Map Box AIP Durations

def get_durations(list_of_locations):

    for x in list_of_locations:
        location_one = x
        for x in list_of_locations:
            location_two = x

            list = []
            durations = time_calculator()

            google_duration = durations.get_duration_google(location_one, location_two)
            mapbox_duration = time_mapbox_matrix(location_one, location_two)

            list.append(google_duration)
            list.append(mapbox_duration)

            google_mapbox_diff = abs(int(google_duration) - int(mapbox_duration))
            list.append(google_mapbox_diff)

            if mapbox_duration and google_duration is not 0:
                list.append(round((google_mapbox_diff / ((mapbox_duration + google_duration)/2))*100, 1))
            else:
                list.append("n/a")

            duration_results_one.append(list)

            for result in duration_results_one:
                if "n/a" in result:
                    duration_results_one.remove(result)

            sorted_duration_results = sorted(duration_results_one, key=itemgetter(3))

        headers = []

        headers.append("Google Duration")
        headers.append("Mapbox Duration")
        headers.append("Duration Difference")
        headers.append("Percentage Difference")
        sorted_duration_results.insert(0, headers)

    return sorted_duration_results


# Finds the shortest and longest duration between two locations

def shortest_longest_duration(list_of_locations):

    for x in list_of_locations:
        location_one = x
        for x in list_of_locations:
            location_two = x

            list = []
            durations = time_calculator()

            google_duration = durations.get_duration_google(location_one, location_two)
            mapbox_duration = time_mapbox_matrix(location_one, location_two)
            graph_hopper_duration = durations.get_duration_graph_hopper(location_one, location_two)

            list.append(google_duration)
            list.append(mapbox_duration)
            list.append(graph_hopper_duration)

            duration_results_two.append(list)

    headers = []

    headers.append("Google Duration")
    headers.append("Mapbox Duration")
    headers.append("Graph Hopper Duration")
    duration_results_two.insert(0, headers)

    return duration_results_two

read_file()
result = shortest_longest_duration(places)
create_csv(result)




















