from urllib.parse import urlparse, urlencode, parse_qs
from urllib.request import urlopen
from apiclient.discovery import build
import argparse
import codecs


def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-k", "--developer_key", required=True, help="Developer Key to be used to access the API")
    parse.add_argument("-q", "--query", required=True, help="Input search string")
    parse.add_argument("-o", "--order", required=True, help="Order by criteria based on which videos will be searched")

    args = parse.parse_args()
    developer_key = args.developer_key
    query = args.query
    order = args.order

    return developer_key, query, order


def youtube_search():

    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
   
    DEVELOPER_KEY, input_query, input_order = get_arguments()
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(part="id,snippet", q=input_query, maxResults=10, order=input_order).execute()
    
    for result in search_response.get("items", []):
            if result["id"]["kind"] == "youtube#video":
                title       = result["snippet"]["title"]
                description = result["snippet"]["description"]
                title_encoded = title.encode('raw_unicode_escape')
                description_encoded = description.encode('raw_unicode_escape')
                print(title_encoded)
                print(description_encoded)
                print("\n")

if __name__ == '__main__':
    youtube_search()
