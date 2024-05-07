#!/usr/bin/python3
"""queries Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(
            url.format(subreddit), headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
