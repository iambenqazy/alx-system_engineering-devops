#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
  """
  Queries the Reddit API to get the subscriber count for a subreddit.

  Args:
      subreddit: The name of the subreddit (without the 'r/').

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
  """

  # Base URL for subreddit information
  url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"

  # Set a custom User-Agent header to avoid throttling
  headers = {"User-Agent": "My Reddit Subscriber Counter Script v1.0"}

  # Send GET request without following redirects
  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException:
    return 0  # Any error, return 0 subscribers

  # Parse JSON response
  data = response.json()

  # Check for valid subreddit data (data key exists)
  if "data" not in data:
    return 0

  # Extract subscriber count from data
  subscribers = data["data"].get("subscribers", 0)

  return subscribers
