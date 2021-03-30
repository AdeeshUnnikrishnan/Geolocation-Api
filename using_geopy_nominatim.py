#from geopy.geocoders import Nominatim
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="example app")

print("Complete_details", geolocator.geocode("Airport Rd Peelamedu Coimbatore, India").raw)
print("\n")
print("Latitude and Longitude",geolocator.geocode("Airport Rd Peelamedu Coimbatore, India").point)
