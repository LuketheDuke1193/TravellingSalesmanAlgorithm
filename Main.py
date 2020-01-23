# Lucas Roberts #001085316
# C950 WGUPS Project

from HashTable import HashTable
import csv
from Package import Package
from Graph import Graph, Vertex
from Location import Location

# create hash table for package data
from Truck import Truck

packages = HashTable()

# import CSV data for packages and insert into hash table
# O(N)
with open('WGUPS Package File.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    for row in readPackageCSV:
        if len(row) == 8:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            packages.insert(package)
        else:
            package = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            packages.insert(package)

# create graph for location data
locations_graph = Graph()
# add in vertex location data.

hub = Location("Western Governors University", "4001 South 700 East", "Salt Lake City", "UT", "84107")
international_peace_gardens = Location("International Peace Gardens", "1060 Dalton Ave S", "Salt Lake City", "UT",
                                       "84104")
sugar_house_park = Location("Sugar House Park", "1330 2100 S", "Salt Lake City", "UT", "84106")
taylorsville_bennion_heritage_city_gov_off = Location("Taylorsville-Bennion Heritage City Gov Off", "1488 4800 S",
                                                      "Salt Lake City", "UT", "84123")
salt_lake_city_division_of_health_services = Location("Salt Lake City Division of Health Services", "177 W Price Ave",
                                                      "Salt Lake City", "UT", "84115")
south_salt_lake_public_works = Location("South Salt Lake Public Works", "195 W Oakland Ave", "Salt Lake City", "UT",
                                        "84115")
salt_lake_city_streets_and_sanitation = Location("Salt Lake City Streets and Sanitation", "2010 W 500 S",
                                                 "Salt Lake City", "UT", "84104")
deker_lake = Location("Deker Lake", "2300 Parkway Blvd", "West Valley City", "UT", "84119")
salt_lake_city_ottinger_hall = Location("Salt Lake City Ottinger Hall", "233 Canyon Rd", "Salt Lake City", "UT",
                                        "84103")
columbus_library = Location("Columbus Library", "2530 S 500 E", "Salt Lake City", "UT", "84106")
taylorsville_city_hall = Location("Taylorsville City Hall", "2600 Taylorsville Blvd", "Salt Lake City", "UT", "84118")
south_salt_lake_police = Location("South Salt Lake Police", "2835 Main St", "Salt Lake City", "UT", "84115")
council_hall = Location("Council Hall", "300 State St", "Salt Lake City", "UT", "84103")
redwood_park = Location("Redwood Park", "3060 Lester St", "West Valley City", "UT", "84119")
salt_lake_county_mental_health = Location("Salt Lake County Mental Health", "3148 S 1100 W", "Salt Lake City", "UT",
                                          "84119")
salt_lake_county_united_police_dept = Location("Salt Lake County/United Police Dept", "3365 S 900 W", "Salt Lake City",
                                               "UT", "84119")
west_valley_prosecutor = Location("West Valley Prosecutor", "3575 W Valley Central Station bus Loop",
                                  "West Valley City", "UT", "84119")
housing_auth_of_salt_lake_county = Location("Housing Auth. of Salt Lake County", "3595 Main St.", "Salt Lake City",
                                            "UT", "84115")
utah_dmv_administrative_office = Location("Utah DMV Administrative Office", "380 W 2880 S", "Salt Lake City", "UT",
                                          "84115")
third_district_juvenile_court = Location("Third District Juvenile Court", "410 S State St", "Salt Lake City", "UT",
                                         "84111")
cottonwood_regional_softball_complex = Location("Cottonwood Regional Softball Complex", "4300 S 1300 E", "Millcreek",
                                                "UT", "84117")
holiday_city_office = Location("Holiday City Office", "4580 S 2300 E", "Holladay", "UT", "84117")
murray_city_museum = Location("Murray City Museum", "5025 State St", "Murray", "UT", "84107")
valley_regional_softball_complex = Location("Valley Regional Softball Complex", "5100 South 2700 West",
                                            "Salt Lake City", "UT", "84118")
city_center_of_rock_springs = Location("City Center of Rock Springs", "5383 S 900 East #104", "Salt Lake City", "UT",
                                       "84117")
rice_terrace_pavilion_park = Location("Rice Terrace Pavilion Park", "600 E 900 South", "Salt Lake City", "UT", "84105")
wheeler_historic_farm = Location("Wheeler Historic Farm", "6351 South 900 East", "Murray", "UT", "84121")

vertex_hub = Vertex(hub)
vertex_international_peace_gardens = Vertex(international_peace_gardens)
vertex_sugar_house_park = Vertex(sugar_house_park)
vertex_taylorsville_bennion_heritage_city_gov_off = Vertex(taylorsville_bennion_heritage_city_gov_off)
vertex_salt_lake_city_division_of_health_services = Vertex(salt_lake_city_division_of_health_services)
vertex_south_salt_lake_public_works = Vertex(south_salt_lake_public_works)
vertex_salt_lake_city_streets_and_sanitation = Vertex(salt_lake_city_streets_and_sanitation)
vertex_deker_lake = Vertex(deker_lake)
vertex_salt_lake_city_ottinger_hall = Vertex(salt_lake_city_ottinger_hall)
vertex_columbus_library = Vertex(columbus_library)
vertex_taylorsville_city_hall = Vertex(taylorsville_city_hall)
vertex_south_salt_lake_police = Vertex(south_salt_lake_police)
vertex_council_hall = Vertex(council_hall)
vertex_redwood_park = Vertex(redwood_park)
vertex_salt_lake_county_mental_health = Vertex(salt_lake_county_mental_health)
vertex_salt_lake_county_united_police_dept = Vertex(salt_lake_county_united_police_dept)
vertex_west_valley_prosecutor = Vertex(west_valley_prosecutor)
vertex_housing_auth_of_salt_lake_county = Vertex(housing_auth_of_salt_lake_county)
vertex_utah_dmv_administrative_office = Vertex(utah_dmv_administrative_office)
vertex_third_district_juvenile_court = Vertex(third_district_juvenile_court)
vertex_cottonwood_regional_softball_complex = Vertex(cottonwood_regional_softball_complex)
vertex_holiday_city_office = Vertex(holiday_city_office)
vertex_murray_city_museum = Vertex(murray_city_museum)
vertex_valley_regional_softball_complex = Vertex(valley_regional_softball_complex)
vertex_city_center_of_rock_springs = Vertex(city_center_of_rock_springs)
vertex_rice_terrace_pavilion_park = Vertex(rice_terrace_pavilion_park)
vertex_wheeler_historic_farm = Vertex(wheeler_historic_farm)

locations_graph.add_vertex(vertex_hub)
locations_graph.add_vertex(vertex_international_peace_gardens)
locations_graph.add_vertex(vertex_sugar_house_park)
locations_graph.add_vertex(vertex_taylorsville_bennion_heritage_city_gov_off)
locations_graph.add_vertex(vertex_salt_lake_city_division_of_health_services)
locations_graph.add_vertex(vertex_south_salt_lake_public_works)
locations_graph.add_vertex(vertex_salt_lake_city_streets_and_sanitation)
locations_graph.add_vertex(vertex_deker_lake)
locations_graph.add_vertex(vertex_salt_lake_city_ottinger_hall)
locations_graph.add_vertex(vertex_columbus_library)
locations_graph.add_vertex(vertex_taylorsville_city_hall)
locations_graph.add_vertex(vertex_south_salt_lake_police)
locations_graph.add_vertex(vertex_council_hall)
locations_graph.add_vertex(vertex_redwood_park)
locations_graph.add_vertex(vertex_salt_lake_county_mental_health)
locations_graph.add_vertex(vertex_salt_lake_county_united_police_dept)
locations_graph.add_vertex(vertex_west_valley_prosecutor)
locations_graph.add_vertex(vertex_housing_auth_of_salt_lake_county)
locations_graph.add_vertex(vertex_utah_dmv_administrative_office)
locations_graph.add_vertex(vertex_third_district_juvenile_court)
locations_graph.add_vertex(vertex_cottonwood_regional_softball_complex)
locations_graph.add_vertex(vertex_holiday_city_office)
locations_graph.add_vertex(vertex_murray_city_museum)
locations_graph.add_vertex(vertex_valley_regional_softball_complex)
locations_graph.add_vertex(vertex_city_center_of_rock_springs)
locations_graph.add_vertex(vertex_rice_terrace_pavilion_park)
locations_graph.add_vertex(vertex_wheeler_historic_farm)

locations_graph.add_undirected_edge(vertex_hub, vertex_international_peace_gardens, 7.2)
locations_graph.add_undirected_edge(vertex_hub, vertex_sugar_house_park, 3.8)
locations_graph.add_undirected_edge(vertex_hub, vertex_taylorsville_bennion_heritage_city_gov_off, 11.0)
locations_graph.add_undirected_edge(vertex_hub, vertex_salt_lake_city_division_of_health_services, 2.2)
locations_graph.add_undirected_edge(vertex_hub, vertex_south_salt_lake_public_works, 3.5)
locations_graph.add_undirected_edge(vertex_hub, vertex_salt_lake_city_streets_and_sanitation, 10.9)
locations_graph.add_undirected_edge(vertex_hub, vertex_deker_lake, 8.6)
locations_graph.add_undirected_edge(vertex_hub, vertex_salt_lake_city_ottinger_hall, 7.6)
locations_graph.add_undirected_edge(vertex_hub, vertex_columbus_library, 2.8)
locations_graph.add_undirected_edge(vertex_hub, vertex_taylorsville_city_hall, 6.4)
locations_graph.add_undirected_edge(vertex_hub, vertex_south_salt_lake_police, 3.2)
locations_graph.add_undirected_edge(vertex_hub, vertex_council_hall, 7.6)
locations_graph.add_undirected_edge(vertex_hub, vertex_redwood_park, 5.2)
locations_graph.add_undirected_edge(vertex_hub, vertex_salt_lake_county_mental_health, 4.4)
locations_graph.add_undirected_edge(vertex_hub, vertex_salt_lake_county_united_police_dept, 3.7)
locations_graph.add_undirected_edge(vertex_hub, vertex_west_valley_prosecutor, 7.6)
locations_graph.add_undirected_edge(vertex_hub, vertex_housing_auth_of_salt_lake_county, 2.0)
locations_graph.add_undirected_edge(vertex_hub, vertex_utah_dmv_administrative_office, 3.6)
locations_graph.add_undirected_edge(vertex_hub, vertex_third_district_juvenile_court, 6.5)
locations_graph.add_undirected_edge(vertex_hub, vertex_cottonwood_regional_softball_complex, 1.9)
locations_graph.add_undirected_edge(vertex_hub, vertex_holiday_city_office, 3.4)
locations_graph.add_undirected_edge(vertex_hub, vertex_murray_city_museum, 2.4)
locations_graph.add_undirected_edge(vertex_hub, vertex_valley_regional_softball_complex, 5.0)
locations_graph.add_undirected_edge(vertex_hub, vertex_city_center_of_rock_springs, 2.4)
locations_graph.add_undirected_edge(vertex_hub, vertex_rice_terrace_pavilion_park, 5.0)
locations_graph.add_undirected_edge(vertex_hub, vertex_wheeler_historic_farm, 3.6)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_sugar_house_park, 7.1)
locations_graph.add_undirected_edge(vertex_international_peace_gardens,
                                    vertex_taylorsville_bennion_heritage_city_gov_off, 6.4)
locations_graph.add_undirected_edge(vertex_international_peace_gardens,
                                    vertex_salt_lake_city_division_of_health_services, 6.0)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_south_salt_lake_public_works, 4.8)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_salt_lake_city_streets_and_sanitation,
                                    1.6)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_deker_lake, 2.8)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_salt_lake_city_ottinger_hall, 4.8)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_columbus_library, 6.3)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_taylorsville_city_hall, 7.3)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_south_salt_lake_police, 5.3)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_council_hall, 4.8)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_redwood_park, 3.0)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_salt_lake_county_mental_health, 4.6)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_salt_lake_county_united_police_dept, 4.5)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_west_valley_prosecutor, 7.4)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_housing_auth_of_salt_lake_county, 6.0)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_utah_dmv_administrative_office, 5.0)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_third_district_juvenile_court, 4.8)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_cottonwood_regional_softball_complex,
                                    9.5)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_holiday_city_office, 10.9)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_murray_city_museum, 8.3)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_valley_regional_softball_complex, 6.9)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_city_center_of_rock_springs, 10.0)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_rice_terrace_pavilion_park, 4.4)
locations_graph.add_undirected_edge(vertex_international_peace_gardens, vertex_wheeler_historic_farm, 13.0)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_taylorsville_bennion_heritage_city_gov_off, 9.2)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_salt_lake_city_division_of_health_services, 4.4)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_south_salt_lake_public_works, 2.8)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_salt_lake_city_streets_and_sanitation, 8.6)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_deker_lake, 6.3)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_salt_lake_city_ottinger_hall, 5.3)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_columbus_library, 1.6)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_taylorsville_city_hall, 10.4)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_south_salt_lake_police, 3.0)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_council_hall, 5.3)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_redwood_park, 6.5)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_salt_lake_county_mental_health, 5.6)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_salt_lake_county_united_police_dept, 5.8)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_west_valley_prosecutor, 5.7)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_housing_auth_of_salt_lake_county, 4.1)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_utah_dmv_administrative_office, 3.6)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_third_district_juvenile_court, 4.3)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_cottonwood_regional_softball_complex, 3.3)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_holiday_city_office, 5.0)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_murray_city_museum, 6.1)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_valley_regional_softball_complex, 9.7)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_city_center_of_rock_springs, 6.1)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_rice_terrace_pavilion_park, 2.8)
locations_graph.add_undirected_edge(vertex_sugar_house_park, vertex_wheeler_historic_farm, 7.4)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_taylorsville_bennion_heritage_city_gov_off, 5.6)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_south_salt_lake_public_works, 6.9)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_salt_lake_city_streets_and_sanitation, 8.6)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_deker_lake, 4.0)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_salt_lake_city_ottinger_hall, 11.1)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_columbus_library, 7.3)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_taylorsville_city_hall,
                                    1.0)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_south_salt_lake_police,
                                    6.4)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_council_hall, 11.1)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_redwood_park, 3.9)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_salt_lake_county_mental_health, 4.3)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_salt_lake_county_united_police_dept, 4.4)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_west_valley_prosecutor,
                                    7.2)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_housing_auth_of_salt_lake_county, 5.3)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_utah_dmv_administrative_office, 6.0)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_third_district_juvenile_court, 10.6)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_cottonwood_regional_softball_complex, 5.9)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_holiday_city_office, 7.4)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_murray_city_museum, 4.7)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_valley_regional_softball_complex, 0.6)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_city_center_of_rock_springs, 6.4)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off,
                                    vertex_rice_terrace_pavilion_park, 10.1)
locations_graph.add_undirected_edge(vertex_taylorsville_bennion_heritage_city_gov_off, vertex_wheeler_historic_farm,
                                    10.1)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_south_salt_lake_public_works, 1.9)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_salt_lake_city_streets_and_sanitation, 7.9)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_deker_lake, 5.1)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_salt_lake_city_ottinger_hall, 7.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_columbus_library, 2.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_taylorsville_city_hall,
                                    6.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_south_salt_lake_police,
                                    1.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_council_hall, 7.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_redwood_park, 3.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_salt_lake_county_mental_health, 2.4)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_salt_lake_county_united_police_dept, 2.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_west_valley_prosecutor,
                                    1.4)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_housing_auth_of_salt_lake_county, 0.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_utah_dmv_administrative_office, 1.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_third_district_juvenile_court, 6.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_cottonwood_regional_softball_complex, 3.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_holiday_city_office, 5.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_murray_city_museum, 2.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_valley_regional_softball_complex, 6.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_city_center_of_rock_springs, 4.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services,
                                    vertex_rice_terrace_pavilion_park, 5.4)
locations_graph.add_undirected_edge(vertex_salt_lake_city_division_of_health_services, vertex_wheeler_historic_farm,
                                    5.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_salt_lake_city_streets_and_sanitation,
                                    6.3)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_deker_lake, 4.3)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_salt_lake_city_ottinger_hall, 4.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_columbus_library, 1.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_taylorsville_city_hall, 8.7)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_south_salt_lake_police, 0.8)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_council_hall, 4.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_redwood_park, 3.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_salt_lake_county_mental_health, 3.0)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_salt_lake_county_united_police_dept,
                                    3.8)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_west_valley_prosecutor, 5.7)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_housing_auth_of_salt_lake_county, 1.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_utah_dmv_administrative_office, 1.1)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_third_district_juvenile_court, 3.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_cottonwood_regional_softball_complex,
                                    4.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_holiday_city_office, 6.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_murray_city_museum, 4.2)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_valley_regional_softball_complex, 9.0)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_city_center_of_rock_springs, 5.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_rice_terrace_pavilion_park, 3.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_public_works, vertex_wheeler_historic_farm, 7.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_deker_lake, 4.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_salt_lake_city_ottinger_hall,
                                    4.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_columbus_library, 8.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_taylorsville_city_hall, 8.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_south_salt_lake_police, 6.9)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_council_hall, 4.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_redwood_park, 4.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_salt_lake_county_mental_health,
                                    8.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation,
                                    vertex_salt_lake_county_united_police_dept, 5.8)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_west_valley_prosecutor, 7.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation,
                                    vertex_housing_auth_of_salt_lake_county, 7.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_utah_dmv_administrative_office,
                                    6.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_third_district_juvenile_court,
                                    3.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation,
                                    vertex_cottonwood_regional_softball_complex, 11.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_holiday_city_office, 12.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_murray_city_museum, 10.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation,
                                    vertex_valley_regional_softball_complex, 8.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_city_center_of_rock_springs,
                                    11.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_rice_terrace_pavilion_park,
                                    5.1)
locations_graph.add_undirected_edge(vertex_salt_lake_city_streets_and_sanitation, vertex_wheeler_historic_farm, 14.2)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_salt_lake_city_ottinger_hall, 7.7)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_columbus_library, 9.3)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_taylorsville_city_hall, 4.6)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_south_salt_lake_police, 4.8)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_council_hall, 7.7)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_redwood_park, 1.6)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_salt_lake_county_mental_health, 3.3)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_salt_lake_county_united_police_dept, 3.4)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_west_valley_prosecutor, 3.1)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_housing_auth_of_salt_lake_county, 5.1)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_utah_dmv_administrative_office, 4.6)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_third_district_juvenile_court, 6.7)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_cottonwood_regional_softball_complex, 8.1)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_holiday_city_office, 10.4)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_murray_city_museum, 7.8)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_valley_regional_softball_complex, 4.2)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_city_center_of_rock_springs, 9.5)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_rice_terrace_pavilion_park, 6.2)
locations_graph.add_undirected_edge(vertex_deker_lake, vertex_wheeler_historic_farm, 10.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_columbus_library, 4.8)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_taylorsville_city_hall, 11.9)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_south_salt_lake_police, 4.7)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_council_hall, 0.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_redwood_park, 7.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_salt_lake_county_mental_health, 7.8)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_salt_lake_county_united_police_dept,
                                    6.6)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_west_valley_prosecutor, 7.2)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_housing_auth_of_salt_lake_county, 5.9)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_utah_dmv_administrative_office, 5.4)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_third_district_juvenile_court, 1.0)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_cottonwood_regional_softball_complex,
                                    8.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_holiday_city_office, 10.3)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_murray_city_museum, 7.8)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_valley_regional_softball_complex, 11.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_city_center_of_rock_springs, 9.5)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_rice_terrace_pavilion_park, 2.8)
locations_graph.add_undirected_edge(vertex_salt_lake_city_ottinger_hall, vertex_wheeler_historic_farm, 14.1)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_taylorsville_city_hall, 9.4)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_south_salt_lake_police, 1.1)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_council_hall, 5.1)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_redwood_park, 4.6)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_salt_lake_county_mental_health, 3.7)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_salt_lake_county_united_police_dept, 4.0)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_west_valley_prosecutor, 6.7)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_housing_auth_of_salt_lake_county, 2.3)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_utah_dmv_administrative_office, 1.8)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_third_district_juvenile_court, 4.1)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_cottonwood_regional_softball_complex, 3.8)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_holiday_city_office, 5.8)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_murray_city_museum, 4.3)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_valley_regional_softball_complex, 7.8)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_city_center_of_rock_springs, 4.8)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_rice_terrace_pavilion_park, 3.2)
locations_graph.add_undirected_edge(vertex_columbus_library, vertex_wheeler_historic_farm, 6.0)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_south_salt_lake_police, 7.3)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_council_hall, 12.0)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_redwood_park, 4.9)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_salt_lake_county_mental_health, 5.2)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_salt_lake_county_united_police_dept, 5.4)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_west_valley_prosecutor, 8.1)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_housing_auth_of_salt_lake_county, 6.2)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_utah_dmv_administrative_office, 6.9)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_third_district_juvenile_court, 11.5)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_cottonwood_regional_softball_complex, 6.9)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_holiday_city_office, 8.3)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_murray_city_museum, 4.1)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_valley_regional_softball_complex, 0.4)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_city_center_of_rock_springs, 4.9)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_rice_terrace_pavilion_park, 11.0)
locations_graph.add_undirected_edge(vertex_taylorsville_city_hall, vertex_wheeler_historic_farm, 6.8)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_council_hall, 4.7)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_redwood_park, 3.5)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_salt_lake_county_mental_health, 2.6)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_salt_lake_county_united_police_dept, 2.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_west_valley_prosecutor, 6.3)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_housing_auth_of_salt_lake_county, 1.2)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_utah_dmv_administrative_office, 1.0)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_third_district_juvenile_court, 3.7)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_cottonwood_regional_softball_complex, 4.1)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_holiday_city_office, 6.2)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_murray_city_museum, 3.4)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_valley_regional_softball_complex, 6.9)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_city_center_of_rock_springs, 5.2)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_rice_terrace_pavilion_park, 3.7)
locations_graph.add_undirected_edge(vertex_south_salt_lake_police, vertex_wheeler_historic_farm, 6.4)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_redwood_park, 7.3)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_salt_lake_county_mental_health, 7.8)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_salt_lake_county_united_police_dept, 6.6)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_west_valley_prosecutor, 7.2)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_housing_auth_of_salt_lake_county, 5.9)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_utah_dmv_administrative_office, 5.4)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_third_district_juvenile_court, 1.0)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_cottonwood_regional_softball_complex, 8.5)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_holiday_city_office, 10.3)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_murray_city_museum, 7.8)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_valley_regional_softball_complex, 11.5)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_city_center_of_rock_springs, 9.5)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_rice_terrace_pavilion_park, 2.8)
locations_graph.add_undirected_edge(vertex_council_hall, vertex_wheeler_historic_farm, 14.1)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_salt_lake_county_mental_health, 1.3)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_salt_lake_county_united_police_dept, 1.5)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_west_valley_prosecutor, 4.0)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_housing_auth_of_salt_lake_county, 3.2)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_utah_dmv_administrative_office, 3.0)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_third_district_juvenile_court, 6.9)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_cottonwood_regional_softball_complex, 6.2)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_holiday_city_office, 8.2)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_murray_city_museum, 5.5)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_valley_regional_softball_complex, 4.4)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_city_center_of_rock_springs, 7.2)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_rice_terrace_pavilion_park, 6.4)
locations_graph.add_undirected_edge(vertex_redwood_park, vertex_wheeler_historic_farm, 10.5)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_salt_lake_county_united_police_dept,
                                    0.6)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_west_valley_prosecutor, 6.4)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_housing_auth_of_salt_lake_county, 2.4)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_utah_dmv_administrative_office, 2.2)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_third_district_juvenile_court, 6.8)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_cottonwood_regional_softball_complex,
                                    5.3)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_holiday_city_office, 7.4)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_murray_city_museum, 4.6)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_valley_regional_softball_complex, 4.8)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_city_center_of_rock_springs, 6.3)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_rice_terrace_pavilion_park, 6.5)
locations_graph.add_undirected_edge(vertex_salt_lake_county_mental_health, vertex_wheeler_historic_farm, 8.8)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_west_valley_prosecutor, 5.6)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_housing_auth_of_salt_lake_county,
                                    1.6)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_utah_dmv_administrative_office,
                                    1.7)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_third_district_juvenile_court,
                                    6.4)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept,
                                    vertex_cottonwood_regional_softball_complex, 4.9)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_holiday_city_office, 6.9)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_murray_city_museum, 4.2)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_valley_regional_softball_complex,
                                    5.6)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_city_center_of_rock_springs, 5.9)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_rice_terrace_pavilion_park, 5.7)
locations_graph.add_undirected_edge(vertex_salt_lake_county_united_police_dept, vertex_wheeler_historic_farm, 8.4)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_housing_auth_of_salt_lake_county, 7.1)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_utah_dmv_administrative_office, 6.1)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_third_district_juvenile_court, 7.2)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_cottonwood_regional_softball_complex, 10.6)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_holiday_city_office, 12.0)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_murray_city_museum, 9.4)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_valley_regional_softball_complex, 7.5)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_city_center_of_rock_springs, 11.1)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_rice_terrace_pavilion_park, 6.2)
locations_graph.add_undirected_edge(vertex_west_valley_prosecutor, vertex_wheeler_historic_farm, 13.6)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_utah_dmv_administrative_office, 1.6)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_third_district_juvenile_court, 4.9)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county,
                                    vertex_cottonwood_regional_softball_complex, 3.0)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_holiday_city_office, 5.0)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_murray_city_museum, 2.3)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_valley_regional_softball_complex,
                                    5.5)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_city_center_of_rock_springs, 4.0)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_rice_terrace_pavilion_park, 5.1)
locations_graph.add_undirected_edge(vertex_housing_auth_of_salt_lake_county, vertex_wheeler_historic_farm, 5.2)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_third_district_juvenile_court, 4.4)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_cottonwood_regional_softball_complex,
                                    4.6)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_holiday_city_office, 6.6)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_murray_city_museum, 3.9)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_valley_regional_softball_complex, 6.5)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_city_center_of_rock_springs, 5.6)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_rice_terrace_pavilion_park, 4.3)
locations_graph.add_undirected_edge(vertex_utah_dmv_administrative_office, vertex_wheeler_historic_farm, 6.9)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_cottonwood_regional_softball_complex,
                                    7.5)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_holiday_city_office, 9.3)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_murray_city_museum, 6.8)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_valley_regional_softball_complex, 11.4)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_city_center_of_rock_springs, 8.5)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_rice_terrace_pavilion_park, 1.8)
locations_graph.add_undirected_edge(vertex_third_district_juvenile_court, vertex_wheeler_historic_farm, 13.1)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex, vertex_holiday_city_office, 2.0)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex, vertex_murray_city_museum, 2.9)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex,
                                    vertex_valley_regional_softball_complex, 6.4)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex, vertex_city_center_of_rock_springs,
                                    2.8)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex, vertex_rice_terrace_pavilion_park, 6.0)
locations_graph.add_undirected_edge(vertex_cottonwood_regional_softball_complex, vertex_wheeler_historic_farm, 4.1)
locations_graph.add_undirected_edge(vertex_holiday_city_office, vertex_murray_city_museum, 4.4)
locations_graph.add_undirected_edge(vertex_holiday_city_office, vertex_valley_regional_softball_complex, 7.9)
locations_graph.add_undirected_edge(vertex_holiday_city_office, vertex_city_center_of_rock_springs, 3.4)
locations_graph.add_undirected_edge(vertex_holiday_city_office, vertex_rice_terrace_pavilion_park, 7.9)
locations_graph.add_undirected_edge(vertex_holiday_city_office, vertex_wheeler_historic_farm, 4.7)
locations_graph.add_undirected_edge(vertex_murray_city_museum, vertex_valley_regional_softball_complex, 4.5)
locations_graph.add_undirected_edge(vertex_murray_city_museum, vertex_city_center_of_rock_springs, 1.7)
locations_graph.add_undirected_edge(vertex_murray_city_museum, vertex_rice_terrace_pavilion_park, 6.8)
locations_graph.add_undirected_edge(vertex_murray_city_museum, vertex_wheeler_historic_farm, 3.1)
locations_graph.add_undirected_edge(vertex_valley_regional_softball_complex, vertex_city_center_of_rock_springs, 5.4)
locations_graph.add_undirected_edge(vertex_valley_regional_softball_complex, vertex_rice_terrace_pavilion_park, 10.6)
locations_graph.add_undirected_edge(vertex_valley_regional_softball_complex, vertex_wheeler_historic_farm, 7.8)
locations_graph.add_undirected_edge(vertex_city_center_of_rock_springs, vertex_rice_terrace_pavilion_park, 7.0)
locations_graph.add_undirected_edge(vertex_city_center_of_rock_springs, vertex_wheeler_historic_farm, 1.3)
locations_graph.add_undirected_edge(vertex_rice_terrace_pavilion_park, vertex_wheeler_historic_farm, 8.3)

# initialize and load trucks with packages
truck1 = Truck(1, locations_graph.adjacency_list.get(hub))
truck2 = Truck(2, locations_graph.adjacency_list.get(hub))
truck3 = Truck(3, locations_graph.adjacency_list.get(hub))

for i in range(1, 40):
    package_being_loaded = packages.lookup_item(i)
    if "truck 2" in packages.lookup_item(i).notes:
        truck2.add_package(packages.lookup_item(i))
        packages.lookup_item(i).status_out_for_delivery()
        print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',
              packages.lookup_item(i).address, 'onto truck 2')
    elif "Delayed" in packages.lookup_item(i).notes:
        packages.lookup_item(i).status_delayed()
    elif "Must be" in packages.lookup_item(i).notes or packages.lookup_item(i).package_id in (13, 15, 19):
        truck1.add_package(packages.lookup_item(i))
        packages.lookup_item(i).status_out_for_delivery()
        print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',
              packages.lookup_item(i).address, 'onto truck 1')
    elif packages.lookup_item(i).deadline != "EOD":
        truck2.add_package(packages.lookup_item(i))
        packages.lookup_item(i).status_out_for_delivery()
        print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',
              packages.lookup_item(i).address, 'onto truck 2')
    elif packages.lookup_item(i).deadline == "EOD":
        truck2.add_package(packages.lookup_item(i))
        packages.lookup_item(i).status_out_for_delivery()
        print('Now loading package #', packages.lookup_item(i).package_id, 'that is headed to',
              packages.lookup_item(i).address, 'onto truck 2')


# create algorithm for delivery of packages


# PLACEHOLDER FOR UNUSED CODE
"""with open('WGUPSLocations.csv') as csvfile:
    readPackageCSV = csv.reader(csvfile, delimiter=',')
    for row in readPackageCSV:
        location = Location(row[0], row[1], row[2])
        vertex = Vertex(location)
        locations_graph.add_vertex(vertex)"""

"""for item in locations_graph.adjacency_list.items():
    print(item[0].location.address)"""
