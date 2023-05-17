#!/usr/bin/python3
"""
A script that lists 10 commits (from the most recent to oldest) of a repository by a specific user.
"""
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    try:
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f'{sha}: {author}')
    except ValueError:
        print('Invalid JSON')

