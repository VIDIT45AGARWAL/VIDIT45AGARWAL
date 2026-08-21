import requests
import os
import json

HEADERS = {'authorization': 'token '+ os.environ['ACCESS_TOKEN']}
USER_NAME = os.environ['USER_NAME']

query = '''
query ($owner_affiliation: [RepositoryAffiliation], $login: String!, $cursor: String) {
    user(login: $login) {
        repositories(first: 100, after: $cursor, ownerAffiliations: $owner_affiliation) {
            totalCount
            edges {
                node {
                    ... on Repository {
                        nameWithOwner
                        stargazers {
                            totalCount
                        }
                    }
                }
            }
            pageInfo {
                endCursor
                hasNextPage
            }
        }
    }
}'''
variables = {'owner_affiliation': ['OWNER'], 'login': USER_NAME, 'cursor': None}

request = requests.post('https://api.github.com/graphql', json={'query': query, 'variables':variables}, headers=HEADERS)
print(json.dumps(request.json(), indent=2))
