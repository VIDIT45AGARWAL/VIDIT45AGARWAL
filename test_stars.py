def starred_repos_counter(data):
    """
    Extracts the count of repositories starred by the user.
    """
    if data and data.get('data') and data['data'].get('user'):
        starred = data['data']['user'].get('starredRepositories')
        if starred and 'totalCount' in starred:
            return starred['totalCount']
    return 0

sample_data = {
    'data': {
        'user': {
            'starredRepositories': {
                'totalCount': 44
            }
        }
    }
}

count = starred_repos_counter(sample_data)
print("Starred repos count:", count)
assert count == 44
print("Tests passed successfully!")
