# Exploring Google APIs

Author : Maneesha Vinayak

face_detection : This will detect the face of a person in an image. The script used openCV to detect the face.
  
    The script needs two input parameters -
    -i input_file  = input image name along with the input path
    -o output_file = path and name to store the processed image


youtube_videos : This will fetch the list of top 10 youtube videos and their description based on the order like viewCount, rating etc.
The script uses Google's Youtube api. 
  
    The script needs three input parameters -
    -k developer_key = used to access the api
    -q query         = search keyword to be searched
    -o order         = used to order the videos in the response based on date, rating, relevance, videoCount, viewCount


visionapi_test.py : This will recognize the image being processed
    
    The script needs one input parameter -
    -i   image_file  = input image file

