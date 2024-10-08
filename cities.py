# install the needed library
pip install py-countries-states-cities-database

from py_countries_states_cities_database import (
        get_all_cities,
        get_all_states,
        get_all_countries,
        get_all_sub_regions,
        get_all_regions,
        get_all_states_and_cities_nested,
        get_all_countries_and_states_nested,
        get_all_countries_and_cities_nested,
        get_file_path
    )
    

# to get all cities
cities = get_all_cities()

# lets make it write some of the cities and see how they look like
for i in cities[:5]:
    print(city)

# in order to search on a specific country

cities = get_all_cities()

# search for only Türkiye
turkiye = [city for city in cities if city['country_name'] == 'Turkey']

for city in turkiye:
    print(city)

# push them into a list
sorted_cities = []

for city in turkiye:
    sorted_cities.append(city)

print(sorted_cities)

# to make it dataframe
import pandas  as pd

filtered = pd.DataFrame(sorted_cities)

filtered_ist_ank = filtered[filtered['state_name'].isin(['İstanbul','Ankara'])]

print(filtered_ist_ank)
