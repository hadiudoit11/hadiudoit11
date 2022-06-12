import json
import requests
from databaseUpdater import runUpdated as runUpdated

# BUSINESS_ENDPOINT = 'https://api.yelp.com/v3/businesses/'
url = 'https://api.yelp.com/v3/businesses/sofresh-tampa-2/reviews'
api_key = 'L4bu8CsQkUq4Q0sEp0Q3bSb53_2tkGCqsnlyGUK7fj-YsjMlIzcXFg8ll_sQcFGlPwYraYOE3-mZn0MD4nKf0vw_VOfY0F9s3AFdGDcqecQfzCZkqXH6SJi4baNPYnYx'
headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
reviewCatcher = {
    "id_Review":[],
    "url_Review":[],
    "body_Review":[],
    "rating_Review":[],
    "platform_Review":[],
    "locationId_Review":[],
    "userId_Review":[],
    "brandId_Review":[],
    "timeCreated_Review":[]
    }

try:
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    reviews = json_data["reviews"]
    for items in reviews:
        reviewCatcher['id_Review'].append('{}'.format(items['id']))
        reviewCatcher['url_Review'].append('{}'.format(items['url']))
        reviewCatcher['body_Review'].append('{}'.format(items['text']))
        reviewCatcher['rating_Review'].append('{}'.format(items['rating']))
        reviewCatcher['platform_Review'].append('Yelp')
        reviewCatcher['locationId_Review'].append('{}'.format(items['id']))
        reviewCatcher['userId_Review'].append('{}'.format(items['id']))
        reviewCatcher['brandId_Review'].append('{}'.format(items['time_created']))
        reviewCatcher['timeCreated_Review'].append('{}'.format(items['time_created']))
except:
        print('HTTP error occurred')

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
        print("iterated through it all!")
# print(reviewCatcher)