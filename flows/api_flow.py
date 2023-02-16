import requests
from prefect import flow, task
from random import randint
from typing import List, Dict

URL = 'https://jsonplaceholder.typicode.com/posts'

@task
def get_posts():
    res = requests.get(URL)
    print(res.status_code)
    return res.json()

@task
def count_posts_by_user(posts: List[Dict]) -> List[Dict]:
    counts = {}

    for post in posts:
        if post['userId'] in counts:
            counts[post['userId']] += 1
        else:
            counts[post['userId']] = 1

    count_list = []

    for user_id in counts:
        count_list.append(
            {
                'userId': user_id,
                'count': counts[user_id]
            }
        )

    return count_list

@flow
def api_flow():
    posts = get_posts()
    counts_by_user = count_posts_by_user(posts)

    return counts_by_user

print(api_flow())
