import json
import numpy as np

def get_clusters_from_str(str_json):
    str_json = str_json.strip("[]")
    str_split = str_json.split(",")
    clusters = []
    cluster_read = False
    for substr in str_split:
        current_cluster = cluster_read
        if '[' in substr:
            substr = substr[1:]
            cluster_read = True
        if ']' in substr:
            substr = substr[:-1]
            cluster_read = False

        if not current_cluster:
            clusters.append([int(substr)])
        else:
            clusters[-1].append(int(substr))
    return clusters

def get_matrix_from_expert(str_json: str):
    clusters = get_clusters_from_str(str_json)
    n = sum(len(cluster) for cluster in clusters)
    matrix = np.ones((n, n), dtype=int)
    worse = []

    for cluster in clusters:
        for worse_elem in worse:
            for elem in cluster:
                matrix[elem - 1][worse_elem - 1] = 0
        for elem in cluster:
            worse.append(elem)

    return matrix

def get_AND_matrix(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)

def get_OR_matrix(matrix1, matrix2):
    return np.maximum(matrix1, matrix2)

def get_clusters(matrix, est1, est2):
    clusters = {}
    rows, cols = matrix.shape
    exclude = []

    for row in range(rows):
        if row + 1 in exclude:
            continue
        clusters[row + 1] = [row + 1]

        for col in range(row + 1, cols):
            if matrix[row][col] == 0:
                clusters[row + 1].append(col + 1)
                exclude.append(col + 1)

    result = []

    for k in clusters:
        if not result:
            result.append(clusters[k])
            continue

        for i, elem in enumerate(result):
            if np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1]) and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1]):
                result[i].extend(clusters[k])
                break
            if np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1]) or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1]):
                result = result[:i] + [clusters[k]] + result[i:]
                break

        result.append(clusters[k])

    final = [r if len(r) > 1 else r[0] for r in result]
    return str(final)

def task(string1, string2):
    mx1 = get_matrix_from_expert(string1)
    mx2 = get_matrix_from_expert(string2)
    mxAND = get_AND_matrix(mx1, mx2)
    mxAND_T = get_AND_matrix(mx1.T, mx2.T)
    mxOR = get_OR_matrix(mxAND, mxAND_T)
    clusters = get_clusters(mxOR, mx1, mx2)
    return clusters

print(task('[1,[2,3],4,[5,6,7],8,9,10]', '[[1,2],[3,4,5],6,7,9,[8,10]]'))
