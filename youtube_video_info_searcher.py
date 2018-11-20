import os
import time
import google.oauth2.credentials
import csv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# Read channel and keywords info from csv
def read_channel_keywords(channel_keyword_csv, search_list):
    with open(channel_keyword_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            search_list.append([row[0], row[1]])


# generate the row for csv file
def generate_result_csv(search_result_csv, final_video_list):
    with open(search_result_csv, 'w', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['Channel', 'Keyword', 'Title', 'Publish Time', 'View Count', 'URL'])
        for result in final_video_list:
            w.writerow([result[key] for key in result.keys()])


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_channelID_by_username(client, **kwargs):
    response = client.channels().list(
        **kwargs
    ).execute()
    return response['items'][0]['id']


def get_video_list_by_keyword(client, **kwargs):
    response = client.search().list(
        **kwargs
    ).execute()
    return response


def get_videos_list_by_id(client, **kwargs):
    response = client.videos().list(
        **kwargs
    ).execute()
    return response


def get_all_channel_info(search_list, service, part, restype, maxResults, raw_video_list, pages, final_video_list):
    def get_final_video_list(service, part, channel_name, q, restype, channelId, maxResults, raw_video_list, pages,
                             final_video_list):
        def get_raw_video_list_by_keyword(service, part, q, restype, channelId, maxResults, raw_video_list, pages):
            response = get_video_list_by_keyword(service,
                                                 part=part,
                                                 q=q,
                                                 type=restype,
                                                 channelId=channelId,
                                                 maxResults=maxResults)
            while pages > 0:
                if response['items'] is not None:
                    raw_video_list.extend(response['items'])
                if 'nextPageToken' not in response:
                    break
                else:
                    response = get_video_list_by_keyword(service,
                                                         part=part,
                                                         q=q,
                                                         type=restype,
                                                         channelId=channelId,
                                                         maxResults=maxResults,
                                                         pageToken=response['nextPageToken'])
                pages -= 1
            return raw_video_list

        get_raw_video_list_by_keyword(service, part, q, restype, channelId, maxResults, raw_video_list, pages)
        for video in raw_video_list:
            temp_video_dict = dict()
            video_response = get_videos_list_by_id(service,
                                                   part='snippet,contentDetails,statistics',
                                                   id=video['id']['videoId'])
            temp_video_dict['channel_name'] = channel_name
            temp_video_dict['keyword'] = q
            temp_video_dict['title'] = video_response['items'][0]['snippet']['title']
            temp_video_dict['publish_time'] = video_response['items'][0]['snippet']['publishedAt']
            temp_video_dict['view_count'] = video_response['items'][0]['statistics']['viewCount']
            temp_video_dict['url'] = 'https://www.youtube.com/watch?v=' + video_response['items'][0]['id']
            final_video_list.append(temp_video_dict)

    for keyword in search_list:
        channel_ID = get_channelID_by_username(service,
                                               part='contentDetails',
                                               forUsername=keyword[0])
        get_final_video_list(service, part, keyword[0], keyword[1], restype, channel_ID, maxResults, raw_video_list,
                             pages,
                             final_video_list)


if __name__ == '__main__':
    search_result_csv = 'search_result_' + str(time.asctime(time.localtime(time.time()))) + '_.csv'
    channel_keyword_csv = 'channel_keywords.csv'
    search_list = list()
    CLIENT_SECRETS_FILE = "client_secret.json"
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    keyword = 'pokemon'
    channel_name = 'IGNentertainment'
    order = 'date'
    results_per_page = 50
    pages = 2
    part = 'snippet'
    restype = 'video'
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    raw_video_list = list()
    final_video_list = list()

    read_channel_keywords(channel_keyword_csv, search_list)
    get_all_channel_info(search_list, service, part, restype, results_per_page, raw_video_list,
                         pages,
                         final_video_list)
    generate_result_csv(search_result_csv, final_video_list)
