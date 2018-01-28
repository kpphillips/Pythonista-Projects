
import requests
import json
from PIL import Image
import Constants


def getRandomPhotoUrl():
    url = 'http://tinyfac.es/api/users'
    r = requests.get(url)
    parsed_json = json.loads(r.content)
    avatarUrl = parsed_json[0]['avatars'][2]['url']
    return avatarUrl


def analizeRandomPhoto():
    headers = {
        "app_id": Constants.app_id,
        "app_key": Constants.app_key
    }

    imageUrl = getRandomPhotoUrl()
    payload = '{"image":' + '"' + imageUrl + '"' + '}'

    imageResponse = requests.get(imageUrl, stream=True)
    im = Image.open(imageResponse.raw)
    im.show()

    url = "https://api.kairos.com/detect"

    r = requests.post(url, data=payload, headers=headers)

    parsed_json = json.loads(r.content)
    attr = parsed_json['images'][0]['faces'][0]['attributes']
    print(json.dumps(attr, indent=2, sort_keys=True))

    return attr


analizeRandomPhoto()