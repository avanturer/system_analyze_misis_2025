def main(csv_graph: str) -> list[list[int]]:
    edges = csv_graph.strip().split('\n')

    delimiter = ';' if ';' in edges[0] else ','
    edges_parsed = [tuple(map(int, edge.split(delimiter))) for edge in edges]

    vertices = set()
    for v_from, v_to in edges_parsed:
        vertices.add(v_from)
        vertices.add(v_to)
    n = max(vertices)

    matrix = [[0] * n for _ in range(n)]
    for v_from, v_to in edges_parsed:
        matrix[v_from - 1][v_to - 1] = 1

    return matrix