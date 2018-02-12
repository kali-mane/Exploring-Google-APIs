# Image detection using Google Cloud Vision API
import os
import io
import argparse
from google.cloud import vision
from google.cloud.vision import types


def get_image():
    parse = argparse.ArgumentParser()
	
    parse.add_argument("-i", "--image_file", required=True, help="path\to\image\file")
    args = parse.parse_args()
    image_file = args.image_file
    print("image_file : ", image_file)
    return image_file
    

def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
        image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        print(label.description, label.score)


if __name__ == '__main__':
     inp_file = get_image()
     detect_faces(inp_file)
