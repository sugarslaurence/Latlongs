from pprint import pprint as pp

# Graph Hopper Main

request_one = {
    "objectives": [{
        "type": "min",
        "value": "transport_time"
    }],
    "vehicles": [{
        "vehicle_id": "vehicle1",
        "start_address": {
            "location_id": "home_location_tower_bridge",
            "lon": -0.075338,
            "lat": 51.505597
        },
        "type_id": "vehicle_type_1"
    }],
    "vehicle_types": [{
        "type_id": "vehicle_type_1",
        "profile": "car",
        "capacity": [3]
    }],
    "services": [{
        "id": "1",
        "name": "chelsea_bridge",
        "address": {
            "location_id": "loc_1",
            "lon": -0.149832,
            "lat": 51.484484
        },
        "size": [1]
    }]
}
new_vehicle = {
    'vehicle_id': 'vehicleX',
    'start_address': {'location_id': 'home_location_tower_bridge', 'lon': -0.075338, 'lat': 51.505597},
    'type_id': 'vehicle_type_1'}


def graph_hopper_request_builder(vehicles=3, objective_function='transport_time'):

    default_body = request_one
    default_body['objectives'] = objective_function
    new_vehicle = default_body['vehicles']

    vehicles_list = []

    for x in range(0, vehicles):
        vehicles_list.append(new_vehicle)
    print(pp(vehicles_list[0][0]['vehicle_id']))
    print(type(vehicles_list[0][0]['vehicle_id']))


graph_hopper_request_builder()

# Request Payloads

request_three = {
        "objectives": [{
            "type": "min",
            "value": "vehicles"
        }],
        "vehicles": [{
                "vehicle_id": "vehicle1",
                "start_address": {
                    "location_id": "home_location_tower_bridge",
                    "lon": -0.075338,
                    "lat": 51.505597
                },
                "type_id": "vehicle_type_1"
            },
            {
                "vehicle_id": "vehicle2",
                "start_address": {
                    "location_id": "home_location_tower_bridge",
                    "lon": -0.075338,
                    "lat": 51.505597
                },
                "type_id": "vehicle_type_1"
            }, {
                "vehicle_id": "vehicle3",
                "start_address": {
                    "location_id": "home_location_tower_bridge",
                    "lon": -0.075338,
                    "lat": 51.505597
                },
                "type_id": "vehicle_type_1"
            }, {
                "vehicle_id": "vehicle4",
                "start_address": {
                    "location_id": "home_location_tower_bridge",
                    "lon": -0.075338,
                    "lat": 51.505597
                },
                "type_id": "vehicle_type_1"
            }
        ],
        "vehicle_types": [{
            "type_id": "vehicle_type_1",
            "profile": "car",
            "capacity": [3]
        }],
        "services": [{
                "id": "1",
                "name": "chelsea_bridge",
                "address": {
                    "location_id": "loc_1",
                    "lon": -0.149832,
                    "lat": 51.484484
                },
                "size": [1]
            },
            {
                "id": "2",
                "name": "southwark_bridge",
                "address": {
                    "location_id": "loc_2",
                    "lon": -0.094011,
                    "lat": 51.508902
                },
                "size": [1]
            },
            {
                "id": "3",
                "name": "victoria_park",
                "address": {
                    "location_id": "loc_3",
                    "lon": -0.038972,
                    "lat": 51.536561
                },
                "size": [1]
            },
            {
                "id": "4",
                "name": "hyde_park",
                "address": {
                    "location_id": "loc_4",
                    "lon": -0.165730,
                    "lat": 51.507268
                },
                "size": [1]
            },
            {
                "id": "5",
                "name": "clapham_common",
                "address": {
                    "location_id": "loc_5",
                    "lon": -0.149261,
                    "lat": 51.458452
                },
                "size": [1]
            },
            {
                "id": "6",
                "name": "battersea_park",
                "address": {
                    "location_id": "loc_6",
                    "lon": -0.156498,
                    "lat": 51.479107
                },
                "size": [1]
            },
            {
                "id": "7",
                "name": "",
                "address": {
                    "location_id": "borough",
                    "lon": -0.091522,
                    "lat": 51.503470
                },
                "size": [1]
            },
            {
                "id": "8",
                "name": "westfield_shopping",
                "address": {
                    "location_id": "loc_11",
                    "lon": -0.221122,
                    "lat": 51.507531
                },
                "size": [1]
            }
        ]
    }	# 4 Cars. 8 Services. Min Vehicles
request_four = {
    "objectives": [{
        "type": "min",
        "value": "transport_time"
    }],
    "vehicles": [{
            "vehicle_id": "vehicle1",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        },
        {
            "vehicle_id": "vehicle2",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle3",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle4",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }
    ],
    "vehicle_types": [{
        "type_id": "vehicle_type_1",
        "profile": "car",
        "capacity": [3]
    }],
    "services": [{
            "id": "1",
            "name": "chelsea_bridge",
            "address": {
                "location_id": "loc_1",
                "lon": -0.149832,
                "lat": 51.484484
            },
            "size": [1]
        },
        {
            "id": "2",
            "name": "southwark_bridge",
            "address": {
                "location_id": "loc_2",
                "lon": -0.094011,
                "lat": 51.508902
            },
            "size": [1]
        },
        {
            "id": "3",
            "name": "victoria_park",
            "address": {
                "location_id": "loc_3",
                "lon": -0.038972,
                "lat": 51.536561
            },
            "size": [1]
        },
        {
            "id": "4",
            "name": "hyde_park",
            "address": {
                "location_id": "loc_4",
                "lon": -0.165730,
                "lat": 51.507268
            },
            "size": [1]
        },
        {
            "id": "5",
            "name": "clapham_common",
            "address": {
                "location_id": "loc_5",
                "lon": -0.149261,
                "lat": 51.458452
            },
            "size": [1]
        },
        {
            "id": "6",
            "name": "battersea_park",
            "address": {
                "location_id": "loc_6",
                "lon": -0.156498,
                "lat": 51.479107
            },
            "size": [1]
        },
        {
            "id": "7",
            "name": "",
            "address": {
                "location_id": "borough",
                "lon": -0.091522,
                "lat": 51.503470
            },
            "size": [1]
        },
        {
            "id": "8",
            "name": "westfield_shopping",
            "address": {
                "location_id": "loc_11",
                "lon": -0.221122,
                "lat": 51.507531
            },
            "size": [1]
        }
    ]
}	# 4 Cars. 8 Services. Min Transport Time
request_five = 	{
    "objectives": [{
            "type": "min",
            "value": "vehicles"
        },
        {
            "type": "min",
            "value": "transport_time"
        }
    ],
    "vehicles": [{
            "vehicle_id": "vehicle1",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        },
        {
            "vehicle_id": "vehicle2",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle3",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle4",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }
    ],
    "vehicle_types": [{
        "type_id": "vehicle_type_1",
        "profile": "car",
        "capacity": [3]
    }],
    "services": [{
            "id": "1",
            "name": "chelsea_bridge",
            "address": {
                "location_id": "loc_1",
                "lon": -0.149832,
                "lat": 51.484484
            },
            "size": [1]
        },
        {
            "id": "2",
            "name": "southwark_bridge",
            "address": {
                "location_id": "loc_2",
                "lon": -0.094011,
                "lat": 51.508902
            },
            "size": [1]
        },
        {
            "id": "3",
            "name": "victoria_park",
            "address": {
                "location_id": "loc_3",
                "lon": -0.038972,
                "lat": 51.536561
            },
            "size": [1]
        },
        {
            "id": "4",
            "name": "hyde_park",
            "address": {
                "location_id": "loc_4",
                "lon": -0.165730,
                "lat": 51.507268
            },
            "size": [1]
        },
        {
            "id": "5",
            "name": "clapham_common",
            "address": {
                "location_id": "loc_5",
                "lon": -0.149261,
                "lat": 51.458452
            },
            "size": [1]
        },
        {
            "id": "6",
            "name": "battersea_park",
            "address": {
                "location_id": "loc_6",
                "lon": -0.156498,
                "lat": 51.479107
            },
            "size": [1]
        },
        {
            "id": "7",
            "name": "",
            "address": {
                "location_id": "borough",
                "lon": -0.091522,
                "lat": 51.503470
            },
            "size": [1]
        },
        {
            "id": "8",
            "name": "westfield_shopping",
            "address": {
                "location_id": "loc_11",
                "lon": -0.221122,
                "lat": 51.507531
            },
            "size": [1]
        }
    ]
}	# 4 Cars. 8 Services. Min Vehicles. Then Min Transport Time

# Response Payloads

response_one = {
    'copyrights': ['GraphHopper', 'OpenStreetMap contributors'],
    'job_id': 'bfc539ed-0df3-4525-a543-bcd75b6281d7',
    'status': 'finished',
    'waiting_time_in_queue': 0,
    'processing_time': 225,
    'solution': {
        'costs': 698,
        'distance': 60805,
        'time': 10105,
        'transport_time': 10105,
        'completion_time': 10105,
        'max_operation_time': 5769,
        'waiting_time': 0,
        'service_duration': 0,
        'preparation_time': 0,
        'no_vehicles': 3,
        'no_unassigned': 0,
        'routes': [{
            'vehicle_id': 'vehicle2',
            'distance': 35516,
            'transport_time': 5769,
            'completion_time': 5769,
            'waiting_time': 0,
            'service_duration': 0,
            'preparation_time': 0,
            'activities': [{
                'type': 'start',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'end_time': 0,
                'end_date_time': None,
                'distance': 0,
                'driving_time': 0,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_after': [0]
            }, {
                'type': 'service',
                'id': '4',
                'location_id': 'loc_4',
                'address': {
                    'location_id': 'loc_4',
                    'lat': 51.507268,
                    'lon': -0.16573
                },
                'arr_time': 1417,
                'arr_date_time': None,
                'end_time': 1417,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 7381,
                'driving_time': 1417,
                'preparation_time': 0,
                'load_before': [0],
                'load_after': [1]
            }, {
                'type': 'service',
                'id': '8',
                'location_id': 'loc_11',
                'address': {
                    'location_id': 'loc_11',
                    'lat': 51.507531,
                    'lon': -0.221122
                },
                'arr_time': 2330,
                'arr_date_time': None,
                'end_time': 2330,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 14390,
                'driving_time': 2330,
                'preparation_time': 0,
                'load_before': [1],
                'load_after': [2]
            }, {
                'type': 'service',
                'id': '3',
                'location_id': 'loc_3',
                'address': {
                    'location_id': 'loc_3',
                    'lat': 51.536561,
                    'lon': -0.038972
                },
                'arr_time': 4738,
                'arr_date_time': None,
                'end_time': 4738,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 29660,
                'driving_time': 4738,
                'preparation_time': 0,
                'load_before': [2],
                'load_after': [3]
            }, {
                'type': 'end',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'arr_time': 5769,
                'arr_date_time': None,
                'distance': 35516,
                'driving_time': 5769,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_before': [3]
            }]
        }, {
            'vehicle_id': 'vehicle3',
            'distance': 4962,
            'transport_time': 972,
            'completion_time': 972,
            'waiting_time': 0,
            'service_duration': 0,
            'preparation_time': 0,
            'activities': [{
                'type': 'start',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'end_time': 0,
                'end_date_time': None,
                'distance': 0,
                'driving_time': 0,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_after': [0]
            }, {
                'type': 'service',
                'id': '7',
                'location_id': 'borough',
                'address': {
                    'location_id': 'borough',
                    'lat': 51.50347,
                    'lon': -0.091522
                },
                'arr_time': 338,
                'arr_date_time': None,
                'end_time': 338,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 1904,
                'driving_time': 338,
                'preparation_time': 0,
                'load_before': [0],
                'load_after': [1]
            }, {
                'type': 'service',
                'id': '2',
                'location_id': 'loc_2',
                'address': {
                    'location_id': 'loc_2',
                    'lat': 51.508902,
                    'lon': -0.094011
                },
                'arr_time': 572,
                'arr_date_time': None,
                'end_time': 572,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 2860,
                'driving_time': 572,
                'preparation_time': 0,
                'load_before': [1],
                'load_after': [2]
            }, {
                'type': 'end',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'arr_time': 972,
                'arr_date_time': None,
                'distance': 4962,
                'driving_time': 972,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_before': [2]
            }]
        }, {
            'vehicle_id': 'vehicle4',
            'distance': 20327,
            'transport_time': 3364,
            'completion_time': 3364,
            'waiting_time': 0,
            'service_duration': 0,
            'preparation_time': 0,
            'activities': [{
                'type': 'start',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'end_time': 0,
                'end_date_time': None,
                'distance': 0,
                'driving_time': 0,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_after': [0]
            }, {
                'type': 'service',
                'id': '5',
                'location_id': 'loc_5',
                'address': {
                    'location_id': 'loc_5',
                    'lat': 51.458452,
                    'lon': -0.149261
                },
                'arr_time': 1340,
                'arr_date_time': None,
                'end_time': 1340,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 8321,
                'driving_time': 1340,
                'preparation_time': 0,
                'load_before': [0],
                'load_after': [1]
            }, {
                'type': 'service',
                'id': '6',
                'location_id': 'loc_6',
                'address': {
                    'location_id': 'loc_6',
                    'lat': 51.479107,
                    'lon': -0.156498
                },
                'arr_time': 1987,
                'arr_date_time': None,
                'end_time': 1987,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 12073,
                'driving_time': 1987,
                'preparation_time': 0,
                'load_before': [1],
                'load_after': [2]
            }, {
                'type': 'service',
                'id': '1',
                'location_id': 'loc_1',
                'address': {
                    'location_id': 'loc_1',
                    'lat': 51.484484,
                    'lon': -0.149832
                },
                'arr_time': 2248,
                'arr_date_time': None,
                'end_time': 2248,
                'end_date_time': None,
                'waiting_time': 0,
                'distance': 13271,
                'driving_time': 2248,
                'preparation_time': 0,
                'load_before': [2],
                'load_after': [3]
            }, {
                'type': 'end',
                'location_id': 'home_location_tower_bridge',
                'address': {
                    'location_id': 'home_location_tower_bridge',
                    'lat': 51.505597,
                    'lon': -0.075338
                },
                'arr_time': 3364,
                'arr_date_time': None,
                'distance': 20327,
                'driving_time': 3364,
                'preparation_time': 0,
                'waiting_time': 0,
                'load_before': [3]
            }]
        }],
        'unassigned': {
            'services': [],
            'shipments': [],
            'breaks': [],
            'details': []
        }
    }
}

# Building Custom Requests