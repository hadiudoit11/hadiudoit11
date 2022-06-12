import json
import requests

# BUSINESS_ENDPOINT = 'https://maps.googleapis.com/maps/api/place/details/json?place_id='
page_ID = '1629340640668140'
access_token = 'EAAJnw1VDS0YBAOKYhZC660TCZARcIyuQdYdBkF5ZB5YPvanZAf3OebVcS6CktO25WJHhVYgwfSp6585OH7FX4EEgNKlsDv68lW8igxsaKhZAlBQrI3yGmyrxlZAasJxZBfcCZBWvTx6Fn08xpwPZCuKxIOmE7sN98MmrwXhCH5CxEnAzGSZCeEZBUWSwxDov54mqy1jcj168wIZAQI3BO0kPk5Ja'
url = "https://graph.facebook.com/v13.0/{}/ratings?fields=open_graph_story&access_token={}".format(page_ID, access_token)


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
    print(response)
    json_data = json.loads(response.text)
    reviews = json_data['data']
    print(reviews)
    # for items in reviews:
    #     print(items)
    #     reviewCatcher['id_Review'].append('{}'.format('needs attention'))
    #     reviewCatcher['url_Review'].append('{}'.format(items['author_url']))
    #     reviewCatcher['body_Review'].append('{}'.format(items['text']))
    #     reviewCatcher['rating_Review'].append('{}'.format(items['rating']))
    #     reviewCatcher['platform_Review'].append('Facebook')
    #     reviewCatcher['locationId_Review'].append('{}'.format('needs attention'))
    #     reviewCatcher['userId_Review'].append('{}'.format(items['author_url']))
    #     reviewCatcher['brandId_Review'].append('{}'.format('needs attention'))
    #     reviewCatcher['timeCreated_Review'].append('{}'.format(items['time']))

except:
    print('HTTP error occurred')
# print('reviewCatcher operating nominally')
#
# i = 0
# while i <= int(len(reviewCatcher['body_Review'])):
#     runUpdated(
#         reviewCatcher['id_Review'][i],
#         reviewCatcher['url_Review'][i],
#         reviewCatcher['body_Review'][i],
#         int(reviewCatcher['rating_Review'][i]),
#         reviewCatcher['platform_Review'][i],
#         reviewCatcher['locationId_Review'][i],
#         reviewCatcher['userId_Review'][i],
#         reviewCatcher['brandId_Review'][i],
#         reviewCatcher['timeCreated_Review'][i])
#     i += 1
#     print(i)
#     if i == int(len(reviewCatcher['body_Review'])):
#         print("Iteration loop operating nominally")
# print('Database update successfully')
