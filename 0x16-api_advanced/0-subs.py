#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit.
    
    Args:
    subreddit (str): The name of the subreddit to query.
    
    Returns:
    int: The number of subscribers or 0 if subreddit is not found or any error occurs.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        results = response.json().get("data", {})
        return results.get("subscribers", 0)
    except requests.RequestException:
        return 0
