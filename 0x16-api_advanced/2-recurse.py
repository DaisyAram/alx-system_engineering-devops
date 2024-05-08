#!/usr/bin/python3
"""Contains recurse function"""
import requests
import sys


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
        }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        return None

    data = response.json()
    if data.get("error"):
        print("Error fetching data: {}".format(data.get("error")))
        return None

    children = data["data"]["children"]

    for post in children:
        hot_list.append(post["data"]["title"])

    after = data["data"]["after"]
    if after:
        return recurse(subreddit, hot_list)
    else:
        return hot_list
