#!/usr/bin/python3
"""queries Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    url = 'https://www.reddit.com/dev/api/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'google/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
