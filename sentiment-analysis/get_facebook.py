import facebook
import os
import string
from analyse_image import analyse_image
from sentiment import get_sentiment

token = os.environ['FACEBOOK_TOKEN']
graph = facebook.GraphAPI(access_token=token, version="3.0")

def get_thing():
    albums = graph.get_object(id='me', fields='albums')

    album_ids = []

    for album in albums['albums']['data']:
        album_ids.append(album['id'])

    print(album_ids)
        

def download_album(id):
    photos = graph.get_connections(id=id, connection_name='photos', fields='images')
    for photo in photos['data'].take(1):
        process_image(photo['images'][0])

def format_result(result):
    a, b, c = result
    return '{},{},{}'.format(a, b, c)

def get_social_score():
    posts = graph.get_all_connections(id='me', connection_name='posts', fields='reactions,likes,comments,created_time,message')

    num_likes = 0
    num_posts = 0
    num_comments = 0
    results = []

    for post in posts:
        num_comments = 0
        num_likes = 0
        content = ''

        if 'comments' in post:
            num_comments = len(post['comments']['data'])
        if 'likes' in post:
            num_likes += len(post['likes']['data'])
        
        sentiment = 0.5

        if 'message' in post:
            content = post['message']
            sentiment = get_sentiment(content)
        time = post['created_time']
        result = (time, sentiment, num_comments + num_likes)
        results.append(result)
        print(format_result(result))

    return results

result = get_social_score()

result_string = [ '{},{},{}'.format(a,b,c) for (a,b,c) in result]
all = '/n'.join*result_string
print(result_string)
