#!/usr/bin/env python3
import requests
import sys

def main(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Get only the first 10 commits
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        main(repo_name, owner_name)
    else:
        print("Usage: script.py repository_name owner_name")
