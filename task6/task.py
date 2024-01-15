import json
import numpy as np

def list_of_reviews_from_json(reviews_str, template):
    reviews = json.loads(reviews_str)
    reviews_list = [0] * len(template)

    for i, review in enumerate(reviews):
        if isinstance(review, list):
            for el in review:
                reviews_list[template[el]] = i + 1
        else:
            reviews_list[template[review]] = i + 1

    return reviews_list

def task(*args):
    experts_count = len(args)
    template = {}
    reviews_count = 0

    for review_set in json.loads(args[0]):
        if isinstance(review_set, list):
            for elem in review_set:
                template[elem] = reviews_count
                reviews_count += 1
        else:
            template[review_set] = reviews_count
            reviews_count += 1

    matrix = []

    for reviews_str in args:
        matrix.append(list_of_reviews_from_json(reviews_str, template))

    x = np.array(matrix)
    matrix_sum = np.sum(x, axis=0)

    # дисперсия
    D = np.var(matrix_sum) * reviews_count / (reviews_count - 1)
    D_max = experts_count ** 2 * (reviews_count ** 3 - reviews_count) / 12 / (reviews_count - 1)

    return format(D / D_max, ".2f")

A = '["1", ["2", "3"], "4", ["5", "6", "7"], "8", "9", "10"]'
B = '[["1", "2"], ["3", "4", "5"], "6", "7", "9", ["8", "10"]]'
C = '["3", ["1", "4"], "2", "6", ["5", "7", "8"], ["9", "10"]]'

print(task(A, B, C))
