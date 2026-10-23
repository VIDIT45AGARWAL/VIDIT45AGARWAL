import requests
import os
import json

HEADERS = {'authorization': 'token '+ os.environ['ACCESS_TOKEN']}
USER_NAME = os.environ['USER_NAME']

query = '''
query ($login: String!) {
    user(login: $login) {
        starredRepositories {
            totalCount
        }
    }
}'''
variables = {'login': USER_NAME}

request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables':variables}, headers=HEADERS)
print(json.dumps(request.json(), indent=2))
