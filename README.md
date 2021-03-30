# Geolocation-Api

Problem Definition : To create an API endpoint, which returns data related to geolocation.<br>

#Solution : 
Using python Geopy module and Google's Geocoding API <br>
IDE - Python IDLE<br>

#Technical Explanation : 
i) In the First program (using_geocoding_api.py) , I used Google's geocoding APIfor returning the address into geographical location i.e in terms of latitude and longitude co-ordinates.<br>
Requirements - Requests module, geocoding API from google console cloud, a base URL, Hyper-Parameter Tuning<br>

ii) In the Second Program(using_geopy_nomionatim.py), I used python's geopy module to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.Geopy uses "Nominatim" Feature for filtering out the requests per application and also uses "User_Agent" feature for the puprose of HTTP headers.<br>
Requirements - Geopy module (pip install geopy), Nominatim from geopy, user_agent
