#!/usr/bin/python3
"""
queries Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """function that queries the Reddit API"""

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    if response.status_code == 200:
        data = response.json().get("data")

        for i in data.get("children", []):
            print(i.get("data").get("title"))
    else:
        print(None)
