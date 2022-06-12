import requests

url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJX5bnADlfwokRUhMJPlULX_o&fields=name%2Crating%2Creviews&key=AIzaSyA20P_POGlN1n7fAsghhbzGMyrr9i24Oa8"

payload={}
headers = {}

response = requests.request("GET", url)

print(response.text)