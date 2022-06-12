import json
import requests
from databaseUpdater import runUpdated as runUpdated

# BUSINESS_ENDPOINT = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
place_ID = 'ChIJX5bnADlfwokRUhMJPlULX_o'
api_key = 'AIzaSyA20P_POGlN1n7fAsghhbzGMyrr9i24Oa8'
url = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name%2Crating%2Creviews&key={}".format(
    place_ID, api_key)


print('GET method operating nominally')

reviewCatcher = {
    "id_Review": [],
    "url_Review": [],
    "body_Review": [],
    "rating_Review": [],
    "platform_Review": [],
    "locationId_Review": [],
    "userId_Review": [],
    "brandId_Review": [],
    "timeCreated_Review": []
}


try:
    response = requests.get(url)
    json_data = json.loads(response.text)
    reviews = json_data['result']["reviews"]
    for items in reviews:
        print(items)
        reviewCatcher['id_Review'].append('{}'.format('needs attention'))
        reviewCatcher['url_Review'].append('{}'.format(items['author_url']))
        reviewCatcher['body_Review'].append('{}'.format(items['text']))
        reviewCatcher['rating_Review'].append('{}'.format(items['rating']))
        reviewCatcher['platform_Review'].append('Google')
        reviewCatcher['locationId_Review'].append('{}'.format('needs attention'))
        reviewCatcher['userId_Review'].append('{}'.format(items['author_url']))
        reviewCatcher['brandId_Review'].append('{}'.format('needs attention'))
        reviewCatcher['timeCreated_Review'].append('{}'.format(items['time']))

except:
    print('HTTP error occurred')
print('reviewCatcher operating nominally')

i = 0
while i <= int(len(reviewCatcher['body_Review'])):
    runUpdated(
        reviewCatcher['id_Review'][i],
        reviewCatcher['url_Review'][i],
        reviewCatcher['body_Review'][i],
        int(reviewCatcher['rating_Review'][i]),
        reviewCatcher['platform_Review'][i],
        reviewCatcher['locationId_Review'][i],
        reviewCatcher['userId_Review'][i],
        reviewCatcher['brandId_Review'][i],
        reviewCatcher['timeCreated_Review'][i])
    i += 1
    print(i)
    if i == int(len(reviewCatcher['body_Review'])):
        print("Iteration loop operating nominally")
print('Database update successfully')
