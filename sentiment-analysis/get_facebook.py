import facebook
import os
from analyse_image import analyse_image

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


def get_social_score():
    posts = graph.get_all_connections(id='me', connection_name='posts', fields='reactions,likes,comments,created_time')

    num_likes = 0
    num_posts = 0
    num_comments = 0
    results = []
    for post in posts:
        print(num_posts)
        num_posts += 1
        if 'comments' in post:
            num_comments += len(post['comments']['data'])
        if 'likes' in post:
            num_likes += len(post['likes']['data'])

    return num_posts, num_comments, num_likes

result = get_social_score()

print(result)