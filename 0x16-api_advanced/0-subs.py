#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Send GET request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Return 0 if the subreddit is invalid or request fails
    if response.status_code != 200:
        return 0

    try:
        # Parse JSON response
        results = response.json().get("data", {})
        return results.get("subscribers", 0)
    except ValueError:
        return 0
