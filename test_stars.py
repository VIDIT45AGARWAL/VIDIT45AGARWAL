def stars_counter(data):
    total_stars = 0
    if data:
        for node in data:
            print("node:", node)
            if node and node.get('node') and node['node'].get('stargazers'):
                total_stars += node['node']['stargazers'].get('totalCount', 0)
    return total_stars

data = [{'node': {'stargazers': {'totalCount': 5}}}, {'node': None}, None]
print(stars_counter(data))
