import requests
from config import *


headers = {
    'Cookie': Cookie,
    'User-Agent': UserAgent,
    'X-CSRFToken': XCSRFToken,
    'X-IG-App-ID': XIGAppID,
    'X-IG-WWW-Claim': XIGWWWClaim,
}


def getUserID(username=None):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    request = requests.get(url, headers=headers)
    if request.status_code == 404:
       return 404 
    r = request.json()
    return r['data']['user']['id']


def getStories(username=None):
    
    storyList = []
    userID = getUserID(username)
    
    if userID == 404:
       return 404  

    url = f"https://i.instagram.com/api/v1/feed/reels_media/?reel_ids={userID}"
    request = requests.get(url, headers=headers)
    r = request.json()

    if len(r['reels_media']) == 0:
       return 400 

    for strory in r['reels'][userID]['items']:
        if 'video_versions' in strory:
            media = strory['video_versions'][0]['url']
            type = 'video'
        else:
            media = strory['image_versions2']['candidates'][0]['url']
            type = 'photo'

        storyDict = {
            'media' : media,
            'type': type
        }

        storyList.append(storyDict)
    
    return storyList
