INF = 999999999 # 9 자리수

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
	'''
    [노드0과 노드0 간선 비용, 노드0과 노드1 간선 비용, 노드0과 노드2 간선 비용]
    [노드1과 노드0 간선 비용, 노드1과 노드1 간선 비용, 노드1과 노드2 간선 비용]
    [노드2와 노드0 간선 비용, 노드2와 노드1 간선 비용, 노드2와 노드2 간선 비용]
    '''
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)