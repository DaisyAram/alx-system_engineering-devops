#!/usr/bin/python3
"""
queries Reddit API and prints the titles of the first 10 hot 
posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """function that queries the Reddit API"""

    response = requests.get(
            'https://www.reddit.com/r/{}/about.json'.format(subreddit), headers={
                'User-Agent': 'Custom'}
            )
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"][:10]:
            print(post['data']['title'])
    else:
        print(None)
