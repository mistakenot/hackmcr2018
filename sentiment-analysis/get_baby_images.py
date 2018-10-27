import facebook
import os

token = os.environ['FACEBOOK_TOKEN']
graph = facebook.GraphAPI(access_token=token, version="3.0")
albums = graph.get_object(id='me', fields='albums')

album_ids = []

for album in albums['albums']['data']:
    album_ids.append(album['id'])

print(album_ids)

def download_album(id):
    photos = graph.get_connections(id=id, connection_name='photos', fields='images')
    print(photos['data'][0].images[0])

download_album(album_ids[0])