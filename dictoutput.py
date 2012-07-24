import table_format

scores = {
   'Santa Monica': {'UrbanSpoon': ['4.4'], 'Google': ['3.5'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['3.5'], 'OpenTable': ['3.9']}, 
   'Canaletto Newport Beach': {'UrbanSpoon': ['4.3'], 'Google': ['3.3'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['5.0'], 'OpenTable': ['4.3']}, 'Pasadena': {'UrbanSpoon': ['4.4'], 'Google': ['3.7'], 'Yelp': ['3.0'], 'TripAdvisor': ['3.5'], 'CitySearch': ['4.5'], 'OpenTable': ['4.0']}, 'Corte Madera': {'UrbanSpoon': ['4.3'], 'Google': ['3.5'], 'Yelp': ['3.0'], 'TripAdvisor': ['3.5'], 'CitySearch': ['4.5'], 'OpenTable': ['3.9']}, 'San Francisco': {'UrbanSpoon': ['4.4'], 'Google': ['3.6'], 'Yelp': ['3.0'], 'TripAdvisor': ['4.0'], 'CitySearch': ['N/A'], 'OpenTable': ['3.8']}, 'Del Mar': {'UrbanSpoon': ['4.3'], 'Google': ['3.8'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['N/A'], 'OpenTable': ['4.0']}, 'Burlingame': {'UrbanSpoon': ['4.1'], 'Google': ['3.8'], 'Yelp': ['3.0'], 'TripAdvisor': ['3.5'], 'CitySearch': ['3.0'], 'OpenTable': ['4.0']}, 'Sacramento': {'UrbanSpoon': ['4.3'], 'Google': ['4.2'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.0'], 'OpenTable': ['4.3']}, 'Irvine': {'UrbanSpoon': ['3.9'], 'Google': ['3.9'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['5.0'], 'OpenTable': ['4.1']}, 'Greenwood Village': {'UrbanSpoon': ['3.7'], 'Google': ['3.4'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['N/A'], 'OpenTable': ['4.0']}, 'San Jose': {'UrbanSpoon': ['4.4'], 'Google': ['3.9'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['N/A'], 'OpenTable': ['3.9']}, 'Canaletto Las Vegas': {'UrbanSpoon': ['4.4'], 'Google': ['4.0'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.0'], 'OpenTable': ['3.9']}, 'Coronado': {'UrbanSpoon': ['4.1'], 'Google': ['4.1'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['5.0'], 'OpenTable': ['4.1']}, 'Palo Alto': {'UrbanSpoon': ['4.1'], 'Google': ['3.6'], 'Yelp': ['3.0'], 'TripAdvisor': ['4.0'], 'CitySearch': ['N/A'], 'OpenTable': ['4.0']}, 'Reston': {'UrbanSpoon': ['3.7'], 'Google': ['3.7'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['N/A'], 'OpenTable': ['4.1']}, 'Walnut Creek': {'UrbanSpoon': ['3.9'], 'Google': ['3.9'], 'Yelp': ['3.0'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.0'], 'OpenTable': ['3.8']}, 'Carmel': {'UrbanSpoon': ['3.9'], 'Google': ['3.6'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.0'], 'OpenTable': ['3.8']}, 'Beverly Hills': {'UrbanSpoon': ['4.5'], 'Google': ['3.8'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.5'], 'OpenTable': ['4.0']}, 'Roseville': {'UrbanSpoon': ['4.1'], 'Google': ['4.2'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['4.0'], 'OpenTable': ['4.2']}, 'Las Vegas': {'UrbanSpoon': ['4.0'], 'Google': ['4.0'], 'Yelp': ['3.0'], 'TripAdvisor': ['4.0'], 'CitySearch': ['3.5'], 'OpenTable': ['N/A']}, 'Manhattan Beach': {'UrbanSpoon': ['4.4'], 'Google': ['3.6'], 'Yelp': ['3.5'], 'TripAdvisor': ['4.0'], 'CitySearch': ['3.5'], 'OpenTable': ['4.1']}, 'Seattle': {'UrbanSpoon': ['3.9'], 'Google': ['3.7'], 'Yelp': ['3.5'], 'TripAdvisor': ['3.5'], 'CitySearch': ['N/A'], 'OpenTable': ['4.0']}}

headers = [
    'Location',
    'CitySearch',
    'Google',
    'OpenTable',
    'TripAdvisor',
    'UrbanSpoon',
    'Yelp'
    ]


table_format.MakeTable(scores, headers)
