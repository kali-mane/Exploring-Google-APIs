import numpy as np
from matplotlib import pyplot as plt
import cv2
import argparse


face_cascade = cv2.CascadeClassifier('D:\\FROM DOWNLOADS\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\FROM DOWNLOADS\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')


def get_image_paths():
    parse = argparse.ArgumentParser()
    
    parse.add_argument("-i", "--input_file", required=True, help="Input jpg file to process along with the path")
    parse.add_argument("-o", "--output_file", required=True, help="Output file path and name to save the procesed image")

    args = parse.parse_args()
    input_filepath   = args.input_file
    output_filepath = args.output_file

    return input_filepath, output_filepath


def detect_face():
    input_filepath, output_filepath  = get_image_paths()
    image = cv2.imread(input_filepath)
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)

    ims = cv2.resize(image, (960, 540)) 

    cv2.imshow('image', ims)
    cv2.imwrite(output_filepath, image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_face()
