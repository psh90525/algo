def solution(n, edge):
    node = [[] for _ in range(n + 1)]
    dist_list = [-1 for _ in range(n + 1)]

    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])

    bfs(1, dist_list, node)

    return dist_list.count(max(dist_list))


def bfs(v, visited, adj):
    count = 0

    q = list([[v, count]])

    while q:
        value = q.pop(0)
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])
