#!/usr/bin/python3
"""queries Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit), {
                headers='User-Agent': 'google/1.0'}
            )
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
