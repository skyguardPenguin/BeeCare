import json

import requests
from decouple import config
import asyncio
import aiohttp

def getToken():
    user = config('GALLERY_USER', cast=str)
    password = config('GALLERY_PASSWORD',cast=str)
    url = config('GALLERY_AUHT_URL',cast=str)

    payload = {"username": user, "password": password}

    token = None

    response = requests.post(url, data=payload)
    if response.status_code == requests.codes.ok:
        response_data = json.loads(response.text)
        token = response_data['access']
    else:
        print('Error obteniendo el token de acceso a la galería. 🫠')


    return token


def postSighting(image):
    token = getToken()

    if(token is None):
        return '!'

    url = config('GALERY_BEEPHOTO_URL', cast=str)
    headers = {"Authorization": "Bearer " + token}
    files = {'loadImage': image}
    response = requests.post(url, headers=headers, files=files)

    if response.status_code == requests.codes.ok:
        print('exitoso')
        return url +'get_image/' + str(response.json().get('id'))
    else:
        print('Error guardando la imagen. 🫠')
        print(response.content)
        return '!'



# async def fetchAsync(url, token):
#     async with aiohttp.ClientSession() as session:
#         headers = {'Authorization': f'Bearer {token}'}
#         async with session.get(url, headers=headers) as response:
#             if response.status == 200:
#                 body = await response.text()
#                 return body
#             else:
#                 return f"Error: {response.status}"
#
# def getImgUrls(sightings,token):
#     urls = list(map(lambda sighting: sighting.sighPicture, sightings))
#     loop = asyncio.get_event_loop()
#     tasks = [fetch(url) for url in urls]
#     # tasks = [asyncio.create_task(fetchAsync(url, token)) for url in urls]
#     # tasks = [fetch(url) for url in urls]
#     results = loop.run_until_complete(asyncio.gather(*tasks))
#
#     for result in results:
#         print(result)



