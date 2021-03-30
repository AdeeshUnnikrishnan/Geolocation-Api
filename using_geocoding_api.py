import requests

API_KEY = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw" #api key provided in the google_drive_link
address =  " Airport Rd Peelamedu Coimbatore India "
params = {
    'key' : API_KEY,
    'address' : address.replace(' ', '+'), # formatting to parse in the url
    #'sensor':True
    }
url = 'https://maps.googleapis.com/maps/api/geocode/json?'
res = requests.get(url,params=params).json()
print("Keys Present:",res.keys())
print("Status = ",res['status'])
print("Results :\n",res['results'])
#print(res['error_message'])
if res['status'] == 'OK':
    res['results'][0].keys()
