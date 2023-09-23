import json
import os
import shutil

import requests

s = requests.Session()


def list_albums():
  resp = s.get('https://photoslibrary.googleapis.com/v1/albums')
  resp.raise_for_status()
  print(json.dumps(resp.json()))


def list_album_contents(album_id):
  resp = s.post('https://photoslibrary.googleapis.com/v1/mediaItems:search', json={
    'pageSize': 100,
    'albumId': album_id,
  })
  resp.raise_for_status()
  items = resp.json()

  first = items['mediaItems'][0]

  print(f'Requesting:\n\n{json.dumps(first, indent=4)}')
  if first['mimeType'].startswith('video'):
    resp = requests.get(f'{first["baseUrl"]}=dv', stream=True)
  else:
    resp = requests.get(f'{first["baseUrl"]}=d', stream=True)
  resp.raise_for_status()

  with open(f'out/{first["filename"]}', 'wb') as f:
    shutil.copyfileobj(resp.raw, f)
  print(f'Wrote out/{first["filename"]}')



def main():
  with open('creds/token.json', 'r') as f:
    token = json.load(f)
  s.headers.update({'Authorization': f'Bearer {token["token"]}'})
  list_album_contents(os.environ['GOOGLE_ALBUM_ID'])


if __name__ == '__main__':
  main()
