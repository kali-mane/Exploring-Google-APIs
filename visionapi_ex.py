from base64 import b64encode
from os.path import join, basename
from sys import argv
import json
import requests
import argparse

url = 'https://vision.googleapis.com/v1/images:annotate'

result_dir = 'json'
api_key = 'ur api key'
image_filename =  'D:\\Machine Learning\\Project\\outputfiles\\MDS.png'

def get_api_key():
    print("inside get_image..")
    parse = argparse.ArgumentParser()
	
    parse.add_argument("-k", "--api_key", required=True, help="vision api key")
    args = parse.parse_args()
    api_key = args.api_key
    print("image_file : ", api_key)
    return api_key
	


def make_image_data(image_filename):
    """
    image_filename is a list of filename strings
    Returns a list of dicts formatted as the Vision API
        needs them to be
    """
    img_requests = []
    with open(image_filename, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 1
                    }]
            })
    return img_requests


def get_response():
#   api_key = get_api_key()
    response = requests.post(url,
                data=make_image_data(image_filename),
                params={'key': api_key},
                headers={'Content-Type': 'application/json'})

    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
    else:
        for idx, resp in enumerate(response.json()['responses']):
            t = resp['labelAnnotations'][0]
            print(t)


if __name__ == '__main__':
    get_response()
