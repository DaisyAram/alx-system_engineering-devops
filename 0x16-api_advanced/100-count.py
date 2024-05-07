#!/usr/bin/python3
"""
 recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
import requests
import json

def get_hot_posts(subreddit, after=None):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 25}
    if after:
        params['after'] = after
    headers = {
        'User-Agent': 'My custom user agent'
    }
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['children'], data['data']['after']
    else:
        return [], None

def count_words_helper(subreddit, word_list, posts, counts):
    if not posts:
        return counts
    post = posts.pop(0)
    title = post['data']['title'].lower()
    for word in word_list:
        if word in title:
            counts[word] = counts.get(word, 0) + title.count(word)
    after = post['data'].get('after')
    if after:
        posts_after, _ = get_hot_posts(subreddit, after)
        posts.extend(posts_after)
    return count_words_helper(subreddit, word_list, posts, counts)

def count_words(subreddit, word_list):
    posts, _ = get_hot_posts(subreddit)
    counts = {}
    for word in word_list:
        counts[word] = 0
    return count_words_helper(subreddit, word_list, posts, counts)
