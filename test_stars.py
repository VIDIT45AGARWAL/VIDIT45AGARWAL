def stars_counter(data):
    total_stars = 0
    if data:
        for node in data:
            if node and node.get('node'):
                repo_node = node['node']
                if 'stargazerCount' in repo_node and repo_node['stargazerCount'] is not None:
                    total_stars += repo_node['stargazerCount']
                elif repo_node.get('stargazers') and repo_node['stargazers'].get('totalCount') is not None:
                    total_stars += repo_node['stargazers']['totalCount']
    return total_stars

data = [
    {'node': {'nameWithOwner': 'VIDIT45AGARWAL/GopherSQL', 'stargazerCount': 35}},
    {'node': {'nameWithOwner': 'VIDIT45AGARWAL/legacy-repo', 'stargazers': {'totalCount': 5}}},
    {'node': None},
    None
]
print("Calculated stars:", stars_counter(data))
assert stars_counter(data) == 40
print("Tests passed successfully!")
